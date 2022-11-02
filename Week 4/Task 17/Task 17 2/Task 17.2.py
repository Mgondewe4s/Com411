def display_chars(file_path, number):
    with open(file_path) as file:
        partial_data = file.read(number)
        print("The first 5 characters are:")
        print(partial_data)
        print("\n")

def display_line(file_path):
    with open(file_path) as file:
        line = file.readline().strip()
        print("The first line is: ")
        print(line)
        print("\n")

def display_txt(file_path):
    with open(file_path) as file:
        data = file.read()
        print("The full text is: ")
        print(data)
        print("\n")

def run():
   display_chars("Library.txt", 5)
   display_line("Library.txt")
   display_txt("Library.txt")

if __name__ == "__main__":
    run()