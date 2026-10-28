"""
tax_calculator.py
-----------------
Backend logic of the Income Tax Calculation System.
Pure Python - no web code here, so it can be tested on its own.

Rules used (Indian resident individual, below 60 years, FY 2026-27 / AY 2027-28).
All numbers are kept at the top so they can be updated easily when the
Budget changes them. Always verify with https://incometax.gov.in
"""

INF = float("inf")

# ---------------------------------------------------------------- tax rules
# Each slab is (upper limit of slab, tax rate in %)
NEW_REGIME_SLABS = [
    (400000, 0), (800000, 5), (1200000, 10), (1600000, 15),
    (2000000, 20), (2400000, 25), (INF, 30),
]
OLD_REGIME_SLABS = [
    (250000, 0), (500000, 5), (1000000, 20), (INF, 30),
]

STANDARD_DEDUCTION_NEW = 75000   # salaried only
STANDARD_DEDUCTION_OLD = 50000   # salaried only

REBATE_LIMIT_NEW, REBATE_MAX_NEW = 1200000, 60000   # Section 87A (new)
REBATE_LIMIT_OLD, REBATE_MAX_OLD = 500000, 12500    # Section 87A (old)

CESS_RATE = 4  # Health & Education Cess (%)

# Maximum deduction allowed per section (old regime only)
DEDUCTION_CAPS = {
    "sec_80c": 150000,    # PPF, LIC, ELSS, tuition fees ...
    "sec_80d": 50000,     # Health insurance premium (simplified cap)
    "sec_nps": 50000,     # 80CCD(1B) - extra NPS contribution
    "home_loan": 200000,  # Section 24(b) - home loan interest
}
DEDUCTION_NAMES = {
    "sec_80c": "Section 80C",
    "sec_80d": "Section 80D",
    "sec_nps": "Section 80CCD(1B)",
    "home_loan": "Home loan interest",
}


# ---------------------------------------------------------------- helpers
def format_inr(amount):
    """Format a number in Indian style: 1234567 -> ₹12,34,567"""
    n = int(round(amount))
    digits = str(abs(n))
    if len(digits) > 3:
        head, tail = digits[:-3], digits[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        digits = ",".join(parts + [tail])
    return ("-" if n < 0 else "") + "₹" + digits


def calculate_slab_tax(taxable_income, slabs):
    """Apply slab rates. Returns (total tax, list of rows for the table)."""
    total = 0.0
    rows = []
    lower = 0
    for upper, rate in slabs:
        if taxable_income <= lower:
            break
        amount_in_slab = min(taxable_income, upper) - lower
        tax = amount_in_slab * rate / 100
        if lower == 0:
            label = "Up to " + format_inr(upper)
        elif upper == INF:
            label = "Above " + format_inr(lower)
        else:
            label = format_inr(lower) + " to " + format_inr(upper)
        rows.append({"range": label, "rate": rate,
                     "amount": amount_in_slab, "tax": tax})
        total += tax
        lower = upper
    return total, rows


def _build_result(name, gross, deductions, taxable, slabs,
                  rebate_limit, rebate_max, marginal_relief, notes):
    """Common steps: slab tax -> rebate -> cess -> final numbers."""
    slab_tax, rows = calculate_slab_tax(taxable, slabs)

    # Section 87A rebate
    rebate = 0.0
    if taxable <= rebate_limit:
        rebate = min(slab_tax, rebate_max)
    elif marginal_relief:
        # Just above the limit, tax can never exceed the extra income
        extra_income = taxable - rebate_limit
        if slab_tax > extra_income:
            rebate = slab_tax - extra_income

    tax_after_rebate = slab_tax - rebate
    cess = tax_after_rebate * CESS_RATE / 100
    total_tax = tax_after_rebate + cess
    take_home = gross - total_tax

    tax_pct = (total_tax / gross * 100) if gross > 0 else 0
    return {
        "name": name,
        "gross": gross,
        "deductions": deductions,
        "taxable": taxable,
        "rows": rows,
        "slab_tax": slab_tax,
        "rebate": rebate,
        "cess": cess,
        "total_tax": total_tax,
        "take_home": take_home,
        "monthly": take_home / 12,
        "effective_rate": tax_pct,
        "tax_pct": round(tax_pct, 2),
        "home_pct": round(100 - tax_pct, 2),
        "notes": notes,
    }


# ---------------------------------------------------------------- regimes
def calculate_new_regime(income, other_income, salaried):
    gross = income + other_income
    std = min(income, STANDARD_DEDUCTION_NEW) if salaried else 0
    taxable = max(0, gross - std)
    return _build_result("New regime", gross, std, taxable, NEW_REGIME_SLABS,
                         REBATE_LIMIT_NEW, REBATE_MAX_NEW, True, [])


def calculate_old_regime(income, other_income, salaried, claims):
    gross = income + other_income
    std = min(income, STANDARD_DEDUCTION_OLD) if salaried else 0

    allowed_total = std
    notes = []
    for key, claimed in claims.items():
        allowed = min(claimed, DEDUCTION_CAPS.get(key, claimed))
        if claimed > allowed:
            notes.append(DEDUCTION_NAMES[key] + " limited to " +
                         format_inr(allowed))
        allowed_total += allowed

    taxable = max(0, gross - allowed_total)
    return _build_result("Old regime", gross, allowed_total, taxable,
                         OLD_REGIME_SLABS, REBATE_LIMIT_OLD,
                         REBATE_MAX_OLD, False, notes)


def compare_regimes(income, other_income, salaried, claims):
    """Calculate both regimes and decide which one is better."""
    new = calculate_new_regime(income, other_income, salaried)
    old = calculate_old_regime(income, other_income, salaried, claims)

    difference = old["total_tax"] - new["total_tax"]
    if abs(difference) < 1:
        better, saving = "same", 0
    elif difference > 0:
        better, saving = "new", difference
    else:
        better, saving = "old", -difference
    return {"new": new, "old": old, "better": better, "saving": saving}


# ---------------------------------------------------------------- self test
if __name__ == "__main__":
    r = compare_regimes(1200000, 0, True, {"sec_80c": 150000})
    print("New regime tax:", format_inr(r["new"]["total_tax"]))
    print("Old regime tax:", format_inr(r["old"]["total_tax"]))
    print("Better regime :", r["better"], "saves", format_inr(r["saving"]))
