n = int(input("Enter the number of rows: "))

for i in range(n):
    print("*", end=" ")
    for j in range(n - i - 1):
        print("_", end=" ")
    if i != n - 1:
        print("*", end="")
    print()
