#WAF to find the factorial of n.(n is the parameter).

def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
    return 
n = int(input("Enter the number: "))
fact(n)