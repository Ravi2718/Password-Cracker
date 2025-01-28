import pyzipper
import pyautogui
import keyboard
import time

# Function to read passwords from the file
def read_passwords(file_path):
    try:
        with open(file_path, 'r') as file:
            passwords = file.readlines()
        return [password.strip() for password in passwords]
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# ZIP file password cracking function
def crack_zip(zip_path, passwords):
    try:
        with pyzipper.AESZipFile(zip_path) as fileobject:
            print("Attempting to crack the ZIP file password...")

            for password in passwords:
                print(f"Trying password: {password}")
                try:
                    fileobject.setpassword(password.encode('utf-8'))
                    if fileobject.testzip() is None:
                        print(f"Password found: {password}")
                        return
                except RuntimeError:
                    pass

            print("Password not found. Try expanding the password list.")
    except FileNotFoundError:
        print(f"File not found: {zip_path}")
    except pyzipper.BadZipFile:
        print("Invalid ZIP file or not an AES-encrypted ZIP.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to simulate typing the password and pressing Enter
def send_password(password):
    print(f"password: {password}")
    pyautogui.typewrite(password)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')

# Main function
def main():
    pass_file_path = "pass.txt"
    passwords = read_passwords(pass_file_path)

    if not passwords:
        print("No passwords found in the file.")
        return

    print("Select mode:")
    print("1. Crack ZIP file password")
    print("2. Crack other password-protected system")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        zip_file_path = input("Enter the path to the password-protected ZIP file: ").strip()
        crack_zip(zip_file_path, passwords)
    elif choice == '2':
        print("You have 5 seconds to focus on the input field...")
        time.sleep(5)
        print("Press 'Enter' to start sending passwords. Press 'Esc' anytime to stop the process.")

        while True:
            if keyboard.is_pressed('enter'):
                print("Started sending passwords...")
                for password in passwords:
                    if keyboard.is_pressed('esc'):
                        print("Process stopped by user.")
                        break

                    send_password(password)
                    time.sleep(10)  # Wait 10 seconds before sending the next password

                print("All passwords processed. Exiting.")
                break

            if keyboard.is_pressed('esc'):
                print("Process stopped before starting.")
                break
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()