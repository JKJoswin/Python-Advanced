
def BtoD(bn):
    i=0
    temp=bn
    res=0
    while temp>0:
        rem=temp%10
        res=res+rem*2**i
        i+=1
        temp//=10
    return res

num=int(input("Enter a binary number: "))
dec=BtoD(num)
print("The decimal equivalent of the binary number ",num," is ",dec,".")