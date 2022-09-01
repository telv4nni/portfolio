#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get card number from user
    const long card = get_long("What's the card number? ");
    long number = card;
    long check = 0;

    //Multiply every other digit
    for (int i = number; i > 0; i = i / 100)
    {
        check += 2 * ((number / 10) % 10);
    }
    printf("%li \n", check);

}