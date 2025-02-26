# #WAP to find sum of first n numbers.(using while loop)

# n = int(input("Enter the number: "))
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("Sum of", n, "is", sum)

n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(sum)