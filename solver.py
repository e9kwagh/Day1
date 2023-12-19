"""Write a function in python that returns the sum of all 
the multiples of a list of factors where the multiples are between the start and end, inclusive"""

def solver(factors, start, end):
    """This is the solver funtions"""
    li = []
    for i in factors:
        for j in range(start, end + 1):
            if j % i == 0:
                if j not in li:
                    li.append(j)
    add = sum(li)
    return add


if __name__ == "__main__":
    print(solver([4, 7, 11], 8912, 40512))
