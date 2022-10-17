print("What phrase do you see?")
Phrase = input()
print("\n")

print("Reversing...")
print("\n")

print("The phrase is: ", end="")

for i in reversed(range(len(Phrase))):
    print(Phrase[i], end="")


