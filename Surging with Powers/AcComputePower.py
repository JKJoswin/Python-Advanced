def compow(x,y):
    res=1
    x1=x
    y1=y
    while(y>0):
        if(y&1):
            res = res * x
        x = x * x
        y>>=1
    print(x1," to the power ",y1," is equal to ",res)

num1=int(input("Enter the number: "))
pow1=int(input("Enter the power: "))
compow(num1,pow1)