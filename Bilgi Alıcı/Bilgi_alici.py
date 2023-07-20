username = input("Enter your name: ")
email = input("Enter your E-mail: ")
password = input("Enter your password")
user_info = {"username": username, "email": email, "password": password}
with open('users.txt', 'a') as f:
    f.write(f"{username},{email},{password}\n")

