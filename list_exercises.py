Number: 5
Number: 20
Number: 1
Number: 2
Number: 3
The first number is 5
The last number is 3
The smallest number is 1
The largest number is 20
The average of the numbers is 6.2

numbers = []
for i in range(5):
    number = int(input("Enter number "))
    numbers.append(number)

print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is", sum(numbers) / len(numbers))