# Multi-Purpose Password Cracker

This script provides a versatile solution for cracking passwords, supporting both:

1. **ZIP file password cracking** (AES-encrypted ZIP files).
2. **Other password-protected systems**, such as login forms or text fields.

The script intelligently prompts the user to choose a mode, reads passwords from a file (`pass.txt`), and processes each password one by one.

## Features

- **Two Modes:**
  - Crack AES-encrypted ZIP file passwords using `pyzipper`.
  - Simulate password entry for other systems.
- **Custom Password Lists:** Reads passwords from an external file (`pass.txt`).
- **Real-Time Feedback:** Displays the current password being tested in the terminal.
- **Key Control:** 
  - Press `Enter` to start cracking.
  - Press `Esc` to stop the process anytime.
- **Auto-Cleanup:** Deletes entered text after each attempt in non-ZIP mode.

## Requirements

1. Python 3.6+
2. Required Libraries:
   - `pyzipper` (install using `pip install pyzipper`)
   - `pyautogui` (install using `pip install pyautogui`)
   - `keyboard` (install using `pip install keyboard`)

## How to Use

### Step 1: Install Required Libraries

Install the necessary Python libraries:

```bash
pip install pyzipper pyautogui keyboard
```

### Step 2: Prepare Your Password List

1. Create a file named `pass.txt` in the same directory as the script.
2. Add potential passwords to the `pass.txt` file, each on a new line:
   ```
   password123
   admin
   qwerty123
   mypassword
   ```

### Step 3: Run the Script

1. Save the script to a Python file, such as `password_cracker.py`.
2. Open a terminal or command prompt in the directory containing the script.
3. Run the script by executing:
   ```bash
   python password_cracker.py
   ```
4. Choose the mode when prompted:
   - **Mode 1:** Crack a ZIP file password. Provide the path to the ZIP file when requested.
   - **Mode 2:** Test passwords on other systems. Focus on the input field where passwords need to be typed.

### Step 4: Interpret Results

- For ZIP files:
  - If the correct password is found, the script displays:
    ```
    Password found: <password>
    ```
  - If no password matches, the script suggests expanding the password list.
- For other systems:
  - Each password is typed into the focused input field and displayed in the terminal.
  - You can stop the process anytime by pressing `Esc`.

##



## Notes

1. Ensure the ZIP file is AES-encrypted for compatibility with `pyzipper`.
2. Use the appropriate password list for the type of password-protected system.
3. Be cautious when testing on live systems to avoid triggering rate limits or account locks.

## Disclaimer

This script is intended for educational purposes or recovering your own password-protected files. Do not use it for unauthorized access to other people's files.

