import json

print("\n------------------------------")
print("     Welcome to Todo List     ")
print("------------------------------\n")
FILE_NAME = "TodoList.json"

def main():
    menu()

def menu():
    try:
        wMenu = int(input("Please choose an option:\n"
                          "1) Add todo\n"
                          "2) List todos\n"
                          "3) Toggle done\n"
                          "4) Delete todo\n"
                          "0) Exit\n"
                          "> "))

    except ValueError:
        print("\nPlease enter valid data.\n")
        return menu()

    if wMenu in [1, 2, 3, 4, 0]:
        match wMenu:
            case 1:
                return add_todo()
            case 2:
                return list_todo()
            case 3:
                return toggle_done()
            case 4:
                return del_todo()
            case 0:
                print("\nWell, have a nice day!\n")

    else:
        print("\nPlease enter valid data.\n")
        return menu()

def add_todo():
    print("\n--- Add Todo ---")
    title = input("Please enter your todo title:\n> ")

    if not title.strip():
        print("\nYou cannot leave blank! Please enter a valid title.")
        return add_todo()

    try:
        with open(FILE_NAME, "r") as file:
            todos = json.load(file)
    except:
        todos = []

    new_todo = {"id": max([item["id"] for item in todos], default=0) + 1, "title": title, "done": False}
    todos.append(new_todo)


    with open(FILE_NAME, "w",) as file:
        json.dump(todos, file, indent=2)

    print("\nYour todo has been successfully saved!")
    return back_to_menu()

def list_todo():
    print("\n--- List of Todos ---")
    try:
        with open(FILE_NAME, "r") as file:
            todos = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nNo todos yet.")
        return back_to_menu()

    print("")
    for item in todos:
        if item["done"] == False:
            x = "[ ]"
        else:
            x = "[x]"

        print(f"{x} {item['id']} - {item['title']}")
    print("")
    return back_to_menu()


def toggle_done():
    toggled = False

    print("\n--- Toggle Todo ---")
    try:
        with open(FILE_NAME, "r") as file:
            todos = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nNo todos yet.")
        return back_to_menu()

    print("")
    for item in todos:
        if item["done"] == False:
            x = "[ ]"
        else:
            x = "[x]"

        print(f"{x} {item['id']} - {item['title']}")
    print("")

    while toggled == False:
        try:
            choice = int(input("Please enter the id of the todo to toggle:\n> "))
        except ValueError:
            print("\nPlease enter valid data.\n")
            continue

        if choice in range(1, len(todos) + 1):
            for item in todos:
                if item["id"] == choice:
                    item["done"] = not item["done"]
                    toggled = True
                    print(f"\nYour todo with id {item['id']} successfully toggled!")

            with open(FILE_NAME, "w") as file:
                json.dump(todos, file, indent=2)

            return back_to_menu()
        else:
            print("\nPlease enter a valid id.\n")

def del_todo():
    deleted = False

    print("\n--- Delete Todo ---")
    try:
        with open(FILE_NAME, "r") as file:
            todos = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nNo todos yet.")
        return back_to_menu()

    print("")
    for item in todos:
        if item["done"] == False:
            x = "[ ]"
        else:
            x = "[x]"

        print(f"{x} {item['id']} - {item['title']}")
    print("")

    while deleted == False:
        try:
            choice = int(input("Please enter the id of the todo you would like to delete:\n> "))
        except ValueError:
            print("\nPlease enter valid data.\n")
            continue

        if choice in range(1, len(todos) + 1):
            for item in todos:
                if item["id"] == choice:
                    todos.remove(item)
                    deleted = True
                    print(f"\nYour todo with id {item['id']} successfully deleted!")

            with open(FILE_NAME, "w") as file:
                json.dump(todos, file, indent=2)

            return back_to_menu()
        else:
            print("\nPlease enter a valid id.\n")


def back_to_menu():
    menu_check = False

    while menu_check == False:
        wmenu = input("\nWould you like to get back to menu? (y/n): ")
        wmenu = wmenu.strip().lower()

        if wmenu == "y":
            print("\nSure!\n")
            return menu()
        elif wmenu == "n":
            print("\nThanks for using the Todo List! Have a nice day!\n")
            menu_check = True
        else:
            print("\nPlease enter valid data.")

if __name__ == "__main__":
    main()