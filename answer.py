def answer() :
    li= []
    for i in range(1000):
        if i%3 ==  0 : 
            li.append(i)
        elif i%5 == 0 :
            li.append(i)

        
    add = sum(li)
    return add


solve()

#methode 2 optimise : 

def answer() :
    a = 1000//3
    b = 1000//5
    li= []
    for i in range(a+1) :
        add_three =  i*3
        li.append(add_three) 
    for i in range(b+1) :
        add_five = i*5
        if add_five not in li :
            li.append(add_five)
    add =  sum(li)

    print("add = ", add)



test_solver()


