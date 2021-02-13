import string
import random

all_letters = string.ascii_letters
lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
digits = string.digits
punctuations = string.punctuation
# Esentially == string.printable, but without the whitespace characters.
all_chars = ''.join(string.ascii_letters + string.digits + string.punctuation)

print('What would you like your password to contain?\n')

user_pass_chars = input("""Enter 'Uppercase' for uppercase letters, 'Lowercase' for lowercase letters, or 'Both' for both,
'Digits' for numbers, and 'Punctuations' for symbols (ex: @#$%^&), and 'All Characters' for all characters. \n""")

user_pass_len = input('How long would you like your password to be? (Enter a number ex: 12) \n')

def password(pass_chars,pass_len):
    """ Function that generates a pseudo random password of a desired length and desired characters. """
    if pass_chars == 'Uppercase':
        print(''.join(random.choices(upper_letters,k=int(pass_len))))
    elif pass_chars == 'Lowercase':
        print(''.join(random.choices(lower_letters,k=int(pass_len))))
    elif pass_chars == 'Both':
        print(''.join(random.choices(all_letters,k=int(pass_len))))
    elif pass_chars == 'Digits':
        print(''.join(random.choices(digits,k=int(pass_len))))
    elif pass_chars == 'Punctuations':
        print(''.join(random.choices(punctuations,k=int(pass_len))))
    elif pass_chars == 'All Characters':
        print(''.join(random.choices(all_chars,k=int(pass_len))))
    elif pass_chars == '' and pass_len == '':
        print("You didn't enter any values, so here's a random password I made for you :D \n")
        print(''.join(random.choices(all_chars,k=random.randrange(8,22))))
    else:
        print('Sorry, please choose one of the available options.')

password(user_pass_chars,user_pass_len)