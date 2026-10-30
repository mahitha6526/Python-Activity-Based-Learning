basic = float(input("Enter basic salary (Rs.): "))
allowances = float(input("Enter total allowances (Rs.): "))
overtime = float(input("Enter overtime amount (Rs.): "))
incentive = float(input("Enter incentive (Rs.): "))

if min(basic, allowances, overtime, incentive) < 0:
    print("Salary components cannot be negative.")
else:
    gross_salary = basic + allowances + overtime + incentive
    deduction = gross_salary * 0.10
    net_salary = gross_salary - deduction

    print("\n--- Salary Statement ---")
    print("Gross salary: Rs.", round(gross_salary, 2))
    print("Deduction (10%): Rs.", round(deduction, 2))
    print("Net salary: Rs.", round(net_salary, 2))