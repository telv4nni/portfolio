#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int size;
    do
    {
        size = get_int("Choose size of the pyramid (1-8): ");
    } while (size<1 || size>8);

    int row = size;
    //Switch Column
    for (int i=0; i<size; i++)
    {
        //Draw a Row
        for(int j=0; j<row; j++)
        {
            printf(" ");
        }
                   //Draw blocks
         for(int k=row; k > row; k--)
        {
            printf("#");
        }
        printf("\n");
        row--;
    }
}