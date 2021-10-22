# Simple pattern.
n = int(input("Enter the step size: "))
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()