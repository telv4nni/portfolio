#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get card number from user
    const long card = get_long("What's the card number? ");
    long number = card;
    long check = 0;

    //Multiply every other digit
    for (int i = 0; i < 8; i++)
    {
        //Get modulo from the second to last number
        check += 2 * ((number / 10) % 10);
    }
    printf("%li \n", check);

}