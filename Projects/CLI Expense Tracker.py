print("""----------------------------
Welcome to Expense Tracker
----------------------------
""")

expenses = []
def main():
    menu()

def menu():
   print("""----------------------------
   Welcome to Main Menu
   ----------------------------
   """)
   try:
        wMenu = int(input("""Please choose an option (1/2/3/4/0): 
        1) Add expense
        2) List expenses
        3) Summary
        4) Category summary
        0) Exit
        """))

   except ValueError:
        print("Please enter valid data")
        return menu()

   if wMenu in [1, 2, 3, 4, 0]:
       match wMenu:
           case 1:
               return add_expense()
           case 2:
               return list_expenses()
           case 3:
               return summary()
           case 4:
               return category_summary()
           case 0:
               print("""Well, have a nice day!""")

   else:
       print("Please enter valid data")
       return menu()

def add_expense():
    print("""
    --------------------
        Add Expense
    --------------------
    """)
    amount_check = False
    amount = -1

    category_check = False
    category = ""

    note_check = False

    menu_check = False

    while amount_check == False:
        try:
            amount = float(input("""How much you would like to deposit ?
                                > """))
            if amount > 0:
                amount = float(amount)
                amount_check = True
            elif amount <= 0:
                print("Please enter value higher than \"0\"")

        except ValueError:
            print("Please enter valid data")

    while category_check == False:
        try:
            wcategory = int(input("""Please select one of the categories that related the your expense (1/2/3/4)
                    1) Food
                    2) Transport
                    3) Rent
                    4) Other
                    > """))
        except ValueError:
            print("Please enter valid data")
            continue

        if wcategory in [1,2,3,4]:
            match wcategory:
                case 1:
                    category = "Food"
                case 2:
                    category = "Transport"
                case 3 :
                    category = "Rent"
                case 4:
                    category = "Other"
            category_check = True
        else:
            print("Please enter valid data")

    while note_check == False:
        wnote = input("Would you like to leave a note for this expense ? (y/n): ").lower()

        if wnote == "y":
            note = input("""Sure, please enter your note: 
                > """)
            note_check = True
        elif wnote == "n":
            note = ""
            note_check = True
        else:
            print("Please enter valid data")

    expenses.append({"amount": amount, "category": category, "note": note})

    while menu_check == False:
        wmenu = input("Would like to get back to menu ? (y/n)").lower()

        if wmenu == "y":
            print("Sure!")
            return menu()
        elif wmenu == "n":
            print("Well, thanks for using us! Have a nice day!")
            menu_check = True
        else:
            print("Please enter valid data")

def list_expenses():
    menu_check = False

    if not expenses:
        print("No expenses yet.")
    else:
        print("""------List of Expenses------
        """)
        for i, item in enumerate(expenses):
            print(f"{i}) {item["amount"]} $ | {item["category"]} | {item["note"]}")


    while menu_check == False:
        wmenu = input("Would like to get back to menu ? (y/n)")
        wmenu.lower()

        if wmenu == "y":
            print("Sure!")
            return menu()
        elif wmenu == "n":
            print("Well, thanks for using us! Have a nice day!")
            menu_check = True
        else:
            print("Please enter valid data")

def summary():
    menu_check = False
    if not expenses:
        print("No expenses yet.")
        return menu()
    else:
        print("""-----Summary of your expenses amount-----
            """)
        amounts = [item["amount"] for item in expenses]

        total = sum(amounts)
        avg = total / len(amounts)
        minimum = min(amounts)
        maximum = max(amounts)

        print(f"""
                Total: {total} $
                Average: {avg} $
                Min: {minimum} $
                Max: {maximum} $
                """)


    while menu_check == False:
        wmenu = input("Would like to get back to menu ? (y/n)")
        wmenu.lower()

        if wmenu == "y":
            print("Sure!")
            return menu()
        elif wmenu == "n":
            print("Well, thanks for using us! Have a nice day!")
            menu_check = True
        else:
            print("Please enter valid data")

def category_summary():
    menu_check = False
    print("""-----Summary of your expenses amount-----
        """)
    if not expenses:
        print("No expenses to categorize.")
    else:
        category_totals = {}

        for item in expenses:
            cat = item["category"]
            amt = item["amount"]

            if cat in category_totals:
                category_totals[cat] += amt
            else:
                category_totals[cat] = amt

        for cat, total in category_totals.items():
            print(f"{cat}: {total} $")

    while menu_check == False:
        wmenu = input("Would like to get back to menu ? (y/n)")
        wmenu.lower()

        if wmenu == "y":
            print("Sure!")
            return menu()
        elif wmenu == "n":
            print("Well, thanks for using us! Have a nice day!")
            menu_check = True
        else:
            print("Please enter valid data")


if __name__ == "__main__":
    main()