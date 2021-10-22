# Find the gcd of two numbers.
a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))
gcd = 1
for i in  range(2, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
print(f"GCD of {a} and {b} is {gcd}")        