# Program to check if a given number is even or odd.
def check_even(number):
    return number % 2 == 0

num = int(input("Enter a number: "))
if check_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")