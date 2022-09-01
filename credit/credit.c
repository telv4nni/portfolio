#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get card number from user
    const long card = get_long("What's the card number? ");
    long number = card;
    long check = 0;

    //Multiply every other digit
for (int )
        //Get modulo from the second to last number
        check += 2 * ((number / 10) % 10);
    }
    while (number > 0);
    printf("%li \n", check);

}