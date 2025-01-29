def divide1(dividend,divisor):
    sign=0
    q=0
    t=0
    
    if(dividend < 0) ^ (divisor < 0):
        sign=-1
    else:
        sign=1
    
    dividend=abs(dividend)
    divisor=abs(divisor)
    
    for i in range(31,-1,-1):
        print("i=",i)
        if(t + (divisor<<i) <= dividend):
            t+=divisor<<i
            q+=1<<i
            print("t =",t)
            print("q =",q)
    
    if(sign == -1):
        q = -1 * q
    print("The Quotient of ",dividend," divided by ",divisor," is ",q)
    return q

dd=int(input("Enter the Dividend: "))
ds=int(input("Enter the Divisor: "))
divide1(dd,ds)