print("Please enter the first whole number.")
num = int(input())
remainder =  num % 2
if (remainder == 0):
    num = "odd"

print("Please enter your second whole number.")
second= int(input())
remainder =  second % 2
if (remainder == 0):
    second = "odd"
else:
    second = "even"

print("Please enter your third whole number.")
third= int(input())
remainder =  third % 2
