def swap(a,b):
    print("Before Swap:- \na =",a,"\nb =",b)
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("\nAfter Swap:- \na =",a,"\nb =",b)

a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
swap(a,b)