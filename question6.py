#write a program to find the maximum of two numbers
def maximum_of_two(a, b):
    if a > b:
        return a
    else:
        return b
num1 = 10
num2 = 20
print(f"The maximum of {num1} and {num2} is {maximum_of_two(num1, num2)}.")
