print("""----------------------------
Welcome to Calculator
----------------------------""")
def main():
    num1 = get_first_number()
    op = get_operator()
    num2 = get_second_number()
    calculator(num1, op, num2)

def get_first_number():
    try:
        num1 = float(input("Please enter your first number: "))
        return num1
    except ValueError:
        print("Your input is not valid")
        return get_first_number()

def get_operator():
    op = input("Please enter the operator you would like to do ? (+, -, *, /")

    if op in ["+", "-", "*", "/"]:
        return op
    else:
        print("Please enter a valid operator")
        return get_operator()

def get_second_number():
    try:
        num2 = float(input("Please enter your second number: "))
        return num2
    except ValueError:
        print("Your input is not valid")
        return get_second_number()

def calculator(num1, op, num2):
    match op:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("You cannot divide something with \"0\"")
                return

    print(f"The result of {num1} {op} {num2} is {result}")

def new_cal():
    again = input("Would like to make another calculation ? (y/n)")
    if again in ["y", "n"]:
        print("""Sure, there you go!
        
        """)
        return get_first_number()
    else:
        print("Please enter valid input")
        return new_cal()

if __name__ == "__main__":
    main()