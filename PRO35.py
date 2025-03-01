#Wite a recursive function to calculate the sum of first n natural numbers.

def sum_natural(n):
    if (n==0):
        return 0
    return sum_natural(n-1)+n 
print(sum_natural(10))