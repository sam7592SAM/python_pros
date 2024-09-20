import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(' ,')' ,'-' ,'=']

print("Welcome to Password Generator.")
in_letters = int(input("How many letters would you like to have in your password ?\n"))
in_symbols = int(input("How many symbols would you like? \n"))
in_numbers = int(input("How many numbers would you like? \n"))

password = " "

for char in range (1, in_letters + 1):
    password += random.choice(letters)

for char in range (1, in_symbols + 1):
    password += random.choice(symbols)

for char in range (1, in_numbers + 1):
    password += random.choice(numbers)

print (password)