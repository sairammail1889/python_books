# Print the first n terms in a fibonacci series.
n = int(input("Enter the number of fibonacci terms to print: "))
f0, f1 = 0, 1
if n == 1:
    print(f0)
elif n == 2:
    print(f0)
    print(f1)
elif n > 2:
    print(f0)
    print(f1)
    for i in range(2, n):
        f0, f1 = f1, f0 + f1
        print(f1)