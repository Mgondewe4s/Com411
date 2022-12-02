import csv


def display_review(review, cols=None):
    print("Extracting...", end="")
    with open(review) as file:
        csv_reader = csv.reader(file)
        for values in csv_reader:
            print(values[0,3,5])


def run():
    display_review("test.csv")


if __name__ == "__main__":
    run()
