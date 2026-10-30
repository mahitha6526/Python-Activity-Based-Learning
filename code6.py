products = ["Notebook", "Pen", "File"]
opening_stock = [100, 200, 50]
received = [30, 50, 20]
dispatched = [40, 80, 10]
recorded_closing = [90, 165, 60]

print("--- Inventory Reconciliation ---")

for i in range(len(products)):
    expected = opening_stock[i] + received[i] - dispatched[i]
    difference = recorded_closing[i] - expected

    print("\nProduct:", products[i])
    print("Expected closing stock:", expected)
    print("Recorded closing stock:", recorded_closing[i])

    if difference == 0:
        print("Status: Stock matches")
    elif difference > 0:
        print("Status: Surplus of", difference)
    else:
        print("Status: Shortage of", abs(difference))