def sqtime(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end=" ")
            iteration+=1
        print()
    print("Number of iterations is ",iteration,".")

sqtime(5)
sqtime(4)
sqtime(3)
sqtime(2)
sqtime(1)
print("With every n, the time is equal to n square -- O(n^2).")