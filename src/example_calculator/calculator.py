class Calc:

    def add(self, x: int, y: int):
        return x + y

    def subtract(self, x: int, y: int):
        return x - y

    def multiply(self, x:int, y:int):
        return x * y

    def divide(self, x: int, y: int):
        if y != 0:
            return x / y
        else:
            print("Error: Cannot divide by zero!")



"""
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")


    while True:
        choice = input("Enter choice (1-4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            else:
                print("Result:", divide(num1, num2))
            break
        else:
            print("Invalid input. Please try again.")


"""
