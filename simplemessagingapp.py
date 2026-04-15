filename = "message.txt"

try:
    with open(filename, "x") as file:
        print("File created successfully!!!")
except FileExistsError:
    print("Error, File already exists hayst")

while True:
    print("\nSimple Messaging App")
    print("1. Send a message")
    print("2. View all messages")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        message = input("Enter your message: ")
        try:
            with open(filename, "a") as file:
                file.write(message + "\n")
            print("Message saved successfully!!!")
        except Exception as e:
            print("Error writing to file: ", e)

    elif choice == "2":
        try:
            with open(filename, "r") as file:
                content = file.read()
                if content:
                    print("\nMessages: ")
                    print(content)
                else:
                    print("No messages found.")
        except Exception as e:
            print("Error reading file: ", e)

    elif choice == "3":
        print("Exiting program, byebyebyebye!!!")
        break

    else:
        print("Invalid choice, try again.")
