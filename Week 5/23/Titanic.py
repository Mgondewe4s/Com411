import csv

records = []
headings = []

def load_data(file_path):
    print("Loading data...", end="")

    with open("titanuic.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)
        for values in csv_reader:
            records.append(values)
    print("Done!")

def display_menu():
    print(" Please select one of the following options:\n[1] Display the names of all passengers\n[2] Display the number of passengers that survived\n[3] Display the number of passengers per gender\n[4] Display the number of passengers per age group\n[5] Display the number of survivors per age group")
    option = int(input())
    return option


def display_passenger_names():
    print("The names of the passengers...")
    print("\n")

    for record in records:
        passenger_name = record[3]
        print(passenger_name)

def display_num_survivors():

    num_survived = 0
    for record in records:
        survival_status = int(record[1])

        if survival_status == 1:
            num_survived += 1

    print(f"{num_survived} passengers survived")

def display_passengers_per_gender():
    females = 0
    males = 0

    for record in records:
        gender = record[4]

        if gender == "male":
            males += 1
        elif gender == "female":
            females += 1

    print(f"females: {females}, males: {males}")

def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0

    for record in records:
        if record[5] != "":
            age = float(record[5])

        if age < 18:
            children += 1
        elif age < 65:
            adults += 1
        else:
            elderly += 1

    print(f"children: {children}, adults: {adults}, elderly: {elderly}")

def display_survivors_per_age_group():
    child_sur = 0
    adults_sur = 0
    elderly_sur = 0
    for record in records:
        if record[5] != "":
            age = float(record[5])
        survival_status = int(record[1])

        if age < 18:
            if survival_status == 1:
                child_sur += 1
        elif age < 65:
            if survival_status == 1:
                adults_sur += 1
        else:
            if survival_status == 1:
                elderly_sur += 1



    children = 0
    adults = 0
    elderly = 0

    for record in records:
        if record[5] != "":
            age = float(record[5])

        if age < 18:
            children += 1
        elif age < 65:
            adults += 1
        else:
            elderly += 1

    print(f"Children {child_sur}/{children}, adults: {adults_sur}/{adults}, elderly: {elderly_sur}/{elderly}")


def run():
    load_data("titanuic.csv")
    num_records = len(records)
    print(f"Sucessfuly loaded {num_records} records .")
    print("\n") 
    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")

    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option == 3:
        display_passengers_per_gender()
    elif selected_option == 4:
        display_passengers_per_age_group()
    elif selected_option == 5:
        display_survivors_per_age_group()
    else:
        print("Error! Option not recognised")




run()



