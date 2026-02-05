print("""----------------------------
Welcome to BMI Calculator
----------------------------""")

def main():
    w = weight()
    h = height()
    calculator(w,h)
    again()

def weight():
    try:
        w = float(input("Please enter your weight: "))
        if w <= 0:
            print("Please enter valid data")
            return weight()
        else:
            return w
    except ValueError:
        print("Please enter valid data")
        return weight()

def height():
    try:
        h = float(input("Please enter your height: "))
        if h > 3:
            h = h / 100
            return h
        else:
            return h
    except  ValueError:
        print("Please enter valid data")
        return height()


def calculator(w,h):
    r = w / (h ** 2)
    print(f"Your index is {r:.2f}")

    if r < 18.5:
        print("And you are considered as \"Underweight\" ")
    elif 18.5 <= r < 25:
        print("And you are considered as \"Normal\" ")
    elif 25 <= r < 30:
        print("And you are considered as \"Overweight\" ")
    else:
        print("And you are considered as \"Obese\" ")

def again():
    print("Thank you for using our service!")
    n = input("Would you like to make a new calculation ? (y/n): ")

    if n in ["y", "n"]:
        match n:
            case "y":
                return main()
            case "n":
                print("Well have a nice day!")
    else:
        print("Please enter valid data")
        return again()