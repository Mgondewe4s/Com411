import random as rnd

print("Please enter the minimum value:")
minimum = int(input())
print("\n")

print("Please enter the maximum value:")
maximum = int(input())
print("\n")

random = rnd.randrange(minimum, maximum)

print(f"I am thinking of a number between {minimum} and {maximum}.\n Can you guess what it is?")
guess = int(input())
print("\n")

if guess == random:
    print("Congratulation! You guessed my number!")

elif guess > random:
    print("Your guess is too high")
    print("Try again:")
    guess = int(input())
elif guess < random:
    print("Your guess is too low")
    print("Try again:")
    guess = int(input())

