def Display_in_box(word):
    message = f"* {word} *"
    print("*" * len(message))
    print(message)
    print("*" * len(message))


def Lowercase(word):
    lower = word.lower()
    print(lower)


def Uppercase(word):
    upper = word.upper()
    print(upper)


def Mirror(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print(f"{word} | {mirrored}")

def display_repeated(word):
    print("How many times would you like it repeated?")
    repeats = int(input())

    for repeat in range(repeats):
        if (repeat % 2 == 0):
            print(Lowercase(word))
        else:
            print(Uppercase(word))



def Enter_word():
    print("Please enter a word")
    word = str(input())
    print("\n")

    print("Choose between: \nDisplay in a box\nDisplay Lower-case\nDisplay Upper-case\nDisplay Mirrored\nRepeat")
    print("\n")
    Option = str(input())
    print("\n")

    if Option == "Display in a box":
        Display_in_box(word)
    elif Option == "Display Lower-case":
        Lowercase(word)
    elif Option == "Display Upper-case":
        Uppercase(word)
    elif Option == "Display Mirrored":
        print(Mirror(word))
    elif Option == "Repeat":
        display_repeated(word)


Enter_word()
