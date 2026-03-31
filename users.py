users = []

while True:
    print("Users: \n\n1. Show user  \n2. Add user  \n3. Update user  \n4. Delete user  \n5. Exit")
    choice = input("\nChoose number: ")

    if choice == "1":
        print(users if users else "No users.")

    elif choice == "2":
        users.append(input("Enter name: "))
        print("Added!")

    elif choice == "3":
        if not users:
            print("Nothing to update.")
            continue
        
        name_to_find = input("Enter name to update: ")
        if name_to_find in users:
            idx = users.index(name_to_find)
            users[idx] = input("Enter new name: ")
            print("Updated!")
        else:
            print("User not found.")

    elif choice == "4":
        if not users:
            print("Nothing to delete.")
            continue
            
        name_to_remove = input("Enter name to delete: ")
        if name_to_remove in users:
            
            users.remove(name_to_remove)
            print("Deleted!")
        else:
            print("User not found.")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
