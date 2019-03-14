for i in range(1000,3001):
    count=0
    num=str(i)
    l=[]
    for a in num:
        a=int(a)
        if(a%2==0):
            count+=1
    if(count==4):
        print(i)
