""" Search for a number x in this tuple using loop:
[1,4,9,16,25,36,49,64,81,100] """

tup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter a number to search: "))
i=0
while i < len(tup):
    if x == tup[i]:
        print("Number found at index", i)
        break
    i += 1
else:
    print(" Number not found")