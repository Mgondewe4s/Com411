def observed():
      observations = []

      for count in range(5):
        print("Please enter an observation:")
        observations.append(input())

      return observations

def remove_observations(observations):
    is_running = True

    while(is_running):
        print("Do you wish to remove any observations previously listed? (yes/no)")
        answer = input()

        if answer == "yes":
            print("name the observations you wish to remove")
            name = input()
            observations.remove(name)
            print("done!")
        else:
           is_running = False


def run():
    observations = observed()
    remove_observations(observations)


  # populate set
    observations_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        observations_set.add(data)

    # display set
    for data in sorted(observations_set):
        print(f"{data[0]} observed {data[1]} times.")

run()





