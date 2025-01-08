l=int(input("Enter The Larger Number: "))
s=int(input("Enter The Smaller Number: "))
while s:
    t=s
    s=l%s
    l=t
print(l)