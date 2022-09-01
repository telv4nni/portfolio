#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get card number from user
    const long card = get_long("What's the card number? ");
    long number = card;
    long modulo;
    long check = 0;

    //Multiply every other digit
    for (int i = number; i > 10; i = (i / 100))
    {
        modulo = 2 * ((number / 10) % 10);
        //Check if multiplied number is 2 digits
        if(modulo > 9)
        {
            modulo = 1 + (modulo % 10);
        }
        //Sum every other number
        check = check + modulo;
   }
    printf("%li \n", check);

}