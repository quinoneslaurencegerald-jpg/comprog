balance = 10000

while True:
    print("\nMoney Withdrawal System:")
    print("1. Withdraw")
    print("2. Check Balance")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        try:
            amount = float(input("Enter amount to withdraw: "))

            if amount > balance:
                print("Insufficient funds!")

                while True:
                    print("\nWhat would you like to do?")
                    print("1. Try Again")
                    print("2. Check Balance")
                    print("3. Exit")

                    option = input("Choose: ")

                    if option == "1":
                        break
                    elif option == "2":
                        print(f"Current Balance: {balance}")
                    elif option == "3":
                        print("Exiting program...")
                        exit()
                    else:
                        print("Invalid option.")

            elif amount <= 0:
                print("Enter a valid amount.")

            else:
                balance -= amount
                print(f"Withdrawal successful!")
                print(f"Remaining Balance: {balance}")

        except ValueError:
            print("Ivalid input! Please enter a number.")

    elif choice == "2":
        print(f"Current Balance: {balance}")

    elif choice == "3":
        print("Thank you! Goodbye.")
        break

    else:
        print("Invalid choice. Try again.")
