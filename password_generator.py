import string
import secrets

all_letters = string.ascii_letters
lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
digits = string.digits
punctuations = string.punctuation
# Esentially == string.printable, but without the whitespace characters.
all_chars = ''.join(string.ascii_letters + string.digits + string.punctuation)

def password(pass_chars,pass_len):
    """ Function that generates a random password of a desired length and desired characters. """
    if pass_chars == 'Uppercase':
        print(''.join(secrets.choice(upper_letters) for i in range(int(pass_len))))
    elif pass_chars == 'Lowercase':
        print(''.join(secrets.choice(lower_letters) for i in range(int(pass_len))))
    elif pass_chars == 'Both':
        print(''.join(secrets.choice(all_letters) for i in range(int(pass_len))))
    elif pass_chars == 'Digits':
        print(''.join(secrets.choice(digits) for i in range(int(pass_len))))
    elif pass_chars == 'Punctuations':
        print(''.join(secrets.choice(punctuations) for i in range(int(pass_len))))
    elif pass_chars == 'All Characters':
        print(''.join(secrets.choice(all_chars) for i in range(int(pass_len))))
    elif pass_chars == '' and pass_len == '':
        #print("You didn't enter any values, so here's a random password I made for you :D \n")
        print(''.join(secrets.choice(all_chars) for i in range(12)))
    else:
        print('Sorry, please choose one of the available options.')
