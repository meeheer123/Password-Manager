
                                                            # Password Manager


import random
import string

# Global dictionary to store user passwords
user_passwords = {}

def register_user(username, password):
    # Store the username and password securely (e.g., in a database or encrypted file)
    user_passwords[username] = {"password": password}
    print("User registered successfully!")
    return 0

def authenticate_user(username, password):
    if username in user_passwords and user_passwords[username]["password"] == password:
        print("Authentication successful!")
        password_manager(username)
        return 0
    else:
        print("Invalid username or password.")
        return 1

def password_manager(username):
    while True:
        print("\nPassword Manager Menu:")
        print("1. Store Password")
        print("2. Get Password")
        print("3. Update Password")
        print("4. Delete Password")
        print("5. Generate Password")
        print("6. Logout")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            website = input("Enter the website name: ")
            password = input("Enter the password: ")
            store_password(username, website, password)
        elif choice == "2":
            website = input("Enter the website name: ")
            get_password(username, website)
        elif choice == "3":
            website = input("Enter the website name: ")
            password = input("Enter the new password: ")
            update_password(username, website, password)
        elif choice == "4":
            website = input("Enter the website name: ")
            delete_password(username, website)
        elif choice == "5":
            length = input("Enter the length: ")
            generate_password(length)
        elif choice == "6":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please try again.")

def store_password(username, website, password):
    if username in user_passwords:
        if "passwords" not in user_passwords[username]:
            user_passwords[username]["passwords"] = {}
        user_passwords[username]["passwords"][website] = password
        print(user_passwords)
        print("Password stored successfully!")
        return 'stored'
    else:
        print("Invalid username. Please try again.")

def get_password(username, website):
    print(user_passwords)
    if username in user_passwords and "passwords" in user_passwords[username]:
        passwords = user_passwords[username]["passwords"]
        if website in passwords:
            password = passwords[website]
            print(f"Website: {website}")
            print(f"Username: {username}")
            print(f"Password: {password}")
            return password
        else:
            print("No password found for the specified website.")
    else:
        print("Invalid username. Please try again.")

def update_password(username, website, password):

    if username in user_passwords and "passwords" in user_passwords[username]:
        passwords = user_passwords[username]["passwords"]
        if website in passwords:
            passwords[website] = password
            print("Password updated successfully!")
            return password
        else:
            print("No password found for the specified website.")
    else:
        print("Invalid username. Please try again.")

def delete_password(username, website):
    if username in user_passwords and "passwords" in user_passwords[username]:
        passwords = user_passwords[username]["passwords"]
        if website in passwords:
            del passwords[website]
            print("Password deleted successfully!")
            return 1
        else:
            print("No password found for the specified website.")
    else:
        print("Invalid username. Please try again.")

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(int(length)))
    print(f"Generated Password: {password}")
    return password

def main():
    while True:
        print("\nPassword Manager Menu:")
        print("1. Register User")
        print("2. Authenticate User")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a master password: ")
            ch1 = register_user(username, password)
        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your master password: ")
            ch2 = authenticate_user(username, password)
        elif choice == "3":
            print("Thank you for using the Password Manager!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
