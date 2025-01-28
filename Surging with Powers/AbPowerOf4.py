def powof4(number):
    count=0
    n=number
    if(number & ~(number & (number-1))):
        print(number & (~(number & (number-1))))
        while((number & (~(number & (number-1))))>1):
            number>>=1
            count+=1
        
        if(count==0):
            return False
        
        if(count % 2 == 0):
            return True
        else:
            return False
        

num=int(input("Enter the number: "))
res=powof4(num)
if(res):
    print(num," is a power of 4.")
else:
    print(num," is not a power of 4.")