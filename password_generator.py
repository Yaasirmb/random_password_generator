letters = ['A','B','C','D','E']
user_options = []
options = 'Letters(upper and lowercase), numbers, and special symbols.'
password_options = ["Letters","Numbers","Symbols"]    


def user():
    """Take the 's user_input."""
    while True:
        print ('Your password can contain all or some of the following: Letters(upper and lowercase), numbers, and special symbols.')
        user_input = input("Please type what you would like to include in your password.\n").title()
        if user_input in password_options:
            user_options.append(user_input)
            print('Your current options are ' + str(user_options))
        elif user_input == 'Done' and len(user_options) <= 3:
            for option in user_options:
                    print(option)
        elif len(user_options) > 3:
            print("You can only choose 3 options.")
            print('Letters(upper and lowercase), numbers, and special symbols.')
            print('\n')           
            break

        elif user_options == 'Done' and len(user_options) == 0:
            print('Good Bye.')
            break
        
        elif user_input == 'Option':
            print(options)
        elif user_input == 'user_input':
            print(str(user_input))
        elif user_input == 'Help':
            print('\n')
            
        elif user_input == 'Remove':
            remove = input('Here is your current user_input ' + str(user_options) + ' what would you like to remove? \n').title()
            if remove in user_input:
                user_options.remove(remove)
                print(str(user_options) + '\n')
            else:
                print("Sorry this option is not among the options you chose. You currently have: " + str(user_input) + '\n' )
        elif user_input not in letters:
            print('This item is not a valid option.\n')
        return(user_input)

user()