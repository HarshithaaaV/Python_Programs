""" Search for a number x in this tuple using loop:
[1,4,9,16,25,36,49,64,81,100] """

tup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter a number to search: "))
for i in tup:
    if i == x:
        print("Number found at index", tup.index(i))
        break
else:
    print("Number not found")