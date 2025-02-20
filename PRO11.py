#WAP to check if a list contains a palindrome of elements.

pal = [1,2,3,2]
pal.reverse()
pal1 = pal.copy()
if pal1 == pal:
    print("Yes, the list contains a palindrome of elements.")
else:   
    print("No, the list does not contain a palindrome of elements.")