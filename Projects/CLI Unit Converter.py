print("""----------------------------
Welcome to Unit Converter
----------------------------""")

def main():
    un_type = type_unit()
    con_direction = selection(un_type)
    val = get_input(un_type)
    converter(un_type, con_direction, val)
    again()

def type_unit():
    un_type = input("""Which unit you would like to do ? (T/L/M)
    Temperature(T)
    Length(L)
    Mass(M)
    """)

    if un_type in ["T", "L", "M", "t", "l", "m"]:
        return un_type
    else:
        return type_unit()

def selection(un_type):
    try:
        match un_type:
            case "T" | "t":
                con_direction = int(input("""Please choose an option (1 or 2)
                    1. Celsius -> Fahrenheit
                    2. Fahrenheit -> Celsius
                    """))
            case "L" | "l":
                con_direction = int(input("""Please choose an option (1 or 2)
                    1. Kilometer -> Mile
                    2. Mile -> Kilometer
                    """))
            case "M" | "m":
                con_direction = int(input("""Please choose an option (1 or 2)
                    1. Kilogram -> Pounds
                    2. Pounds -> Kilogram
                    """))
    except ValueError:
        print("Please enter valid data")
        return selection(un_type)

    if con_direction in [1, 2]:
        return con_direction
    else:
        print("Please enter valid data")
        return selection(un_type)


def get_input(un_type):
    try:
        val = float(input("Please enter your value: "))
        if un_type in ["L", "l", "M", "m"] and val < 0:
            print("You cannot enter value below zero for this type of unit")
            return get_input(un_type)
        else:
            return val
    except ValueError:
        print("Please enter valid data")
        return get_input(un_type)

def converter(un_type, con_direction, val):
    match un_type:
        case "T" | "t":
            if con_direction == 1:
                result = f"{(val * 9/5) + 32:.2f} Fahrenheit"
            else:
                result = f"{(val-32) * 5/9:.2f} Celsius"
        case "L" | "l":
            if con_direction == 1:
                result = f"{val * 0.621371:.2f} Mile"
            else:
                result = f"{val / 0.621371:.2f} Kilometer"
        case "M" | "m":
            if con_direction == 1:
                result = f"{val * 2.20462:.2f} Pounds"
            else:
                result = f"{val / 2.20462:.2f} Kilogram"

    print(f"\nThe result is {result}\n")


def again():
    new = input("""Thanks for using our service!
    Would like to make another calculation ? (y/n): """)

    if new in ["y", "n"]:
        match new:
            case "y":
                return main()
            case "n":
                print("""Well, have a nice day!""")
    else:
        print("Please enter valid data")
        return again()

if __name__ == "__main__":
    main()



