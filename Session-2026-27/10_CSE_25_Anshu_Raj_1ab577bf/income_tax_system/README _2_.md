# Income Tax Calculation System

GOVERNMENT POLYTECHNIC PATNA 7

Department of Computer Science and Information Technology

PROJECT REPORT

Submitted in partial fulfilment of the requirements for the Diploma in CSE

A Python and Flask Microproject

Subject  Python Programming

Submitted by

| S No | Student Name | Roll Number |
| --- | --- | --- |
| 1 | KRISHNA KUMAR SINGH | 07/CSE/25 |
| 2 | ANSHU RAJ | 10/CSE/25 |
| 3 | RICHA KUMARI | 11/CSE/25 |
| 4 | TANMAY RAJ | 08/CSE/25 |
| 5 | NIKHIL RAJ | 09/CSE/25 |
| 6 | VIVEK KUMAR | 12/CSE/25 |

Under the Guidance of Lect Sonal Kumari

Academic Year 2025–28

## Certificate

This is to certify that the project report entitled Income Tax Calculation System is submitted by Krishna Kumar Singh, Anshu Raj, Richa Kumari, Tanmay Raj, Nikhil Raj and Vivek Kumar in partial fulfilment of the requirements for the Diploma in Computer Science and Engineering at Government Polytechnic Patna 7 for the academic year 2025–28.

The report describes a Python and Flask application for comparing income tax under the configured old and new tax regimes. Approval of the submitted work is to be confirmed by the signatures below.

Project Guide  Lect Sonal Kumari

Signature  __________________________

Head of Department  Neha Rani

Signature  __________________________

Principal or Examiner  __________________________

Date  __________________________

## Acknowledgement

We express our sincere gratitude to our project guide, Lect Sonal Kumari, for guidance and support in preparing this microproject. We thank the Head of the Department, Neha Rani, and the faculty members of the Computer Science and Information Technology department for their encouragement.

This project helped us connect Python programming concepts with a practical calculation task. We also thank our families and friends for their support during the preparation of the project and report.

The Project Team

## Abstract

The Income Tax Calculation System is an educational Python microproject that estimates tax under two configured Indian income tax regimes. It accepts salary or business income, other income and selected deduction claims. The system applies progressive tax slabs, the configured standard deduction, rebate, new regime marginal relief and four percent cess. It compares the results and displays the regime with the lower calculated tax.

The application uses Flask for request handling, a separate Python module for calculations, a Jinja HTML template for presentation and CSS for responsive styling. The result includes taxable income, tax on slabs, rebate, cess, estimated monthly income after tax, a saving comparison and expandable slab details. The standalone Python module also prints a demonstration result.

This report explains the aim, tools, installation procedure, architecture, calculation method, tested outputs, limitations and possible improvements. Four output figures are based on executed backend calculations and are rendered as console images. They are not browser screenshots. Flask template rendering and validation were checked separately using its test client.

The code labels its tax configuration for FY 2026–27 and AY 2027–28. The report documents that implementation without independently certifying the legal validity of the settings. It does not calculate surcharge or special rate income and uses simplified deduction eligibility assumptions.

## Contents

