def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def times(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b

print("Basic Calculator")
print("1. Add")
print("2. Minus")
print("3. Times")
print("4. Divide")

choice = input("Choose: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Answer:", add(num1, num2))

elif choice == '2':
    print("Answer:", minus(num1, num2))

elif choice == '3':
    print("Answer:", times(num1, num2))

elif choice == '4':
    print("Answer:", divide(num1, num2))

else:
    print("Invalid input!")
