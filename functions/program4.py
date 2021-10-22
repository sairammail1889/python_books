# Program to add 'Is' at the beginning of a string.
# If 'Is' already at the beginning then don't change anything.

def new_string(s):
    if len(s) >= 2 and s[:2] != 'Is':
        return 'Is ' + s
    return s 

s = input("Enter a string: ")
print(f"new_string: {new_string(s)}")