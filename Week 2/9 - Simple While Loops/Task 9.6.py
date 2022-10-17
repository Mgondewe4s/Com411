print("How many numbers should I sum up?")
Sum = int(input())

Summed = 0

print()

total =  0

while Sum > Summed:
     print(f"Please enter number of {Summed} of {Sum}:")
     num = int(input())

     total = total + num

     Summed = Summed + 1

     print (f"The answer is {total}.")