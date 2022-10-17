print("How many live cables must i avoid?")
Avoid = int(input())

Avoided = 0

print()

while Avoided <  Avoid:
    print("Avoiding...", end="")
    Avoided = Avoided + 1

    print("...Done!", Avoided, " live cables avoided!")