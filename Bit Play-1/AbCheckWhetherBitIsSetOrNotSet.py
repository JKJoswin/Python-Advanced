def setornot(number,bn):
    if number&(1<<(bn-1)):
        print("In the number ",number,", bit number ",bn,"is set.")
    else:
        print("In the number ",number,", bit number ",bn,"is not set.")

num=int(input("Enter The Number: "))
bnum=int(input("Enter The Bit Number: "))
setornot(num,bnum)