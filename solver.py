def solver(factors, start, end):
    li = []
    for i in  factors :
        for j in range(start , end) :
            if j%i == 0 :      
                if j  not in li :
                    li.append(j)
    add = sum(li)
    return add
    

print(solver([4, 7, 11], 8912, 40512))


