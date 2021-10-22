# Find the factorial of a given number.
a = int(input("Enter a number: "))
fact = 1
for i in range(2, a + 1):
    fact *= i
print(f"{a}! = {fact}")    