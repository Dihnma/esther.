users = {
    'obi': '1234',
    'ada': '5678',
    'eze': '1122',
    'ugo': '3456',
}
username = input("what is your username: ")
password = input("what is your password: ")


for key, value in users.items():
    if username == key and password == value:
        print("Login successful")
        break
else:
    print("Invalid username or password")
