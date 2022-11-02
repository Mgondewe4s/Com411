import csv

def export(file_path, interger):
    print("Exporting..")
    with open(file_path, "a") as file:
        print("Please enter the id of your chosen bot:")
        bot_id = int(input())
        print("\n")

        print("Please enter the name of your chosen bot:")
        bot_name = input()
        print("\n")

        print("Please enter the paint of your chosen bot:")
        bot_paint = input()
        print("\n")

        file.write(f"\n {bot_id},{bot_name},{bot_paint}")

        print("Done!")

def run():
    export("exported_bots.csv",0)

run()




