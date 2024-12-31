n=int(input("Enter the number: "))
temp=n
res=0
while temp>0:
    rem=temp%10
    res=res + rem**3
    temp//=10

if res==n:
    print(n," is an Arm Strong Number!")
else:
    print(n," is not an Arm Strong Number!")