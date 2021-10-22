# Program to find if a number is 100 within 1000 or 2000.
def near_thousand(number):
    if abs(1000 - number) <= 100:
        th = True
    else:
        th = False
    if abs(2000 - number) <= 100:
        twoth = True
    else:
        twoth = False
    return th, twoth

num = int(input("Enter a number: "))
k, m = near_thousand(num)
if k:
    print(f"{num} is with 100 of 1000.")
elif m:
    print(f"{num} is with 100 of 2000.")
else:
    print(f"{num} is not within 100 of 1000 or 2000.")