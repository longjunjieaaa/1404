#Number of items: 3
#Price of item: 100
#Price of item: 35.56
#Price of item: 3.24
#Total price for 3 items is $124.92

total = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid number")
    number = int(input("Number of items: "))
for i in range(number):
    price = float(input("Price of item: "))
    total += price
if total > 100:
    total =total * 0.9
print("Total price for {} items is ${:.2f}".format(number, total))

