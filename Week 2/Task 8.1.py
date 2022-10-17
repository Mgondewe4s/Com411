#Retrieve answer from user
print("What type of adventure would you like?")
adventure = input()

#Path for chosen answer
if (adventure == "scary") or (adventure=="short"):
    print("Entering the dark forest!")

    if (adventure == "safe") or (adventure == "long"):
        print("Taking the safe route")

else:
    print("Not sure which route to take")
