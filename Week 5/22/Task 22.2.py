def min_likelihood():
    likelihood = (50, 38, 27, 99, 4)
    min_value = {min(likelihood)}
    return min_value

def max_likelihood():
    likelihood = (50, 38, 27, 99, 4)
    max_value = {max(likelihood)}
    return max_value



def run():
    maxx = max_likelihood()
    minn = min_likelihood()

    print(f"Minimum likelihood of falling: {minn}%")
    print(f"Maximum likelihood of falling: {maxx}%")

run()

