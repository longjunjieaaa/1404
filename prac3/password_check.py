number = 6
def password_1():
    password = input("Enter your password:")
    if password < number:
        password = input("Enter your password again: ")
    print('*' * password)
