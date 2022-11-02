import json

def read(file_path):
    with open(file_path) as file:
        data = json.load(file)
        #variables from json file
        city_name = data["city"]
        population = data["population"]
        print(f"City name: {city_name}")
        print(f"Population: {population}")

        bots = data["bots"]

    for bot in bots:
        name = bot["name"]
        stats = bot["stats"]

        print(f"{name} has the following stats: {stats}")

def run():
    read("robocity.json")

if __name__ == "__main__":
        run()
