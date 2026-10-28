# Student Result Calculator

A student micro-project for calculating academic results. The project
report includes a Python console implementation and a browser-based
version built with HTML, CSS, and JavaScript.

## Overview

The Student Result Calculator collects marks for five subjects,
validates the entries, and calculates the total marks, percentage,
grade, and pass/fail status. The browser version also accepts the
student's name and roll number and can print the result summary.

## Features

-   Enter marks for **English, Mathematics, Computer Science, Physics,
    and Chemistry**
-   Validate marks so each value is between **0 and 100**
-   Show a helpful message for invalid or missing entries
-   Calculate total marks out of **500**
-   Calculate percentage
-   Assign a grade based on the project's demonstration thresholds
-   Check the minimum passing mark for every subject
-   Display a subject-wise result summary
-   Reset the form and print the result (browser version)

## Technologies

-   **Python 3** --- console-based version
-   **HTML5** --- web page structure
-   **CSS3** --- styling and responsive layout
-   **JavaScript** --- input validation, calculations, grade selection,
    and result display

The browser version uses standard browser features and does not require
a JavaScript package installation. The CSS references the Inter font
from Google Fonts; if it is unavailable, fallback fonts are specified.

## Grading and passing rules

Each subject has a maximum of 100 marks. A student must score at least
**33 marks in every subject** to pass.

  Percentage                              Grade
  --------------------------------------- ----------
  90% and above                           A+
  80% to below 90%                        A
  70% to below 80%                        B
  60% to below 70%                        C
  45% to below 60%                        D
  Below 45%, if every subject is passed   E
  Any subject below 33                    F / FAIL

These are **project demonstration rules**, not necessarily the official
grading policy of any institution.

## Project files

For the browser version, keep these three files in the same folder:

``` text
student-result-calculator/
├── index.html
├── style.css
├── script.js
└── README.md
```

The report contains the HTML, CSS, and JavaScript source code. Save each
section into the corresponding file names above. The Python console
version can be saved separately as `student_result_calculator.py`.

## Run the browser version

1.  Create a project folder.
2.  Save the HTML source as `index.html`.
3.  Save the CSS source as `style.css`.
4.  Save the JavaScript source as `script.js`.
5.  Open `index.html` in a modern web browser.
6.  Enter the student's name, roll number, and marks for all five
    subjects.
7.  Select **Calculate Result** to view the summary.
8.  Select **Print Result** to print the displayed result. Use **Reset**
    to clear the form and result.

No local server is normally required for this basic browser version.

## Run the Python console version

1.  Install Python 3 if it is not already installed.
2.  Save the Python source from the report as
    `student_result_calculator.py`.
3.  Open a terminal or command prompt in that folder.
4.  Run:

``` bash
python student_result_calculator.py
```

On systems where the command is `python3`, use:

``` bash
python3 student_result_calculator.py
```

Enter a numeric mark from 0 to 100 when prompted for each subject.

## Example

Sample marks:

  Subject                      Marks
  ------------------ ---------------
  English                         80
  Mathematics                     90
  Computer Science                85
  Physics                         75
  Chemistry                       70
  **Total**            **400 / 500**

-   **Percentage:** 80.00%
-   **Grade:** A
-   **Status:** PASS

Every subject in this example has at least 33 marks.

## Validation and testing

Try these cases to check the program:

-   Valid marks such as `80, 90, 85, 75, 70` should produce 400/500,
    80.00%, grade A, and PASS.
-   A mark below 33 in any subject should produce grade F and FAIL, even
    if the overall percentage is high.
-   Text such as `abc`, a negative mark, or a mark greater than 100
    should be rejected.
-   Test grade boundaries around 45%, 60%, 70%, 80%, and 90%.

## Scope and limitations

-   Designed as an educational demonstration and micro-project.
-   Processes one student's result at a time.
-   Uses five fixed subjects, each out of 100.
-   Does not store results permanently or connect to a database.
-   Does not verify marks against official records.
-   The grading thresholds should be checked and changed if an
    institution requires a different policy.

## Possible future improvements

-   Process multiple students in one session
-   Save results to CSV or a database
-   Add student search and record management
-   Add a graphical interface or authentication
-   Add automated tests for grade boundaries and pass/fail conditions

## Academic project

Prepared as a Python Programming micro-project for the Computer Science
and Engineering (CSE) department, Government Polytechnic College, Patna
7, academic session 2026--2027.

------------------------------------------------------------------------

**Note:** The PDF report documents the source code and project
explanation; it is not itself an executable application. Create the
source files as described above to run the program.
