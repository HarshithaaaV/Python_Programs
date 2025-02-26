# #WAP to find factorial of first n numbers.(using for loop).

# n = int(input("Enter the number: "))
# fact = 1
# i = 1
# while i <= n:
#     fact *= 1
#     i += 1
# print("Factorial of", n, "is", fact)

n = int(input("Enter the number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial of", n, "is", fact)