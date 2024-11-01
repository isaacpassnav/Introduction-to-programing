
#number list #####
print("Wellcome to number list!, if you type 0 the game is over ")

numbers = []
number = -1

while number != 0:
    number = int(input("Enter number: "))
    if number != 0:
        numbers.append(number)

if 0 in numbers:
    numbers.remove(0)

positive_numbers = [num for num in numbers if num > 0]
smallest_positive = min(positive_numbers, default=None)

numbers.sort()

print("The sum is:", sum(numbers))
print("The average is:", sum(numbers) / len(numbers))
print("The largest number is:", max(numbers))
print("The smallest positive number is:", smallest_positive)
print("The sorted list is:", numbers)


