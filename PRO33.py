#WAF to convert USD to INR.

def usd_to_inr(usd):
    inr = usd * 83.5
    print("The amount in INR is: ", inr)
usd = float(input("Enter the amount in USD: "))
usd_to_inr(usd)