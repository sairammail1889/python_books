# Print the sum of given number list.
lst = input("Enter a list: ")
lst = map(int, lst.split())
lst = list(lst)
print(type(lst))
total = 0
for item in lst:
    total += item
print(f"The sum is {total}")