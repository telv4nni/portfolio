#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get card number from user
    do
    {
        long number = get_long("What's the card number?");
    }
    while (number);
}