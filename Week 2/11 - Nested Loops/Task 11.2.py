print("Please enter a sequence of characters consisting of dashes and two markers e.g. 'X----X'.")
Sequence = input()
print("\n")

print("Please enter the character for the marker")
Marker =  input()
print("\n")

is_counting = False
count = 0

for character in Sequence:
    if (is_counting == False) and (character == Marker):
      print("Found first marker")
      is_counting = True
    elif (is_counting == True) and (character == Marker):
      print("Found last marker")
    elif is_counting:
      count += 1

# Display result
print(f"The distance between the markers is {count}")


