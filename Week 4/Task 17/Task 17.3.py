def search(file_name):
    print("Saerching... \n")

    with open(file_name) as file:
        for line in file:
            print(f"Looked in the {line.strip()} ")

        print("\n ...done")

def run():
    search("library.txt")

if __name__ == "__main__":
    run()
