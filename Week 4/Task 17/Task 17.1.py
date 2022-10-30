

def getcwd():
    import os
    path = os.getcwd()
    print(f"Current Working Directory: {path}")

    for file in os.listdir(path):
        print(f"The directory contains the following files: {file}")


def run():
    print("Processing...")
    getcwd()

run()