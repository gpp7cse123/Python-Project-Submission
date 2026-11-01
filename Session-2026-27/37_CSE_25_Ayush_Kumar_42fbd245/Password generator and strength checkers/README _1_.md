# Password Generator and Strength Checker

A command-line Python application that can generate random passwords and evaluate the strength of an entered password.

## Features

- Generate passwords with a configurable length.
- Optionally include uppercase letters, numbers, and symbols.
- Uses Python's `secrets` module for cryptographically secure random selection.
- Check password strength and receive a score from 0 to 100.
- Detect common passwords, character sequences, and repeated characters.
- Display an estimated entropy value.
- Hide password input while checking strength by using `getpass`.

## Requirements

- Python 3.6 or newer
- No third-party packages are required.

## Project files

```text
password_tool_project/
├── password_tool.py
└── README.md
```

## How to run

1. Download or clone this project.
2. Open a terminal in the project folder.
3. Run:

```bash
python password_tool.py
```

On some systems, use:

```bash
python3 password_tool.py
```

## Menu options

When the program starts, it displays:

```text
=== Password Tool ===
1. Generate a password
2. Check password strength
3. Exit
```

### 1. Generate a password

- Enter a password length between 4 and 128.
- Choose whether to include uppercase letters, numbers, and symbols.
- The program displays the generated password and its estimated strength.

The generator always includes lowercase letters. It also guarantees at least one character from each optional character group that you enable.

### 2. Check password strength

- Enter the password when prompted.
- The input is hidden while typing.
- The program displays a strength label, score, estimated entropy, and improvement suggestions.

### 3. Exit

Closes the program.

## Strength labels

| Score | Strength |
|---:|---|
| 0–29 | Very Weak |
| 30–49 | Weak |
| 50–69 | Medium |
| 70–84 | Strong |
| 85–100 | Very Strong |

The score is produced by this project's own heuristic. It is not a standardized security rating.

## Security notes

- The generator uses Python's `secrets` module rather than the non-cryptographic `random` module.
- Use a different password for every account.
- Store passwords in a reputable password manager.
- Do not share generated passwords or commit real passwords to a public repository.
- The entropy value is an estimate based on the character groups detected in the password. It may overestimate the actual unpredictability of a human-created password.
- The common-password list is small and is not a substitute for checking against a comprehensive breached-password database.

## License

Add a license file if you intend to distribute or reuse this project publicly.
