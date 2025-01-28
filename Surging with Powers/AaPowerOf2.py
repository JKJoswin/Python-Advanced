def powof2(n):
    if(n & (~(n-1))== n):
        print(n," is a power of 2.")
    else:
        print(n," is not a power of 2.")

n1=int(input("Enter the number: "))
powof2(n1)