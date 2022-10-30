def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left","Turn Right"]
    return directions

def menu():
    print("Please select a direction:")
    path = directions()

    for index in range(len(path)):
        direction = path[index]
        print(f"{index} :{direction}")

def run():
    menu()


run()
