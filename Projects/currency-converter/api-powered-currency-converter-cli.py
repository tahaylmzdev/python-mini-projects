import requests
import json
import time

FILE_NAME = "Currencies.json"

def main():
    menu()

def menu():
    print("""----------------------------------------------
    Welcome to API-Powered Currency Converter CLI
    ----------------------------------------------
    """)
    wMenu = input("""Please choose an option (1/2/0):
                           1) Convert currency
                           2) List/search currencies
                           0) Exit
                           > """)

    if wMenu == "1":
        convert_currency()
    elif wMenu == "2":
        list_search()
    elif wMenu == "0":
        print("Well, have a nice day!")
    else:
        print("Please enter valid data")
        return menu()

def fetch_currencies():
    try:
        url = "https://api.frankfurter.dev/v1/latest?base=USD"
        response = requests.get(url)

        data = response.json()

        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(data, f)
    except Exception:
        print("An error occurred")

def convert_currency():
    fetch_currencies()
    first_done = False
    second_done = False
    amount_done = False

    with open(FILE_NAME, "r") as file:
        currencies = json.load(file)

    print("""--------------------------
        Converter
--------------------------
        """)
    while first_done == False:
        first_currency = input("""Please enter your currency code (ex: USD/EUR/TRY)
        > """).upper()

        if first_currency in currencies["rates"]:
            first_done = True
        elif first_currency == "USD":
            first_done = True

    while second_done == False:
        second_currency = input("""Please enter your currency code that you would like to convert (ex: USD/EUR/TRY)
        > """).upper()

        if first_currency == second_currency:
            print("""You cannot convert to same currency!
            """)
        elif second_currency in currencies["rates"]:
            second_done = True
        elif second_currency == "USD":
            second_done = True

    while amount_done == False:
        try:
            amount = float(input(f"""Please enter how much you would like to convert {first_currency} to {second_currency}
            > """))
            if amount > 0:
                amount_done = True
            else:
                print("You cannot enter value below zero!")
        except ValueError:
            print("Please enter valid data")

    if first_currency == "USD":
        first_rate = 1.0
    else:
        first_rate = currencies["rates"][first_currency]

    if second_currency == "USD":
        second_rate = 1.0
    else:
        second_rate = currencies["rates"][second_currency]

    converted_result = (second_rate / first_rate) * amount
    print(f"""{amount} of {first_currency} equals to {converted_result:.2f}{second_currency}""")

    back_to_menu()

def list_search():
    fetch_currencies()
    with open(FILE_NAME, "r") as file:
        currencies = json.load(file)

    currency = input("""Please enter the currencies code to search it
               > """).upper()

    print("Connecting to bank API...")
    time.sleep(1)
    print("Accessing data base...")
    time.sleep(1.7)
    print("Searching for the currency...")
    time.sleep(1)

    if currency == "USD":
        print("""The currency has been found!
            USD --> 1.0 based on USD""")
        back_to_menu()
        return

    if currency in currencies["rates"]:
        print(f"""The currency has been found!
            {currency} --> {currencies["rates"][currency]} based on USD""")
        back_to_menu()
    else:
        print(f"""unfortunately, we couldn't find {currency} in the data base!""")

        again_check = False

        while again_check == False:
            wmenu = input("\nWould you try again ? (y/n): ")
            wmenu = wmenu.strip().lower()

            if wmenu == "y":
                print("\nSure!\n")
                return list_search()
            elif wmenu == "n":
                again_check = True
                back_to_menu()
                break
            else:
                print("\nPlease enter valid data.")

def back_to_menu():
    menu_check = False

    while menu_check == False:
        wmenu = input("\nWould you like to get back to menu? (y/n): ")
        wmenu = wmenu.strip().lower()

        if wmenu == "y":
            print("\nSure!\n")
            return menu()
        elif wmenu == "n":
            print("\nThanks for using the Currency Converter! Have a nice day!\n")
            menu_check = True
        else:
            print("\nPlease enter valid data.")

if __name__ == "__main__":
    main()