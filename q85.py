users = {}

def register():
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists.")
    else:
        password = input("Enter a new password: ")
        users[username] = password
        print("Registration successful.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful.")
    else:
        print("Invalid username or password.")

def main():
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()
