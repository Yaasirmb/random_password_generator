from password_generator import password

#print('What would you like your password to contain?\n')
user_pass_chars = input("""Enter 'Uppercase' for uppercase letters, 'Lowercase' for lowercase letters, or 'Both' for both,
'Digits' for numbers, and 'Punctuations' for symbols (ex: @#$%^&), and 'All Characters' for all characters. \n""")
user_pass_len = input('How long would you like your password to be? (Enter a number ex: 12) \n')

#chars = ''
#pass_len = ''
#for _ in range(10):
password(user_pass_chars,user_pass_len)
