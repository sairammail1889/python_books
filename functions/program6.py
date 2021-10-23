# Program a function to return True if two given numbers are equal to each other
# or their sum and difference is equal to 5.
def test_number(n1, n2):
    if n1 == n2:
        return True
    elif abs(n1 - n2) == 5:
        return True
    elif (n1 + n2) == 5:
        return True
    return False

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(test_number(a, b))