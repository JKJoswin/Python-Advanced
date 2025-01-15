num=int(input("Enter The Number: "))
ones=0
zeros=0

while(num):
    if(num&1==1):
        ones+=1
    else:
        zeros+=1
    
    num>>=1

print("The No. of Ones are ",ones," and the No. of Zeros are ",zeros,".")