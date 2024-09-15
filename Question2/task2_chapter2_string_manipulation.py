# Given string
s = '56aAww1984sktr235270aYmn145ss785fsq31D0'

# Separate numbers and letters
number_string = ''
letter_string = ''

for char in s:
    if char.isdigit():  # If character is a digit, add to number_string
        number_string += char
    elif char.isalpha():  # If character is a letter, add to letter_string
        letter_string += char

# Convert even numbers to ASCII values
even_numbers_ascii = []
for num in number_string:
    if int(num) % 2 == 0:  # Check if the number is even
        even_numbers_ascii.append(ord(num))

# Convert uppercase letters to ASCII values
uppercase_letters_ascii = []
for char in letter_string:
    if char.isupper():  # Check if the letter is uppercase
        uppercase_letters_ascii.append(ord(char))

# Output the results
print("Number string:", number_string)
print("Letter string:", letter_string)
print("Even numbers in ASCII:", even_numbers_ascii)
print("Uppercase letters in ASCII:", uppercase_letters_ascii)
