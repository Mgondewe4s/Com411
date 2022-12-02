def observed():
    observations = []
    for count in range(7):
        print("Please enter an observation: ")
        obse = input()
        observations.append(obse)

    return observations


def run():
    print("Counting observations...")
    obs = observed()

    setty = set()
    for observation in obs:
        data = (observation, obs.count(observation))
        setty.add(data)

    for data in setty:
        print(f"{data[0]} observed {data[1]} times.")


run()
