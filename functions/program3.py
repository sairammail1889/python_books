# Program to calculate the sum of three given number, if the values are equal then
# return thrice their sum.
def sum_thrice(x, y, z):
    total = x + y + z
    if x == y == z:
        total = total * 3
    return total

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
print(f"sum_thrice: {sum_thrice(x, y, z)}")