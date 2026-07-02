import math

print("=" * 50)
print("        SIP CALCULATOR")
print("=" * 50)

monthly_investment = float(input("Enter Monthly Investment (₹): "))
annual_return = float(input("Enter Expected Annual Return (%): "))
years = int(input("Enter Investment Duration (Years): "))

monthly_rate = annual_return / 12 / 100
months = years * 12

future_value = monthly_investment * (
    ((1 + monthly_rate) ** months - 1) / monthly_rate
) * (1 + monthly_rate)

total_investment = monthly_investment * months
estimated_return = future_value - total_investment

print("\n" + "=" * 50)
print("           SIP SUMMARY")
print("=" * 50)
print(f"Monthly Investment : ₹{monthly_investment:,.2f}")
print(f"Investment Period  : {years} Years")
print(f"Expected Return    : {annual_return:.2f}%")
print("-" * 50)
print(f"Total Investment   : ₹{total_investment:,.2f}")
print(f"Estimated Returns  : ₹{estimated_return:,.2f}")
print(f"Maturity Amount    : ₹{future_value:,.2f}")
print("=" * 50)