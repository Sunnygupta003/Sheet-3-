# n=int(input("enter a number"))
# m=int(input("enter a number"))
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()




n = int(input("Enter number of rows: "))

for i in range(n):
    # loop for spaces
    for j in range(1,n):
        print("_ ", end="")
    # loop for stars
    for k in range(i+1):
        print("*", end=" ")
    print()








