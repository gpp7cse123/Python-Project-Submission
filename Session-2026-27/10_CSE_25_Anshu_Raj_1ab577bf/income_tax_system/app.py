"""
app.py
------
Flask web server: connects the HTML form (frontend) with tax_calculator.py
(backend).  Run with:   python app.py   then open http://127.0.0.1:5000
"""
from flask import Flask, render_template, request

from tax_calculator import (compare_regimes, format_inr,
                            DEDUCTION_CAPS, CESS_RATE)

app = Flask(__name__)
app.jinja_env.filters["inr"] = format_inr   # use {{ value|inr }} in HTML


def read_amount(form, field, label, errors):
    """Read a number from the form. Empty = 0. Bad input adds an error."""
    raw = form.get(field, "").replace(",", "").strip()
    if raw == "":
        return 0.0
    try:
        value = float(raw)
    except ValueError:
        errors.append(label + " must be a number.")
        return 0.0
    if value < 0:
        errors.append(label + " cannot be negative.")
        return 0.0
    return value


@app.route("/", methods=["GET", "POST"])
def index():
    result, errors, form = None, [], {}

    if request.method == "POST":
        form = request.form
        income = read_amount(form, "income", "Annual income", errors)
        other = read_amount(form, "other_income", "Other income", errors)
        claims = {
            "sec_80c": read_amount(form, "sec_80c", "Section 80C", errors),
            "sec_80d": read_amount(form, "sec_80d", "Section 80D", errors),
            "sec_nps": read_amount(form, "sec_nps", "NPS (80CCD1B)", errors),
            "home_loan": read_amount(form, "home_loan", "Home loan interest", errors),
            # HRA exemption is entered directly (no cap applied here)
            "hra": read_amount(form, "hra", "HRA exemption", errors),
        }
        salaried = form.get("income_type", "salaried") == "salaried"

        if income + other <= 0 and not errors:
            errors.append("Enter your annual income to calculate tax.")

        if not errors:
            result = compare_regimes(income, other, salaried, claims)

    return render_template("index.html", result=result, errors=errors,
                           form=form, caps=DEDUCTION_CAPS, cess=CESS_RATE)


if __name__ == "__main__":
    app.run(debug=True)
