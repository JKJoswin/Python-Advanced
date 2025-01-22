def too(n,s):
    x=0
    y=0
    xor=n[0]
    setbit=0
    for i in range(1,s):
        xor=xor ^ n[i]
    print(xor)
    setbit=xor & ~(xor-1)
    for i in range(0,s):
        if(setbit & n[i]):
            x=x ^ n[i]
        else:
            y=y ^ n[i]
    
    print("The Two Odd Occuring Numbers are ",x," and ",y,".")

arr1=[]
for i in range(6):
    num=int(input("Enter a Number: "))
    arr1.append(num)

too(arr1,6)