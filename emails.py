Email: lindsay.ward@jcu.edu.au
Is your name Lindsay Ward? (Y/n)
Email: abe@gmail.com
Is your name Abe? (Y/n) y
Email: jimbo546@hotmail.com
Is your name Jimbo546? (Y/n) no
Name: Jim Boh
Email:

Lindsay Ward (lindsay.ward@jcu.edu.au)
Abe (Abe@gmail.com)
Jim Boh (jimbo546@hotmail.com)


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()