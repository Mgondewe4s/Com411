def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left","Turn Right"]
    return directions

def menu():
    print("Please select a direction:")

    Path = directions()

    for direction in Path:
        print(f"{index}:{direction}")

def run():
    menu()


run()
