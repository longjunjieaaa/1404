1. When will a ValueError occur?  numerator= 0
2. When will a ZeroDivisionError occur?denominator=0
3. Could you change the code to avoid the possibility of a ZeroDivisionError? NO


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")



