#Ask user what to do
print("Which cover would you like for your boook, (hard/soft)")
cover = input()

#Depending on what user chose

if cover == "soft":
    print("Is the book, perfect bound?")
    perfect = input()

    if perfect == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")

if cover == "hard":
    print("Books with hard covers can be more expensive!")