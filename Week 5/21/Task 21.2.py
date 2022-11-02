def movement():
    path = [("Move Forward", 10,),("Move Backward", 5), ("Move Left", 3,), ("Move Right", 1)]
    return path

def run():
    print("Moving...")
    paths = movement()

    for directions,steps in paths:
        print(f"{directions} for {steps} steps")

run()
