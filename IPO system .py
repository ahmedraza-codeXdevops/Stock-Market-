import random

ipo = {
    "company": "ABC Technologies Ltd",
    "price": 520,
    "lot_size": 25,
    "available_lots": 20
}

applications = []

while True:

    print("\n" + "=" * 50)
    print("        IPO ALLOTMENT SYSTEM")
    print("=" * 50)

    print("1. IPO Details")
    print("2. Apply for IPO")
    print("3. View Applications")
    print("4. Run Allotment")
    print("5. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        print("\nCompany :", ipo["company"])
        print("Issue Price : ₹", ipo["price"])
        print("Lot Size :", ipo["lot_size"], "Shares")
        print("Available Lots :", ipo["available_lots"])

    elif choice == "2":

        name = input("Investor Name : ")
        pan = input("PAN Number : ")
        lots = int(input("Number of Lots : "))

        amount = lots * ipo["lot_size"] * ipo["price"]

        applications.append({
            "name": name,
            "pan": pan,
            "lots": lots,
            "amount": amount,
            "status": "Pending"
        })

        print("\nApplication Submitted Successfully.")

    elif choice == "3":

        if len(applications) == 0:
            print("\nNo Applications Found.")

        else:

            print("\nAPPLICATIONS\n")

            for app in applications:

                print("-------------------------------")
                print("Name :", app["name"])
                print("PAN :", app["pan"])
                print("Lots :", app["lots"])
                print("Amount : ₹", app["amount"])
                print("Status :", app["status"])

    elif choice == "4":

        if len(applications) == 0:

            print("No Applications.")

        else:

            winners = random.sample(
                applications,
                min(ipo["available_lots"], len(applications))
            )

            for app in applications:

                if app in winners:
                    app["status"] = "ALLOTTED"
                else:
                    app["status"] = "NOT ALLOTTED"

            print("\nAllotment Completed.\n")

            for app in applications:

                print(app["name"], "->", app["status"])

    elif choice == "5":

        print("\nThank You")
        break

    else:
        print("Invalid Choice")