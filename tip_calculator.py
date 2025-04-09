print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))

tip_desired = float(
    input("How much tip would you like to give? 10, 12 or 15? "))

people = float(input("How many people to split the bill? "))

bill_w_tip = total_bill + (total_bill * (tip_desired / 100))

# Final calculations
print(f"Total bill with the tip desired: {bill_w_tip:.2f}")
print(f"Each person should pay: ${(bill_w_tip / people):.2f}")