- [Title Aim and Introduction](#1-title-aim-and-introduction)
- [Tools Used and Project Files](#2-tools-used-and-project-files)
- [Procedure and System Design](#3-procedure-and-system-design)
- [Calculation Method and Program Logic](#4-calculation-method-and-program-logic)
- [Output Examples](#5-screenshots-of-output-and-verification)
- [Conclusion and Future Scope](#7-limitations-conclusion-and-future-scope)

## 1 Title Aim and Introduction

### Title

Income Tax Calculation System

### Aim

To develop a Python based income tax calculation system that accepts income and deduction details, calculates tax under the old and new regimes, and identifies the regime with the lower calculated tax.

### Introduction

Manual tax calculations require several steps, including selecting the applicable slabs, subtracting eligible deductions, applying a rebate and adding cess. Repeating these steps for two regimes can lead to arithmetic mistakes. This project demonstrates how functions, conditional statements, loops and dictionaries can automate that process.

The program separates the web interface from the calculation engine. This makes the tax functions easier to understand and test independently. The comparison includes taxable income, tax before rebate, rebate or relief, cess, final tax and an estimate of income after tax.

### Objectives

- Accept annual income, other income, employment type and deduction claims.

- Apply progressive slabs instead of applying one rate to the entire income.

- Compare both configured regimes and show the calculated saving.

- Handle blank, nonnumeric and negative form inputs.

- Demonstrate modular Python programming and Flask form handling.

### Scope

The source labels its configuration for a resident individual below 60 years for FY 2026–27 and AY 2027–28. This report describes those source settings; it does not independently certify their legal validity. The system handles ordinary slab based income using simplified deduction assumptions and is an educational estimate, not a complete tax filing system.

## 2 Tools Used and Project Files

### Hardware requirements

A desktop or laptop capable of running Python and a modern browser is sufficient. A keyboard and display are needed for entering inputs and viewing outputs. The source does not specify a minimum processor, RAM or storage requirement.

### Software requirements

- Python 3 to execute the application and calculation functions.

- Flask version 3.0 or later, as specified in requirements.txt.

- A browser for the intended local web interface.

- A text editor or IDE, such as IDLE or Visual Studio Code, and a terminal.

### app.py

Creates the Flask application, registers an Indian currency formatting filter, defines read_amount for input conversion, and handles GET and POST requests at the root route. It calls compare_regimes only when validation succeeds and sends form values, errors and results to index.html.

### tax_calculator.py

Contains the slab settings, deduction caps, currency formatting, progressive tax calculation, old and new regime functions and comparison logic. It has no dependency on Flask and includes a runnable demonstration under the main guard.

### requirements.txt and README.md

The requirements file declares Flask>=3.0. The README explains installation, intended folder structure, application flow and limitations.

### index.html and style.css

The Jinja template provides income and deduction fields, error messages, comparison cards, a saving verdict and expandable slab tables. CSS adds a navy header, teal highlights, tax share bars, responsive grids, focus effects and reduced motion support. No JavaScript or database is required.

### Compiled bytecode

tax_calculator.cpython-315.pyc is a CPython 3.15 cache file. It is not needed to run the readable source on another compatible Python 3 environment; Python generates its own cache as needed.

## 3 Procedure and System Design

### Installation and execution

1. Place app.py, tax_calculator.py and requirements.txt in one project folder. Open a terminal in that folder.

2. Install the dependency using the following command.

python -m pip install -r requirements.txt

3. Test the standalone calculation engine.

python tax_calculator.py

4. For the web version, place index.html in templates and style.css in static, then start the server.

python app.py

5. Open http://127.0.0.1:5000 in a browser. Enter income and deductions, submit the form and inspect the comparison. Stop the server with Ctrl+C. The supplied debug=True setting is intended for local development.

### System design

The intended data flow is browser form → Flask route → input validation → comparison function → calculation results → Jinja template → browser. On GET, the application prepares an empty form. On POST, it reads the submitted fields and either returns errors or calculates results.

### Input validation

read_amount removes commas and surrounding spaces, treats an empty field as zero, and converts other values with float. It records an error for text that cannot be converted or for a negative value. If combined income is zero and no earlier error exists, the route asks the user to enter annual income.

### Inputs and outputs

Inputs are income, other_income, income_type, sec_80c, sec_80d, sec_nps, home_loan and hra. Output dictionaries include gross income, deductions, taxable income, slab rows, rebate, cess, final tax, estimated annual and monthly income after tax, effective rate, notes, preferred regime and saving.

## 4 Calculation Method and Program Logic

### Income and deductions

Gross income = annual income + other income. For salaried input, the new regime standard deduction is min(annual income, Rs 75,000), and the old regime standard deduction is min(annual income, Rs 50,000). Non salaried input receives no standard deduction. Taxable income is limited to a minimum of zero.

In the old regime, the code caps 80C at Rs 1,50,000, 80D at Rs 50,000, additional NPS at Rs 50,000 and home loan interest at Rs 2,00,000. HRA is entered as an exemption amount and is not calculated or capped by this program. A note is returned when a capped claim exceeds its configured limit. These are implementation assumptions; actual eligibility is not validated.

### Configured slab rates

New regime: up to Rs 4 lakh at 0%; Rs 4–8 lakh at 5%; Rs 8–12 lakh at 10%; Rs 12–16 lakh at 15%; Rs 16–20 lakh at 20%; Rs 20–24 lakh at 25%; above Rs 24 lakh at 30%.

Old regime: up to Rs 2.5 lakh at 0%; Rs 2.5–5 lakh at 5%; Rs 5–10 lakh at 20%; above Rs 10 lakh at 30%. Each percentage applies only to the portion within that slab.

### Rebate and final tax

The code applies a new regime rebate up to Rs 60,000 when taxable income is at most Rs 12 lakh, and an old regime rebate up to Rs 12,500 when taxable income is at most Rs 5 lakh. New regime marginal relief reduces tax before cess when that tax exceeds income above the rebate threshold. The same rebate field stores either rebate or marginal relief.

Cess = tax after rebate × 4%. Total tax = tax after rebate + cess. Estimated income after tax = gross income − total tax; the monthly estimate divides this amount by 12. It excludes payroll deductions and is not an actual salary slip take home amount.

### Comparison algorithm

Calculate both regimes, subtract new regime tax from old regime tax, and recommend the lower value. An absolute difference below Rs 1 is treated as a tie. format_inr rounds displayed values to whole rupees and inserts Indian digit grouping; internal calculations retain floating point values.

## 5 Screenshots of Output and Verification

The following figures show actual results from the supplied calculation functions, rendered as console images. The first case also matches the module’s built in demonstration. Flask template rendering was checked separately with its test client; these figures are not browser screenshots.

### Case 1 Salary with Section 80C

![Verified calculation output 1](assets/output_1.png)

For a salary of Rs 12 lakh and an 80C claim of Rs 1.5 lakh, new regime tax is zero and old regime tax is Rs 1,17,000.

### Case 2 Old regime with substantial deductions

![Verified calculation output 2](assets/output_2.png)

For a salary of Rs 14 lakh with the stated claims, old regime tax is Rs 75,400 and new regime tax is Rs 81,900. The old regime saves Rs 6,500.

## 6 Further Output Examples

### Case 3 New regime marginal relief

![Verified calculation output 3](assets/output_3.png)

At a salary of Rs 12.8 lakh, new regime taxable income is Rs 12.05 lakh. Marginal relief reduces tax before cess to Rs 5,000; with Rs 200 cess, total tax is Rs 5,200.

### Case 4 Deduction cap enforcement

![Verified calculation output 4](assets/output_4.png)

An 80C claim of Rs 2 lakh is limited to Rs 1.5 lakh. Including the standard deduction, old regime deductions total Rs 2 lakh, and a cap notification is returned.

## 7 Limitations Conclusion and Future Scope

### Verification summary

The standalone demonstration and four calculation scenarios were executed. Assertions verified the first case’s tax totals, the marginal relief result, the deduction cap and the second case’s comparison. Flask request tests also verified the initial page, a valid form submission, negative input, nonnumeric input and zero income. The four calculation cases were checked independently. Visual browser interaction was not tested.

### Limitations

- No surcharge, special rate capital gains, senior citizen slabs or nonresident rules are implemented.

- The 80D cap is simplified, and HRA and home loan eligibility conditions are not checked.

- The program does not save calculations, manage accounts or export reports.

- Tax settings are hardcoded and require review when the applicable rules change.

- Validation does not explicitly reject NaN or infinity, and pure calculation functions assume valid nonnegative inputs.

- Displayed rupee rounding is not a complete implementation of statutory tax rounding rules.

### Conclusion

The project demonstrates how Python can automate progressive tax calculations and compare two sets of tax rules. Its separation of Flask request handling from pure calculation functions supports independent testing and makes the code suitable for learning modular programming. The backend produces consistent results for the documented scenarios; the supplied frontend presents the results with clear comparisons and expandable details.

### Future scope

Extend automated regression tests; validate finite numeric values; use decimal arithmetic and explicit tax rounding; support financial year selection and verified tax configurations; calculate HRA eligibility; extend deductions, surcharge and income categories; and optionally add SQLite history, comparison charts and PDF export.

### Project references

Primary sources reviewed: app.py, tax_calculator.py, README.md and requirements.txt, index.html and style.css supplied with the project. The .pyc cache was identified as a generated artifact and was not used as source code. The tax module points to https://incometax.gov.in for verification of applicable rules. The report documents source behavior and does not claim an independent legal review of those settings.

## 8 Functional Requirements and Scope

### Purpose of the application

The application helps a user compare the two tax regimes configured in the supplied Python module. A successful calculation requires annual income, an income category and any deduction claims that the user wishes to include. Other income and deduction fields may be left blank because the request handler converts blank amounts to zero. The comparison is an estimate under the implemented assumptions rather than a complete income tax return.

### Functional requirements

The system must accept salaried or business input, combine annual and other income, apply the appropriate standard deduction, calculate progressive tax and compare the two results. Under the old regime it must apply the selected caps to deduction claims and identify any capped claim in a note. It must display both results even when one regime produces a lower tax, because the user needs to understand the comparison.

### Result requirements

Each regime returns gross income, total deductions, taxable income, slab rows, slab tax, rebate or relief, cess, final tax, effective rate and an estimate of monthly income after tax. The comparison returns better and saving values. A difference below one rupee is treated as a tie. The template uses these outputs directly, so the calculation module remains the single source of numeric results.

### Quality and scope requirements

The code should be easy to read, run locally and update when its configuration changes. A separate calculation module supports independent checks. The current implementation has no accounts, payment processing, return filing or persistent history. These features should not be described as completed capabilities. The program also assumes ordinary slab based income and does not verify deduction eligibility from supporting documents.

## 9 Frontend Design and User Interaction

### HTML and Jinja presentation

index.html is a server rendered Jinja template, not a standalone calculator page. Flask supplies form, result, errors, caps and cess variables. Template expressions repopulate input fields after submission, display configured deduction limits and format money with the inr filter. Opening the template directly from a file browser does not execute these expressions.

### Input form

The form submits a POST request to the root URL. Its income type menu offers Salaried and Business or Self employed. The remaining controls collect annual income, other income and five old regime claims. The inputs are text fields with a numeric input hint. The novalidate attribute means the application relies on server validation rather than the browser’s native form checking. Clear form links back to the initial GET page.

### Comparison and breakdown

When a result exists, a verdict explains whether the new regime, old regime or neither is preferable under the entered assumptions. Two cards show total tax and detailed figures. The lower tax card receives a Best badge. A horizontal bar illustrates tax and estimated income remaining as percentages of gross income. Expandable details elements reveal the individual slab calculations without requiring JavaScript.

### Responsive styling and accessibility

style.css uses CSS variables, Grid and Flexbox. At wider viewports the form and results are placed alongside each other; smaller screens stack the content. Result cards also change layout with a media query. Error messages use an alert role and the results region uses aria live. Focus styling supports keyboard users, and a reduced motion query disables transitions and animations. Google Fonts are optional external resources with fallback fonts specified in CSS.

## 10 Backend Modules and Function Design

### Request handling in app py

Flask creates the application and registers format_inr as the inr template filter. The index function handles both GET and POST. GET prepares the empty view, while POST collects form values and creates a claims dictionary. The comparison runs only when the errors list is empty. render_template then creates the page with either the results or validation messages.

### Progressive tax engine

calculate_slab_tax iterates over ordered upper limits and rates. For each band it determines the amount of taxable income that falls between the previous limit and the current limit. It multiplies this amount by the rate divided by one hundred. The function stores a readable range, rate, amount and tax for the template, while accumulating the total. It stops once there is no remaining income above the lower bound.

### Shared result construction

_build_result is used by both regime functions. It calls the slab engine, applies a configured rebate or marginal relief, calculates cess and builds a consistent result dictionary. Reusing this function avoids duplicating the same final calculation in two places. It also ensures the template receives the same field names for each card.

### Regime comparison and formatting

calculate_new_regime and calculate_old_regime determine their deductions and taxable income before calling the shared builder. compare_regimes calls both functions and compares final tax. format_inr rounds an amount to an integer for display and groups digits in the Indian style. This formatting does not change the underlying floating point amounts stored in the result dictionaries.

## 11 Input Validation and Data Handling

### Numeric conversion

read_amount first removes commas, trims surrounding spaces and checks whether the remaining string is empty. Empty input becomes 0.0. Other input is converted with float. A ValueError adds a field specific message rather than allowing the request to continue silently with invalid data. For example, letters in annual income produce the message Annual income must be a number.

### Negative and zero values

Negative amounts produce a cannot be negative message and a zero return value. Because the error remains in the errors list, the tax comparison is not executed for that request. If income and other income total zero and no previous error is recorded, the handler adds Enter your annual income to calculate tax. Blank deductions remain valid because they represent no claim.

### Claims and deductions

The handler constructs the dictionary with known keys for 80C, 80D, additional NPS, home loan interest and HRA. The calculation module limits capped values using min. It adds the allowed amounts to the standard deduction and clamps taxable income at zero. HRA has no configured cap and is accepted as an already calculated exemption. Direct users of the Python functions must supply suitable values because the functions do not repeat the Flask validation.

### Data storage and remaining checks

The source does not connect to a database or write calculation history to a file. Form values are processed during the request and inserted in the returned HTML. The implementation should add an explicit finite number check because float accepts special values such as NaN and infinity. A future production version would also need suitable deployment controls and a deliberate decision about whether any user data should be retained.

## 12 Worked Calculation Examples

### Salary of twelve lakh rupees

For annual salary of Rs 12,00,000, no other income and an 80C claim of Rs 1,50,000, the new regime deducts Rs 75,000. Taxable income becomes Rs 11,25,000. Slab tax is Rs 20,000 on the Rs 4–8 lakh band plus Rs 32,500 on the remaining Rs 3,25,000, giving Rs 52,500. The implemented rebate removes that amount, so cess and final tax are zero.

### Old regime for the same salary

The old regime deducts the Rs 50,000 standard deduction and Rs 1,50,000 under 80C. Taxable income is Rs 10,00,000. The first Rs 2,50,000 is untaxed, the next Rs 2,50,000 contributes Rs 12,500, and the next Rs 5,00,000 contributes Rs 1,00,000. Slab tax is Rs 1,12,500. There is no rebate at this taxable income. Four percent cess is Rs 4,500, making the final tax Rs 1,17,000.

### When old regime deductions help

For salary of Rs 14,00,000, claims of Rs 1,50,000 under 80C, Rs 50,000 under 80D, Rs 50,000 under NPS, Rs 2,00,000 home loan interest and Rs 1,00,000 HRA, the old regime’s total deductions including the standard deduction are Rs 6,00,000. Taxable income is Rs 8,00,000 and final tax is Rs 75,400. The new regime produces Rs 81,900, giving an old regime saving of Rs 6,500 under the code assumptions.

### Marginal relief near the threshold

For salary of Rs 12,80,000, the new regime taxable income is Rs 12,05,000. The slab tax is Rs 60,750. Because the extra taxable income above Rs 12 lakh is only Rs 5,000, the implemented relief reduces tax before cess to Rs 5,000. Cess is Rs 200 and final tax is Rs 5,200. The result dictionary records this relief within its rebate field.

## 13 Testing Approach and Observations

### Checks performed

The calculation module’s built in demonstration was executed, along with four independent input scenarios. Assertions checked the zero new regime tax and Rs 1,17,000 old regime tax for the first case, the preferred old regime in the second case, the Rs 5,200 marginal relief result and the deduction cap in the fourth case. These observed values support the examples printed in the report.

### Flask request checks

A temporary local project layout placed the template in templates and the stylesheet in static. Flask’s test client returned HTTP 200 for the initial page and a valid submission. The valid submission contained the expected new regime verdict. Invalid text, negative income and zero combined income returned the expected error messages. These checks exercised request handling and template rendering without making a claim about manual browser interaction.

### Additional useful cases

Further regression checks should cover both sides of each slab boundary, both rebate limits, non salaried input, positive other income with zero primary income and deductions greater than gross income. These cases would help identify accidental configuration changes. They are proposed checks and are not presented as completed tests. Nonfinite numbers should become explicit rejection cases after validation is strengthened.

### Interpretation of output figures

The four images earlier in the report show actual calculated values rendered in a console style format. They are reproducible from the Python functions and are clearly distinguished from browser screenshots. The application’s real browser display can be captured after running python app.py and submitting the same values. Comparing those displays with the recorded figures is a useful final demonstration step.

## 14 User Manual and Troubleshooting

### Preparing the folder

Keep app.py and tax_calculator.py in the main project directory. Put index.html inside a templates directory and style.css inside a static directory. Keep requirements.txt in the main directory. The supplied .pyc cache is not required; Python can build a cache suitable for the interpreter in use. Running the source is preferable to depending on a cache generated by another Python version.

### Starting and using the application

Open a terminal in the project directory, run python -m pip install -r requirements.txt and then python app.py. Visit http://127.0.0.1:5000 in a browser. Select the income type, enter annual income and other income, and enter eligible claim amounts. Press Calculate tax. Compare final tax, deductions, rebate, cess and the expandable slab information. Use Clear form to begin a fresh calculation.

### Common installation problems

If Flask is missing, install requirements with the same Python interpreter that starts the application. If the browser reports that the local address cannot be reached, check that the terminal still shows the server running. TemplateNotFound usually means index.html has not been placed inside templates. An unstyled page may indicate that style.css is missing from static. External font failure should still leave readable fallback text.

### Understanding the result

The recommendation compares only the calculated tax for the supplied inputs and configured assumptions. The monthly take home estimate is gross income minus tax divided by twelve; it excludes provident fund, professional tax and other payroll deductions. A cap note means the program used a smaller allowed claim than the user entered. Users should not interpret an accepted claim as proof that it is legally eligible.

## 15 Learning Outcomes and Maintenance

### Python concepts demonstrated

The project uses constants for configuration, lists of tuples for slab definitions, dictionaries for named inputs and outputs, loops for slab processing and conditional statements for rebates and comparison. Functions divide the work into manageable tasks. The main guard permits an executable demonstration without running that demonstration when the module is imported by Flask.

### Web development concepts demonstrated

The implementation connects an HTML form to Python through an HTTP POST request. Flask processes the request and Jinja inserts dynamic values into the returned page. CSS provides presentation independently from the calculation rules. The project demonstrates how an interface can display the same calculation output in summary cards and detailed slab rows without maintaining a second tax engine in JavaScript.

### Maintaining the configuration

Tax slabs, standard deductions, rebate settings and deduction caps are placed near the top of tax_calculator.py. A maintainer can update these settings after reviewing the applicable official rules. Any update should be accompanied by recalculated examples and regression checks. Changing a financial year label alone does not establish that the tax configuration is correct for that year.
