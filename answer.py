# def answer() :
#     li= []
#     for i in range(1000):
#         if i%3 ==  0 :
#             li.append(i)
#         elif i%5 == 0 :
#             li.append(i)


#     add = sum(li)
#     return add


# methode 2 optimise :


"""Find the sum of all the multiples of 3 or 5 below 1000."""


def answer():
    """anseer fucntion"""

    li = []
    for i in range(1000):
        if i % 3 == 0:
            li.append(i)
        elif i % 5 == 0:
            if i not in li:
                li.append(i)

    add = sum(li)
    return add


if __name__ == "__main__":
    print(answer())
