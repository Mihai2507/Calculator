import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def power(a, b):
    return a ** b


def square(a):
    return a ** 2


def square_root(a):
    return math.sqrt(a)


def modulo(a, b):
    return a % b


def logarithm(a, b):
    return math.log(a, b)


def absolute(a):
    return abs(a)


def logartihm_ln(a):
    e = 2.718218284590
    return math.log(a, e)


def factorial(a):
    return math.factorial(a)


def exponential(a):
    return math.pow(a, 2)


def menu():
    print("OPTIONS:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square")
    print("7. SquareRoot")
    print("8. Modulo")
    print("9. Logarithm")
    print("10. Absolute")
    print("11. Logarithm_ln")
    print("12. Factorial")
    print("13. Exponential")
    print("14. Exit")


if __name__ == '__main__':
    while True:
        menu()
        choice = int(input("Enter your choice(number):\n"))
        if choice in [1, 2, 3, 4, 5, 8, 9]:
            number1 = float(input("Enter the first number:\n"))
            number2 = float(input("Enter the second number:\n"))
            match choice:
                case 1:
                    print(add(number1, number2))
                case 2:
                    print(subtract(number1, number2))
                case 3:
                    print(multiply(number1, number2))
                case 4:
                    print(divide(number1, number2))
                case 5:
                    print(power(number1, number2))
                case 8:
                    print(modulo(number1, number2))
                case 9:
                    print(logarithm(number1, number2))
                case _:
                    print("Invalid choice.")
                    break
        elif choice in [6, 7, 10, 11, 12, 13]:
            number = float(input("Enter a number:\n"))
            match choice:
                case 6:
                    print(square(number))
                case 7:
                    print(square_root(number))
                case 10:
                    print(absolute(number))
                case 11:
                    print(logartihm_ln(number))
                case 12:
                    print(factorial(int(number)))
                case 13:
                    print(exponential(number))
        elif choice == 14:
            print("Thank you for using Calculator!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
            continue
        continue_choice = input("Do you want to perform another operation? (yes/no):\n").lower()
        if continue_choice != 'yes':
            print("Thank you for using Calculator!")
            break
