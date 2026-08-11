n = int(input("enter the number:"))
even_count = 0
odd_count = 0
for i in range(1,11):
    result = n * i

    if result % 2 == 0:
        parity = "Even"
        even_count += 1
    else:
        parity = "Odd"
        odd_count += 1
    print(f"{n} X {i} = {result} - {parity}")
print()
print(f"Even Results: {even_count}")
print(f"Odd Results: {odd_count}")
