def likelihood():
    likelihood = (50, 38, 27, 99, 4)
    value = {min(likelihood)}
    return value

def run():
     sum = likelihood()
     print(f"Minimum likelihood of falling:{sum}%")

run()