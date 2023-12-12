# def solver(factors, start, end):
#     li = []
#     for i in  factors :
#         for j in range(start , end) :
#             if j%i == 0 :      
#                 if j  not in li :
#                     li.append(j)
#     add = sum(li)
#     return add
    

# print(solver([4, 7, 11], 8912, 40512))

# this is the  optimise version 

# 1. Send me the answer for solver([2, 3, 5, 7, 11], 34567, 1234567)
# 2. Ensure that your program runs in < 1 minute.
# 3. Submit the updated code, if applicable, to github.
# 4. Your solution must be uniquely yours. We are running sophisticated algorithms that have identified several submissions to be meaningfully identical.




def solver(arr,start,end):
    li =[]
    for i in arr :
        val=  end//i
        for j in range(val) :
            add  = j *val
            if add not in li :
                li.append(add)
                total = sum(li)
    print(total)
    return total 

solver([2, 3, 5, 7, 11], 34567, 1234567) 


    





#     for i in range(a+1) :
#         add_three =  i*3
#         li.append(add_three) 
#     for i in range(b+1) :
#         add_five = i*5
#         if add_five not in li :
#             li.append(add_five)
#     add =  sum(li)

#     print("add = ", add)





# test_solver()

