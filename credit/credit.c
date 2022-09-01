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
    do
    {
        //Get modulo from the second to last number
        modulo = 2 * ((number / 10) % 10);
        check += modulo;
    }
    while (number > 0);
    printf("%li \n", check);

}