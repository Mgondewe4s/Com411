print("How many rows should i have?")
Rows = int(input())
print("\n")

print("How many columns should i have?")
columns = int(input())
print("\n")

print("Here i go:")
print("\n")

Emoji = ":)"

for row in range(0, Rows, 1):
    for column in range(0,columns, 1):
        print(f"{Emoji}", end="")
    print()