import json

def read(file_path):
    print("Reading...", end="")
    with open(file_path) as file:
        data = json.load(file)
        print("Done")
        return data

def save(file_path, saved):
    print("Exporting...", end="")
    data = {
        "name": "Beep",
        "type": "Bot"
    }
    with open(file_path, "w") as file:
        json.dump(data, file)
        print("Done!")

def run():
    json_data = read("robocity.json")
    save("exported.json", "json_data")

if __name__ == "__main__":
  run()
