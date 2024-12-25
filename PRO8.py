#WAP to find the greatest of 3 numbers entered by the user.

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))
if (num1>=num2 and num1>=num3):
    print("number1 is greatest.")
elif (num2>=num1 and num2>=num3):
    print("number2 is greatest.")
else:
    print("number3 is greatest.")