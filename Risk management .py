print("=" * 60)
print("           STOCK MARKET RISK MANAGEMENT")
print("=" * 60)

account_balance = float(input("Enter Account Balance (₹): "))
risk_percent = float(input("Enter Risk Per Trade (%): "))
entry_price = float(input("Enter Entry Price (₹): "))
stop_loss = float(input("Enter Stop Loss Price (₹): "))
target_price = float(input("Enter Target Price (₹): "))

risk_amount = account_balance * (risk_percent / 100)

risk_per_share = entry_price - stop_loss

if risk_per_share <= 0:
    print("\nInvalid Stop Loss!")
else:
    quantity = int(risk_amount // risk_per_share)

    investment = quantity * entry_price
    profit_per_share = target_price - entry_price
    expected_profit = quantity * profit_per_share

    reward_ratio = profit_per_share / risk_per_share

    print("\n" + "=" * 60)
    print("              TRADE SUMMARY")
    print("=" * 60)

    print(f"Account Balance       : ₹{account_balance:,.2f}")
    print(f"Risk Percentage       : {risk_percent}%")
    print(f"Maximum Risk Amount   : ₹{risk_amount:,.2f}")

    print("-" * 60)

    print(f"Entry Price           : ₹{entry_price}")
    print(f"Stop Loss             : ₹{stop_loss}")
    print(f"Target Price          : ₹{target_price}")

    print("-" * 60)

    print(f"Risk Per Share        : ₹{risk_per_share:.2f}")
    print(f"Quantity to Buy       : {quantity}")
    print(f"Investment Required   : ₹{investment:,.2f}")
    print(f"Expected Profit       : ₹{expected_profit:,.2f}")
    print(f"Risk : Reward Ratio   = 1 : {reward_ratio:.2f}")

    print("=" * 60)

    if reward_ratio >= 2:
        print("Good Trade 👍")
    else:
        print("Risk is high. Consider skipping this trade.")