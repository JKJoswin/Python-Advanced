def palindrome(n):
    temp=n
    rev=0
    while temp>0:
        rem=temp%10
        rev=rev*10+rem
        temp//=10
    if n==rev:
        print(n," is a palindrome.")
    else:
        print(n," is not a palindrome.")

num=int(input("Enter The Number: "))
palindrome(num)