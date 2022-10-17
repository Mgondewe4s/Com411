print("Please enter a sequence of characters consisting of dashes and two markers e.g. 'X----X'.")
Sequence = input()
print("\n")

print("Please enter the character for the marker")
Marker =  input()
print("\n")

is_counting = False
count = 0

for character in sequence:
    if (is_counting == False) and (character == marker):
      print("Found first marker")
      is_counting = True
    elif (is_counting == True) and (character == marker):
      print("Found last marker")
    elif is_counting:
      count += 1

# Display result
print(f"The distance between the markers is {count}")


