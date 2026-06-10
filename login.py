"""
Username and password login

"""

correct_username = "Queenasa"
correct_password = "2312"
attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "queenasa" and password == "2312":
        print("Login successful")
        break
    else:
        attempts += 1
        print("Error: invalid username or password")
        if attempts >= 3:
            print("Maximum login attempts reached.")
    
    