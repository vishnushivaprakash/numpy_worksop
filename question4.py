#write a program to find the sum of digits of a given number'
def sum_of_digits(number):
    num_str = str(number)
    total = 0
    for digit in num_str:
        total += int(digit)
    return total
number = 12345
print(f"The sum of the digits of {number} is {sum_of_digits(number)}.")
