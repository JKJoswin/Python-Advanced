def ooo(arr):
    res=0
    for i in arr:
        res=res^i
    
    print("One Odd Occuring number is ",res)

arr1=[]
for i in range(5):
    num=int(input("Enter a Number: "))
    arr1.append(num)

ooo(arr1)