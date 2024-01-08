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
    if (math_operation != "+") and (math_operation != "-") and (math_operation != "*") and (math_operation != "/") and (math_operation != "**"):
        raise ValueError("Invalid input")

    first_number = input("Enter first number: ")
    if not first_number.isnumeric():
        raise ValueError("Invalid input")

    second_number = input("Enter second number: ")
    if not second_number.isnumeric():
        raise ValueError("Invalid input")
    
    first_number, second_number = int(first_number), int(second_number)
    
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
        print("Result:", main())