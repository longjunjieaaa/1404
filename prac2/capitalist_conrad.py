Starting price: $10.00
On day 1 price is: $9.89
...
On day 424 price is: $915.71
On day 425 price is: $1,001.60

import random

MAX_INCREASE = 0.1
MAX_DECREASE = 0.05
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "stock_output.txt"
out_file = open(OUTPUT_FILE, 'w')
price = INITIAL_PRICE
day = 0
print("Starting price: ${:,.2f}".format(price), file=out_file)
while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    day += 1
    if random.randint(1, 2) == 1:
         price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)
    price *= (1 + price_change)
    print("On day {} price is: ${:,.2f}".format(day, price), file=out_file)
out_file.close()