import math
l=int(input("Enter The Lower Range: "))
u=int(input("Enter The Upper Range: "))

for i in range(l,u+1):
    if i>1:
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                break
        else:
            print(i)