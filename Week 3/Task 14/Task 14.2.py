def sum_weight(Beep, Bop):
    Total = Beep + Bop
    return Total

def calc_avg_weight(Beep, Bop):
    sum = sum_weight(Beep,Bop)/2
    return sum

def run():
    print("What is the weight of beep?")
    Beep = int(input())
    print("\n")

    print("What is the weight of Bop?")
    Bop = int(input())
    print("\n")

    print("what would you like to calculate(sum or average)?")
    Calc = input()
    print("\n")

    if Calc == "sum":
        answer = sum_weight(Beep, Bop)
        print(f"The sum of Beep's and Bop's weight is {answer:.2f}")
    elif Calc == "average":
        answer = calc_avg_weight(Beep, Bop)
        print(f"The average of Beep's and Bop's weight is {answer:.2f}")
    else:
        print("I am not sure what you would like to do.")


# call to function
run()

