import random
import string

print("\n------------------------------")
print("     Welcome to Password Generator     ")
print("------------------------------\n")

def main():
    menu()

def menu():
    try:
        wMenu = int(input("Please choose an option:\n"
                          "1) Create a password\n"
                          "0) Exit\n"
                          "> "))

    except ValueError:
        print("\nPlease enter valid data.\n")
        return menu()

    if wMenu in [1, 2, 3, 4, 0]:
        match wMenu:
            case 1:
                length, upper, lower, num, symbol = get_data()
                generator(length, upper, lower, num, symbol)
            case 0:
                print("\nWell, have a nice day!\n")

    else:
        print("\nPlease enter valid data.\n")
        return menu()

def get_data():
    print(" ")

    # Length
    length_done = False
    while length_done == False:
        try:
            length = int(input("""How long you'd like to your password to be ? (8-64):
                                   > """))
            if 7 < length < 65:
                length_done = True
                print(f"""Your password will be {length} character long!
                """)
            else:
                print("""Your password should between 8-64 (inclusive)
                """)
                continue
        except ValueError:
            print("Please enter valid data")
            continue

    #Upper Case Character
    upper_done = False
    while upper_done == False:
        upper = input("""
        Would you like to to be your password includes upper case ? (y/n): 
        > """).lower()

        if upper in ["y", "n"]:
            upper_done = True
        else:
            print("""Please enter valid data
            """)
            continue

    #Lower Case Character
    lower_done = False
    while lower_done == False:
        lower = input("""
        Would you like to to be your password includes lower case ? (y/n): 
        > """).lower()

        if lower in ["y", "n"]:
            lower_done = True
        else:
            print("""Please enter valid data
            """)
            continue

    #Number Character
    num_done = False
    while num_done == False:
        num = input("""
        Would you like to to be your password includes numbers ? (y/n): 
        > """).lower()

        if num in ["y", "n"]:
            num_done = True
        else:
            print("""Please enter valid data
            """)
            continue

    #Symbol Character
    symbol_done = False
    while symbol_done == False:
        symbol = input("""
        Would you like to to be your password includes symbol ? (y/n): 
        > """).lower()

        if symbol in ["y", "n"]:
            symbol_done = True
        else:
            print("""Please enter valid data
            """)
            continue
    
    if upper == lower == num == symbol == "n":
        print("You have select least one option")
        return get_data()
    else:
        return length, upper, lower, num, symbol

def generator(length,upper,lower,num,symbol):
    password = ""
    length = length + 1
    if lower == "y":
        for i in range(1, length):
            password += chr(random.randint(97, 122))
            pass
    elif upper == "y":
        for i in range(1, length):
            password += chr(random.randint(65, 90))
            pass
    elif num == "y":
        for i in range(1, length):
            password += chr(random.randint(48, 57))
            pass
    elif symbol == "y":
        for i in range(1, length):
            symbols = string.punctuation
            password += random.choice(symbols)
            pass
    temp_list = list(password)

    if upper == "y":
        for i in range(random.randint(1, length // 2)):
            random_indx = random.randint(1, length - 2)
            temp_list[random_indx] = temp_list[random_indx].upper()

    if lower == "y":
        for i in range(random.randint(1, length // 2)):
            random_indx = random.randint(1, length - 2)
            temp_list[random_indx] = temp_list[random_indx].lower()

    if num == "y":
        for i in range(random.randint(1, length // 2)):
            random_indx = random.randint(1, length - 2)
            temp_list[random_indx] = chr(random.randint(48, 57))

    if symbol == "y":
        for i in range(random.randint(1, length // 2)):
            symbols = string.punctuation
            random_indx = random.randint(1, length - 2)
            temp_list[random_indx] = random.choice(symbols)

    password = "".join(temp_list)


    print(f"""
          Generated password: {password}
          Length: {length - 1}
          
          ----------------""")

    back_to_menu()


def back_to_menu():
    menu_check = False

    while menu_check == False:
        wmenu = input("\nWould you like to get back to menu? (y/n): ")
        wmenu = wmenu.strip().lower()

        if wmenu == "y":
            print("\nSure!\n")
            return menu()
        elif wmenu == "n":
            print("\nThanks for using the Password Generator! Have a nice day!\n")
            menu_check = True
        else:
            print("\nPlease enter valid data.")

if __name__ == "__main__":
    main()