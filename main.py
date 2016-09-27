import csv

with open("main.csv") as open_file:
    data = list(csv.reader(open_file))
    new = ""
    while new != 'c':
        username = input("Username: ")
        password = input("Password: ")
        for row in data:
            if username == row[0] and password == row[1]:
                print("Welcome! Here is your info for the login:")
                print(row)
                new = input("Would you like to [c]reate a new user or [l]og out? ")
                if new == 'c'.lower():
                    break
                else:
                    print("Bye.")
                break
        else:
            print("Try again.")


new_username = input("New username: ")
new_password = input("New password: ")
new_full_name = input("New full name: ")
new_fact = input("New fact: ")

with open("main.csv", 'a') as open_file:
    data = csv.writer(open_file)
    data.writerow([new_username,new_password,new_full_name,new_fact])
