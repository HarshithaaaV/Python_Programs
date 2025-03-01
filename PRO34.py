#WAF to check whether if a number is an even or odd.

def even_or_odd(n):
    if (n%2==0):
        print("EVEN")
    else:
        print("ODD")
n=int(input("Enter a number: "))
even_or_odd(n)