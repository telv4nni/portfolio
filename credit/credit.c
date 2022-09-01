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
    for (long i = number; i > 0; i = i / 100)
    {
        modulo = 2 * ((number / 10) % 10);
        number = number / 100;
        //Check if multiplied number is 2 digits
        if(modulo > 9)
        {
            modulo = 1 + (modulo % 10);
        }
        //Sum every other number
        check = check + modulo;
        printf("%li\n", check);
   }
    //Add numbers not multiplied
    number = card;
    for (long i = number; i > 0; i = i / 100)
    {
        modulo = number % 10;
        number = number / 100;
        check = check + modulo;
        printf("%li\n", check);
    }
    number = card;
    //Check validity
    printf("%li\n", check);
    if ((number >= 4000000000000000 && number < 5000000000000000 && (check % 10) == 0) || (number >= 4000000000000 && number < 5000000000000 && (check % 10) == 0))
    {
        printf("VISA\n");
    }
    else if (number >= 340000000000000 && number < 380000000000000 && (check % 10) == 0)
    {
        printf("AMEX\n");
    }
    else if (number >= 5100000000000000 && number < 5600000000000000 && (check % 10) == 0)
    {
        printf("MASTERCARD\n");
    }

    else
    {
        printf("INVALID\n");
    }
}