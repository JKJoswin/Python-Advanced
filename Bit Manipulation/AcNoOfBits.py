def noOfBits(n):
    count=0
    while(n):
        count+=1
        n>>=1
    
    return count

num=int(input("Enter The Number: "))
print("Total no. of Bits in ",num," is ",noOfBits(num))