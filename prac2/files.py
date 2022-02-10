1.
out_file = open("name.txt")
name = input("enter your name? ")
print(name, file=out_file)
out_file.close()

2.
name = in_file.read().strip()
in_file.close()
print("Your name is Bob")

3.
in_file = open("numbers.txt")
file1 = int(in_file.readline())
file2 = int(in_file.readline())
in_file.close()
print(number1 + number2)


4.in_file = open("numbers.txt")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)