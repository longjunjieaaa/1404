#get sales
#while sales >= 0
#    calculate bonus
#    get sales
#do next thing (if needed)
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        sales_bonus = sales * 0.1
    else:
        sales_bonus = sales * 0.15
    print("You sales bonus is $", sales_bonus)
    sales = float(input("Enter sales: $"))
