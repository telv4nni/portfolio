#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int size;
    do
    {
        size = get_int("Choose size of the pyramid (1-8): ");
    } while (size<1 || size>8);

    //Column
    for (int i=0; i<size; i++)
    {
        //Row
        for(int j=0; j<size; j++)
        {
            do
            {
                printf(" ");
            } while 
        }
        printf("#\n");
    }
}