finished = False
result = 0
while not finished:
    try:
        # TODO: this line
        # TODO: this line
        pass
    except:  # TODO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", result)

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
    except:
        print("Please enter a valid integer.")
print("Valid result is:", result)