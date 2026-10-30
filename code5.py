balance = float(input("Enter opening balance (Rs.): "))
transactions = []

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            transactions.append(("Deposit", amount))
            print("Deposit successful.")
        else:
            print("Amount must be positive.")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Amount must be positive.")
        elif amount > balance:
            print("Rejected: insufficient balance.")
        else:
            balance -= amount
            transactions.append(("Withdrawal", amount))
            print("Withdrawal successful.")

    elif choice == "3":
        print("Current balance: Rs.", round(balance, 2))

    elif choice == "4":
        break

    else:
        print("Invalid option.")

print("\n--- Transaction Summary ---")

for transaction_type, amount in transactions:
    print(transaction_type, ": Rs.", round(amount, 2))

print("Closing balance: Rs.", round(balance, 2))