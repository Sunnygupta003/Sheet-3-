n=int(input("enter a number"))
for i in range(n,0,-1):
    for j in range(i):
        if (j==1)or (j==n):
            print("*", end=" ")
        else:
            print("_" , end=" ")
    print()