# Number System Converter using Python

A simple, menu-driven Python micro-project that converts a number from one number system to Decimal, Binary, Octal, and Hexadecimal.

## Project Details

- **Project:** Number System Converter using Python
- **Subject:** Python Programming
- **Class / Semester:** CSE / 3rd
- **Academic Year:** 2026–2027
- **Team:** Sameer Kumar, Aashutosh Kumar, Dibyanshu Kumar, Chandani Kumari, Ankit Kumar, Diwakar Kumar
- **Roll Numbers:** 29–34

## Features

- Accepts input in Decimal (base 10), Binary (base 2), Octal (base 8), or Hexadecimal (base 16).
- Displays the equivalent value in all four number systems.
- Checks whether each digit is valid for the selected number system.
- Shows a clear error message for invalid input.
- Provides a menu to perform multiple conversions or exit.

## Requirements

- Python 3.8 or later
- IDLE, VS Code, or another Python editor
- Command Prompt or terminal

## How to Run

1. Save the program code as `converter.py`.
2. Open a terminal in the folder containing the file.
3. Run:

   ```bash
   python converter.py
   ```

4. Choose an input number system:
   - `1` — Decimal
   - `2` — Binary
   - `3` — Octal
   - `4` — Hexadecimal
   - `5` — Exit
5. Enter a number when prompted. The program displays its Decimal, Binary, Octal, and Hexadecimal values.

## Example

For hexadecimal input `2F`, the results are:

| Number system | Result |
|---|---:|
| Decimal | `47` |
| Binary | `101111` |
| Octal | `57` |
| Hexadecimal | `2F` |

## Invalid Input Example

Binary numbers can contain only `0` and `1`. If you enter `1021` as a binary number, the program reports an error because `2` is not a valid binary digit.

## How It Works

1. `to_decimal()` validates the input and converts it to a decimal integer.
2. `from_decimal()` converts a decimal integer to the requested base using division and remainders.
3. `convert()` combines the conversion functions.
4. `show_menu()` displays the available choices.
5. `main()` handles user input, errors, and output.

## Concepts Used

- Number systems and base conversion
- Functions
- Loops and conditional statements
- String handling
- Exception handling with `ValueError`

## Future Improvements

- Support negative and fractional numbers.
- Add a graphical interface using Tkinter.
- Support custom bases from 2 to 36.
- Show conversion steps.
- Convert multiple numbers from a file or list.
- Create a web or mobile version.

## Project Conclusion

This project demonstrates how Python can convert numbers among Decimal, Binary, Octal, and Hexadecimal systems. It also validates input and reports invalid digits clearly.
