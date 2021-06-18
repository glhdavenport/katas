# Page 46

# print("10 + 15 =", 10 + 15)

# Write a script that receives two numbers from the user and displays the result of taking 
# the first number to the power of the second number.


# base = input("Enter a base: ")
# exponent = input("Enter an exponent: ")
# result = float(base)**float(exponent)

# print(f"{base} to the power of {exponent} = {result}")

# print("{} to the power of {} = {}".format(base,exponent,result))


# squid = float(input("Enter a number:"))
# possum = int("42")

# print(square(squid))
# print(square(possum))

# def square(number):
#     return number ** 2

# def return_difference(num1, num2):
#     """It's subtraction, idiot."""
#     return num1 - num2

# print(return_difference(3, 5))

# num_difference = float(input("Enter a number: "))
# num_difference2 = float(input("Enter another number: "))

# print(return_difference(num_difference, num_difference2))
# help(return_difference)

# def cube(num1):
#     """We're cubing a number"""
#     return num1 ** 3

# print(cube(4))

# def multiply(num1, num2):
#     """Multiplication"""
#     return num1 * num2

# inputnumbers = float(input("Enter a number: "))
# inputnumbers2 = float(input("Enter another number: "))

# print(multiply(inputnumbers, inputnumbers2))

def celsius(num1):
    """This will convert a celsius temp to fahrenheit"""
    return (num1 - 32) * 5/9

def fahrenheit(num1):
    """This will convert a fahrenheit temp to celsius"""
    return num1 * 9/5 + 32

f = float(input("Enter a temperature in Fahrenheit: "))
celsius = celsius(f)
print(f"{f} in Fahrenheit is {celsius} Celsius")

c = float(input("Enter a temperature in Celsius: "))
fahrenheit = fahrenheit(c)
print(f"{c} in Celsius is {fahrenheit} Fahrenheit")