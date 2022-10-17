print("What is your name?")
name = input()
print("Hello", name)

print("How old are you (in years)?")
Years = input()
print("So", name, "you are", Years,"?")
input()

print("How tall are you (in meters)", name)
Height = float(input())
print("So", name, "you are", Years, "and are", Height, "meters tall")
input()

print("How much do you weigh (in kilograms)?")
Weight = int(input())
print("So", name, "you are", Years,",", Height, "meters tall and you weigh", Weight,"kilograms")
input()
Bmi = Weight/Height**2
print("Your bmi is",Bmi)



