# Income Tax Calculation System (Python Micro-project)

A small web app that calculates income tax under the **old** and **new** regimes
and tells the user which one is cheaper.

## Tech used
| Part      | Technology                      | File                     |
|-----------|---------------------------------|--------------------------|
| Backend   | Python 3 + Flask                | `app.py`                 |
| Logic     | Pure Python functions           | `tax_calculator.py`      |
| Frontend  | HTML (Jinja template)           | `templates/index.html`   |
| Design    | CSS (transitions, animation)    | `static/style.css`       |

## Folder structure
```
income_tax_system/
├── app.py
├── tax_calculator.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## How to run
```
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000 in your browser.

To test only the calculation logic (no browser): `python tax_calculator.py`

## How it works
1. User fills the form -> browser sends it to Flask (`POST /`).
2. `app.py` validates the numbers and calls `compare_regimes()`.
3. `tax_calculator.py` applies deductions, slab rates, Section 87A rebate and 4% cess.
4. Flask sends the result to `index.html`, which shows both regimes side by side.

## Tax rules used
* New regime: standard deduction 75,000; slabs 0/5/10/15/20/25/30%; no tax up to 12 lakh taxable income (87A).
* Old regime: standard deduction 50,000; slabs 0/5/20/30%; deductions 80C, 80D, 80CCD(1B), home loan interest, HRA; no tax up to 5 lakh (87A).
* 4% Health & Education Cess on both.

## Limitations (good points to mention in viva)
* Surcharge for income above 50 lakh is not included.
* Senior-citizen slabs are not included.
* HRA exemption is entered directly, not calculated.
* Rates are stored at the top of `tax_calculator.py`, so they are easy to update after every Budget.

## Ideas for improvement
Save calculations in SQLite, add a PDF download, add senior-citizen slabs, add a chart using JavaScript.
