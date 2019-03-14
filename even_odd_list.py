list1=[]
list2=[]
def sequence(n):
    while n != 1:
        if n%2 == 0:# n is even
            list1.append(n)
            n-=1
        else: # n is odd
            list2.append(n)
            n-=1
    return(list1,list2)
print("even and odd numbers from {} to n are".format(2),sequence(100))
