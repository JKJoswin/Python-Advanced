# Program to show the linear time complexity

def linear(n):
    it=0
    for i in range(0,n):
        it=it+1
    
    print("Iterations=",it)

linear(10)
linear(20)
linear(30)