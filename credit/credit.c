#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get card number from user
    const long number = get_long("What's the card number? ");
    long check = number;
    //Multiply every other digit
    for (int i = 0; check > i; i++)
    {
        check = 2 * ((number / 10) % 10);
    }
    printf("%li \n", check);

}