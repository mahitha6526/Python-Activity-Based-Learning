distance = float(input("Enter journey distance in km: "))
print("1. Sleeper (Rs. 1.20/km)")
print("2. AC (Rs. 2.50/km)")
choice = int(input("Choose class (1 or 2): "))
age = int(input("Enter passenger age: "))
reservation_fee = 40

if distance < 0 or age < 0:
    print("Distance and age cannot be negative.")
elif choice not in (1, 2):
    print("Invalid class choice.")
else:
    if choice == 1:
        rate, class_name = 1.20, "Sleeper"
    else:
        rate, class_name = 2.50, "AC"

    base_fare = distance * rate

    if age < 5:
        concession = base_fare
    elif age >= 60:
        concession = base_fare * 0.20
    else:
        concession = 0

    total_fare = base_fare - concession + reservation_fee

    print("Class:", class_name)
    print("Base fare: Rs.", round(base_fare, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Reservation fee: Rs.", reservation_fee)
    print("Total fare: Rs.", round(total_fare, 2))