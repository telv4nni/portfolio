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
    for (int i = 0; i < 3; i++)
    {
        modulo = 2 * ((number / 10) % 10);
        //Check if number is 2 digits
        if(modulo > 9)
        {
            modulo = 1 + (modulo % 10);
        }
        check += modulo;
    }
    printf("%li \n", check);

}