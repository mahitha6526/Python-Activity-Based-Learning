units = int(input("Enter electricity units consumed: "))
fixed_charge = 50

if units < 0:
    print("Units cannot be negative.")
elif units <= 100:
    energy_charge = units * 1.50
elif units <= 200:
    energy_charge = 100 * 1.50 + (units - 100) * 2.50
elif units <= 300:
    energy_charge = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
else:
    energy_charge = 100 * 1.50 + 100 * 2.50 + 100 * 4.00 + (units - 300) * 6.00

if units >= 0:
    total_bill = energy_charge + fixed_charge
    print("Units:", units)
    print("Energy charge: Rs.", round(energy_charge, 2))
    print("Fixed charge: Rs.", fixed_charge)
    print("Total bill: Rs.", round(total_bill, 2))