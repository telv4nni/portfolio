#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int size;
    do
    {
        size = get_int("Choose size of the pyramid (1-8): ");
    } while (size<1 || size>8);

    //Make a line
    for (int i=0; i<size; i++)
    {
        printf("#");
    }
    //Make next row
}