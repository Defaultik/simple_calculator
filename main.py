class math:
    def plus(num1, num2):
        return num1 + num2


    def minus(num1, num2):
        return num1 - num2


    def multiply(num1, num2):
        return num1 * num2


    def divide(num1, num2):
        return round(num1 / num2, 3)
    

    def power(num1, num2):
        return num1 ** num2


def main():
    math_operation = input("(+, -, *, /, **)\nEnter mathematical operation: ")
    if math_operation not in ("+", "-", "*", "/", "**"):
        raise ValueError("Invalid input")

    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
    except ValueError:
        raise ValueError("Invalid input")
        
    if math_operation == "+":
        return math.plus(first_number, second_number)
    elif math_operation == "-":
        return math.minus(first_number, second_number)
    elif math_operation == "*":
        return math.multiply(first_number, second_number)
    elif math_operation == "/":
        return math.divide(first_number, second_number)
    elif math_operation == "**":
        return math.power(first_number, second_number)


if __name__ == "__main__":
    while True:
        print(f"Result: {main()}\n")