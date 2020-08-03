# This is a python script that gerates a random password.

import random
from random import randrange


letters = ['A','B','C','D','E']

symbols = [' ','!','"','#','$','%','&',"'",'(',')','*',
    '+',',','-','.','/',':',';','<','=',">",'?','@','['
    ,']','^','_','`','{','|','}','~',']',"\\"]

user_options = []
password_options = ["Letters","Numbers","Symbols"]    

def user():
    message = ("Your password can contain all or some of the following: Letters(upper and lowercase), numbers, and special symbols.")
    
    while True:
        print(message)
        print("Type 'Done' when you're ready to generate your password.")
        user_input = input('Please type what you would like to include in your password.\n').title()

        if user_input in password_options:
            user_options.append(user_input)
        elif user_input.title() == 'Done' or len(user_options) == 3: 
            print('You chose the following options: ')
            #print(str(user_options))
            for option in user_options:
                print(option)
                break
            print('Your password is \n: ')

        elif user_input not in password_options:
            print("Sorry please choose one of the following options.")
            print(message)
                    

user()


"""def random_number():
    randrange(10)

def random_symbol():
    

def random_letter():
    print(random.sample(letters,2))"""
    

