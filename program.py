from password_generator import password
import time
#print('What would you like your password to contain?\n')
#user_pass_chars = input("""Enter 'Uppercase' for uppercase letters, 'Lowercase' for lowercase letters, or 'Both' for both,
#'Digits' for numbers, and 'Punctuations' for symbols (ex: @#$%^&), and 'All Characters' for all characters. \n""")
#user_pass_len = input('How long would you like your password to be? (Enter a number ex: 12) \n')
start_time = time.time()

chars = ''
pass_len = ''
for _ in range(0,1000000):
    password(chars,pass_len)

print("Random module took: --- %s seconds ---" % (time.time() - start_time))
