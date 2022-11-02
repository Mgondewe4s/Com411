def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction")
    path = directions()

    for index in range(len(path)):
        direction = path[index]
        print(f"{index} :{direction}")
    answer = int(input())
    return direction



def run():
    route = []
    print("Working out escape route...")

    for i in range(5):
        route.append(menu())
        print(f"Escape route: {route}")



run()


