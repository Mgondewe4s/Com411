print("What level of brightness is required?")
Level =  int(input())
print("\n")

print("Adjusting brightness...")
print("\n")

for i in range(2, Level, 2):
    Heart = (i) * ("*")
    print(f"Beep's brightness level: {Heart} \n Bop's brightness level: {Heart} \n" )


print("Adjusment complete")