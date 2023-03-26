dict_name = {}
print()
print('---------------------------------   WELCOME TO OUR CONTACT BOOK :)  ------------------------------')
while True:
    print()
    print("Commands:\nA for Add\nD for Delete\nE for Edit\nP for viewing all contacts\nS for Search\nQ for Quit.")
    print()
    command = input("Enter command:").upper()
    print()

    if command == "A":
        name = input("Enter the name:")
        phone = input("Enter phone number:")
        email = input("Enter email address:")
        location = input("Enter the location:")
        dict_name[name] =[]
        dict_name[name].append(phone)
        dict_name[name].append(email)
        dict_name[name].append(location)

    elif command == "D":
        name = input("Enter name to delete:")
        if name in list(dict_name.keys()):
            del dict_name[name]
        else:
            print("No person with this name found.")

    elif command == "E":
        name = input("Enter the name to edit:")

        if name not in list(dict_name.keys()):
            print("No person with this name found.")

        else:
            what = input("1 to Edit Name \n2 to edit phone number \n3 to edit email address \n4 to edit location \nEnter your command:")
            if what == "1":
                new_name = input("Enter the new name:")
                dict_name[new_name] = dict_name[name]
                del dict_name[name]
            elif what == '2':
                new_phone = int(input("Enter the new phone number:"))
                dict_name[name][0] = new_phone
            elif what == '3':
                new_email=input('enter new email id:')
                dict_name[name][1] = new_email
            elif what == '4':
                new_location=input('enter new location:')
                dict_name[name][2] = new_location
            else:
                print("Invalid response.")

    elif command == "P":
        print("|{:^20}|{:^22}|{:^30}|{:^22}|".format("NAME", "PHONE","EMAIL","LOCATION"))
        print('-'*99)
        for i, j in dict_name.items():
            print("|{:^20}|{:^22}|{:^30}|{:^22}|".format(i, j[0],j[1],j[2]))
            print("|{:^20}|{:^22}|{:^30}|{:^22}|".format(' ', ' ',' ',' '))

    elif command == "S":
        name = input("Enter name to search:")
        print()
        if name in list(dict_name.keys()):
            print("Name : {}    \nPhone number: {} \nemail id: {} \nlocation: {}".format(name, dict_name[name][0],dict_name[name][1],dict_name[name][2]))
        else:
            print("No person with this name found.")

    elif command == "Q":
        break

    else:
        print("Invalid command.")
print()
print("Program End.")
print()
