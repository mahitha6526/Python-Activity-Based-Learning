products = []
quantities = []
prices = []

n = int(input("Enter number of products: "))

if n <= 0:
    print("Number of products must be positive.")
else:
    for i in range(n):
        print("\nProduct", i + 1)

        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item (Rs.): "))

        while quantity < 0 or price < 0:
            print("Quantity and price cannot be negative. Re-enter details.")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item (Rs.): "))

        products.append(name)
        quantities.append(quantity)
        prices.append(price)

    subtotal = 0
    print("\n--- Itemized Invoice ---")

    for i in range(n):
        amount = quantities[i] * prices[i]
        subtotal += amount

        print(products[i], "x", quantities[i], "=", "Rs.", round(amount, 2))

    discount = subtotal * 0.10 if subtotal >= 2000 else 0
    taxable_amount = subtotal - discount
    tax = taxable_amount * 0.05
    total = taxable_amount + tax

    print("Subtotal: Rs.", round(subtotal, 2))
    print("Discount: Rs.", round(discount, 2))
    print("Tax (5%): Rs.", round(tax, 2))
    print("Final total: Rs.", round(total, 2))