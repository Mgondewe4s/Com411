#Ask user where to search
print("Where should i look?")
Search = input()

#User wants to check bedroom
if Search == "in the bedroom":
    print("Where in the bedroom should i look?")
    bedroom = input()

    if bedroom == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery")

#User wants to check bathroom

if Search == "in the bathroom":
    print("Where in the bathroom should i look?")
    bathroom = input()

    if bathroom == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery")

#User wants to check the lab

if Search == "in the lab":
    print("Where in the lab should i look?")
    lab = input()

    if lab == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery")

else:
    print("I do not know where that is buy i will keep looking.")