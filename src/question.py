hours = int(input("ENter the number of hours:"))
if hours <=2:
    parking_charge = hours * 30
elif hours <=5:
    parking_charge = hours * 25
elif hours >5:
    parking_charge = hours * 20
    if parking_charge >= 150:
        service_charge = 20
final_amount = parking_charge + service_charge
print(f"Parking Charge: {parking_charge}INR")
print(f"Service Charge: {service_charge}INR")
print(f"Final Amount: {final_amount}INR")
