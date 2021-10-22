# Count the number of vowels in a given string.
s = input("Enter string: ")
num_vowels = 0
for ch in s.lower():
    if ch in 'aeiou':
        num_vowels += 1
print(f"Then number of vowels in {s} is {num_vowels}")