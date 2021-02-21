#include <stdio.h>
#include <string.h>

void main() {

    char user_char[15];
    char uppercase [ ] = "Uppercase";
    int upper_cmp;
    int lower_cmp;
    int both_cmp;
    int digit_cmp;
    int punct_cmp;
    int all_cmp;
    char all_letters[ ] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char lower_letters[ ] = "abcdefghijklmnopqrstuvwxyz";
    char upper_letters[ ] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char digits[ ] = "0123456789";
    char punctuations[ ] = "!\"#$%&\'()*+,-./:;<=>?@\[]^_`{|}~";
    char all_chars[ ] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&\'()*+,-./:;<=>?@\[]^_`{|}~";
    char *user_options[] = {"Uppercase","Lowercase","Both","Digits","Symbols","All Characters"};

    /*int i;
    char user_option;
    for(i = 0; i < len; ++i){
        user_option = user_options[i];
        // Result of comparing the 2 strings together.
        result = strcmp(user_char,user_option);
    }*/
    

    
    printf("What would you like your password to have?\n");
    printf("Enter 'Uppercase' for uppercase letters, 'Lowercase' for lowercase letters, or 'Both' for both,"
    "'Digits' for numbers, and 'Punctuations' for symbols (ex: @#$%^&), and 'All Characters' for all characters.\n");
    
    gets(user_char);

    upper_cmp = strcmp(user_char,user_options[0]);
    lower_cmp = strcmp(user_char,user_options[1]);
    both_cmp = strcmp(user_char,user_options[2]);
    digit_cmp = strcmp(user_char,user_options[3]);
    punct_cmp = strcmp(user_char,user_options[4]);
    all_cmp = strcmp(user_char,user_options[5]);
    

    if (upper_cmp == 0)
        printf("%s\n",upper_letters);
    else 
        if (lower_cmp == 0)
            printf("%s\n",lower_letters);
    else 
        if (both_cmp == 0)
            printf("%s\n",all_letters);
    else
        if (digit_cmp == 0)
            printf("%s\n",digits);
    else 
        if (punct_cmp == 0)
            printf("%s\n",punctuations);
    else
        if (all_cmp == 0)
            printf("%s\n",all_chars);
    else
        printf("Please select a valid option.");

        /*password(user_char,user_pass_len);*/
  
};


 /*int password(char pass_chars,int pass_len){


};*/



