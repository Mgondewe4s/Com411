print("Please enter a number:")
num = int(input())

total =  1

for i in range(num):
    total = total * (i + 1)

print(f"The factorial is {total}")