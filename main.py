# def string_methods_practice():
#     # Eingabe eines Strings
#     input_string = input("Geben Sie einen beliebigen Text ein: ")
#
#     # Anwenden der String-Methoden
#     print("capitalize():", input_string.capitalize())
#     print("lower():", input_string.lower())
#     print("upper():", input_string.upper())
#     print("title():", input_string.title())
#     print("swapcase():", input_string.swapcase())
#     print("strip():", input_string.strip())
#     print("split():", input_string.split())
#     print("replace('a', 'b'):", input_string.replace('a', 'b'))
#     print("find('e'):", input_string.find('e'))
#     print("startswith('H'):", input_string.startswith('H'))
#     print("endswith('d'):", input_string.endswith('d'))
#     print("len():", len(input_string))
# string_methods_practice()
import pprint

# s = input("just for fun give me a sentence : -> ")
# mid = len(s)//2
# print(s[mid])


# a = 8
# b = 9.7
# c = "hello"returns the largest integer that is less than or equal to 10 / 3, which is 3.
#
#
# Tue, Nov 28, 2023, 7:10 pm
# +
# print(type(a))
# print(type(b))
# print(type(c))


# a = 8
# b = "python lovers"
# c = f"{a} {b} -> "
# print(c)
#
# print(f"""
# {a} {b} ->
# next = {a+1}
# """)

#
# print(f"{10//3}")
# print(f"{10/3}")


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulos = num1 % num2
exponentiation = num1 ** num2
print("Ergebnisse:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Floor Division: {floor_division}")
print(f"Modulos: {modulos}")
print(f"Exponentiation: {exponentiation}")