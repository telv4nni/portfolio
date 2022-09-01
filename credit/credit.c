#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get card number from user
    const long number = get_long("What's the card number? ");
    long check = number;
    //Multiply every other digit
    check = 2 * ((number / 10) % 10);
    printf("%li \n", check);

}