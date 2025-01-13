def oddoreven(n):
    if(n^1==n+1):
        return True
    else:
        return False

num=int(input("Enter The Number: "))

if oddoreven(num):
    print(num," is an even number.")
else:
    print(num," is an odd number.")