def powset(size,set):
    subsetsize=1<<size
    subset=[]
    for i in range(subsetsize):
        list1=[]
        for j in range(3):
            if(i & (1<<j) > 0):
                list1.append(set[j])
        subset.append(list1)
    print("Subset is equal to ",subset)

n=int(input("Enter the Size: "))
set1=[]
for i in range(0,n):
    l1=int(input("Enter the Element: "))
    set1.append(l1)
powset(n,set1)