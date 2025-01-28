import pyzipper

def crack_zip(zip_path, pass_file_path):
    try:
        # Open the ZIP 
        with pyzipper.AESZipFile(zip_path) as fileobject:
            print("Attempting to crack the password...")

            #  pass.txt file 
            with open(pass_file_path, 'r') as pass_file:
                passwords = pass_file.readlines()

            # Attempt each password from the pass.txt file
            for password in passwords:
                password = password.strip()  # Remove any leading/trailing spaces or newlines
                print(f"Trying password: {password}")  # Display the password being tested
                
                try:
                    # Try setting the password and testing it
                    fileobject.setpassword(password.encode('utf-8'))
                    if fileobject.testzip() is None:  # This checks if the password works
                        print(f"Password found: {password}")
                        return  # Stop execution 
                except RuntimeError:
                    pass  # If the password is incorrect, continue testing the next one
            
            print("Password not found. Try expanding the password list.")
    
    except FileNotFoundError:
        print(f"File not found: {zip_path}")
    except pyzipper.BadZipFile:
        print("Invalid ZIP file or not an AES-encrypted ZIP.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input the path to your zip file and the pass.txt file
zip_file_path = input("Enter the path to the password-protected zip file: ").strip()
pass_file_path = "pass.txt"  # Folder Name 

# Call the function with the paths
crack_zip(zip_file_path, pass_file_path)
