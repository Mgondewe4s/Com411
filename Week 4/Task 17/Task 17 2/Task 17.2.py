def display_chars(file_path, number):
    with open("Library.txt") as file:
        partial_data = file.read(10)