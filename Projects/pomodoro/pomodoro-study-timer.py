import json
import time

with open("Settings.json", "r") as file:
    setting = json.load(file)
work_time = setting[0]["work"]
break_time = setting[0]["break"]

def main():
    work_time, break_time = data_upload()
    menu()

def data_upload():
    with open("Settings.json", "r") as file:
        setting = json.load(file)
    work_time = setting[0]["work"]
    break_time = setting[0]["break"]
    return work_time, break_time

def menu():
    print("""----------------------------------------------
    Welcome to Pomodoro Timer
    ----------------------------------------------
    """)
    menu_done = False
    while menu_done == False:
        wMenu = input("""Please choose an option (1/2/0):
                                   1) Start Pomodoro
                                   2) Settings
                                   3) Stats
                                   0) Exit
                                   > """)

        if wMenu == "1":
            menu_done = True
            pomodoro(work_time, break_time)
        elif wMenu == "0":
            menu_done = True
            print("Well, have a nice day!")
        else:
            print("Please enter valid data")


def pomodoro(work_time, break_time):
    try:
        pom_quantity = int(input("""How many pomodoro you'd like to do today ?
                           """))
        if pom_quantity <= 0:
            print("Please enter valid data")
            return pomodoro(work_time, break_time)

    except ValueError:
        print("Please enter valid data")
        return pomodoro(work_time, break_time)

    pomodoro_done = 1
    while pomodoro_done <= pom_quantity:
        print(f"""Your {pomodoro_done}. pomodoro is starting...""")
        time.sleep(2)

        for t in range(3, 0, -1):
            seconds = t % 60
            minutes = int(t / 60) % 60
            print(f"Pomodoro Starting in: {minutes:02}:{seconds:02}")
            time.sleep(1)

        print("-----Pomodoro Timer-----")
        for t in range(work_time, 0, -1):
            seconds = t % 60
            minutes = int(t / 60) % 60
            print(f"Pomodoro Timer: {minutes:02}:{seconds:02}")
            time.sleep(1)

        if pomodoro_done < pom_quantity:
            skip_done = False
            while not skip_done:
                skip = input("Would you like to make a break (y/n): ").lower().strip()
                if skip in ["y", "n"]:
                    if skip == "y":
                        print(f"\nSure, enjoy your {break_time}m break!\n")
                        break_timer(break_time)
                        print("TIMES UP!")

                        con_done = False
                        while not con_done:
                            con = input("Would like to continue ? (y/n): ").lower().strip()
                            if con in ["y", "n"]:
                                if con == "y":
                                    con_done = True
                                    skip_done = True
                                else:
                                    print("Well, have a nice day!")
                                    return back_to_menu()
                            else:
                                print("Please enter valid data")
                    else:
                        skip_done = True
                else:
                    print("Please enter valid data")

        pomodoro_done += 1

    if pomodoro_done > pom_quantity:
        print(f"""Congrats! You have been done your {pomodoro_done - 1} pomodoros!
            Good for you!
            """)
        back_to_menu()



def break_timer(break_time):
    for t in range(3, 0, -1):
        seconds = t % 60
        minutes = int(t / 60) % 60
        print(f"Break Starting in: {minutes:02}:{seconds:02}")
        time.sleep(1)
    print("-----Break Timer-----")
    for t in range(break_time, 0, -1):
        seconds = t % 60
        minutes = int(t / 60) % 60
        print(f"Break Timer: {minutes:02}:{seconds:02}")
        time.sleep(1)

def settings():
    pass


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