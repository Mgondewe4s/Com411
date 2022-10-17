print("What phrase do you see?")
Phrase = input()
print("\n")

print("Reversing...")
print("\n")

print("The phrase is: ", end="")

reversed=""

for i in Phrase:
    reversed = i + reversed

print(reversed)

