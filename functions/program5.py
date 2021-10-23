# Program to print n copies of a given string.
def n_copies(s, n):
    return (s + " ") * n

s = input("Enter string: ") 
n = int(input("Enter number of times to repeat the string: "))
print(n_copies(s, n))   