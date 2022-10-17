print("How many bars should be charged?")
Bars = int(input())

bar = 0

print()

while bar < Bars:
    print("Charging:", end="")
    bar = bar + 1

    Heart = (bar) * ('(\u03C0)')
    print(Heart)

print("The battery is fully charged")

