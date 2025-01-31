def flipbits(a,b):
    x = a ^ b
    count=1
    while(x & (x-1) > 0):
        count+=1
        x = x & (x-1)
    print("The number of bits to flipped is ",count)

a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
flipbits(a,b)