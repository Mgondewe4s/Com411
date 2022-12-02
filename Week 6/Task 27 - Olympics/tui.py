def started(msg=""):
    dashes = "-" * 85
    print(dashes)
    print(f"Operation started:{msg}...\n")

def completed():
    print("\nOperation completed.")
    dashes = "-" * 85
    print(dashes)

def error(msg):
    print(f"Error!{msg}")


def menu():
    print("\nPlease select onw of the following options:")
    print("\n    [years]  List unique years\n    [tally]  Tally up medasls\n    [team]   Tally up medals for each team\n    [exit]   Exit the program")
    print("\nYour selection: ", end="")
    selection = input()

def display_medal_tally(tally):
    print("\n| Gold    | 13372  |\n| Silver  | 13116  |\n| Bronze  | 13295  |")

def display_medal_tally(team_tally):
    print(f"{team}\n  {medals}")

def display_years(years):
    for time in years:
        print(years)


def run():
    started(msg="Reading data from athlete_events.csv")
    completed()
    error(msg="Invalid selection")
    menu()
    display_medal_tally()

run()