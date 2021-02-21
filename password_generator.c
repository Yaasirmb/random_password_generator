#include <stdio.h>
#include <string.h>


int password(char pass_chars,int pass_len);

void main() {

    char user_char[15];
    char uppercase [ ] = "Uppercase";
    int result;
    char upper_letters[ ] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    
    printf("What would you like your password to have?\n");
    while ((result != 1) || (result != -1)){
        gets(user_char);

        result = strcmp(user_char,uppercase);
        printf("%i\n",result);

        if (result == 0)
            printf("%s\n",upper_letters);
        else 
            printf("These are not the same string\n");
    }
        /*password(user_char,user_pass_len);*/
  
};


 /*int password(char pass_chars,int pass_len){

    char user_char;
    int user_pass_len;
    int result;
    char all_letters[ ] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char lower_letters[ ] = "abcdefghijklmnopqrstuvwxyz";
    char upper_letters[ ] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char digits[ ] = "0123456789";
    char punctuations[ ] = "!\"#$%&\'()*+,-./:;<=>?@\[]^_`{|}~";
    char all_chars[ ] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&\'()*+,-./:;<=>?@\[]^_`{|}~";
    char uppercase [ ] = "Uppercase";

    printf("What would you like your password to contain?");
    

   else if (user_char == "Lowercase")
        printf("%s",lower_letters);
    else if (user_char == "Both")
        printf("%s",all_letters);
    else if (user_char == "Digits")
        printf("%s",digits);
    else if (user_char == "Punctuations")
        printf("%s",punctuations);
    else if (user_char == "All Characters")
        printf("%s",all_chars);

};*/



