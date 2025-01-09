import math
u=3000

for i in range(11,u+1):
    if i>1:
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                break
        else:
            temp=i
            rev=0
            while temp>0:
                rem=temp%10
                rev=rev*10+rem
                temp//=10
            if rev==i:
                print(i)