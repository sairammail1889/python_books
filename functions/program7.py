# Program a function that takes two lists and returns True if they have atleast one 
# item common between them.
def check_condition(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1 = input("Enter list1 items: ").split()
list2 = input("Enter list2 items: ").split()
print(check_condition(list1, list2))