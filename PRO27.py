##Using range() function: Print the multiplication table of a number n.

n = int(input("Enter a number: "))
for i in range(1,11):
    print(n,"X",i,"=",n*i)