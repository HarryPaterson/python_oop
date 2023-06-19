class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num

    def subtract(self, num):
        self.result -= num

    def multiply(self, num):
        self.result *= num

    def divide(self, num):
        if num != 0:
            self.result /= num
        else:
            print("Error: Cannot divide by zero.")

    def clear(self):
        self.result = 0

    def get_result(self):
        return self.result

calculator = Calculator()

while True:
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        num = float(input("Enter a number to add: "))
        calculator.add(num)
    elif choice == "2":
        num = float(input("Enter a number to subtract: "))
        calculator.subtract(num)
    elif choice == "3":
        num = float(input("Enter a number to multiply: "))
        calculator.multiply(num)
    elif choice == "4":
        num = float(input("Enter a number to divide: "))
        calculator.divide(num)
    elif choice == "5":
        calculator.clear()
    elif choice == "6":
        print("Exiting the calculator.")
        break
    else:
        print("Invalid choice. Please try again.")

    print("Result:", calculator.get_result())