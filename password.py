import secrets
import string

import pyperclip

letters = string.ascii_letters
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special = string.punctuation

chars = letters + digits + special
length = 16

while True:
    password_list = [secrets.choice(chars) for i in range(16)]
    password = ('').join(password_list)

    has_lowercase = any(char in lowercase for char in password)
    has_uppercase = any(char in uppercase for char in password)
    has_digit = any(char in digits for char in password)
    has_special = any(char in special for char in password)

    if all((has_lowercase, has_uppercase, has_digit, has_special)):
        break

print('Copied to clipboard:')
print(password)
pyperclip.copy(password)
