customer_name = input("Enter the name:")
age = int(input("Enter the age:"))
number_of_tickets = int(input("Enter the number of tickets:"))
if age < 12:
    ticket_price = 120
elif age >= 12 and age <=59:
    ticket_price = 200
elif age >=60:
    ticket_price = 150
total_before_discount = ticket_price * number_of_tickets
if number_of_tickets >= 5:
    total_amount = total_before_discount * 0.10
else:
    total_amount = 0.0
final_amount = total_before_discount - total_amount
print(f"Customer Name: {customer_name}")
print(f"Ticket Price: {ticket_price}")
print(f"No of Tickets: {number_of_tickets}")
print(f"Total Before Discount: {total_before_discount:.2f}")
print(F"Discount: {total_amount:.2f}")
print(f"Final Amount: {final_amount:.2f}")


