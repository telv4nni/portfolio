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
        //Draw empty space
        for(int j=0; j<row; j++)
        {
            printf(" ");
        }
                   //Draw left blocks
        for(int k=0; k < i+1; k++)
        {
            printf("#");
        }
        printf("  ");
        //Draw right blocks
        for(int k=0; k < i+1; k++)
        {
            printf("#");
        }
        printf("\n");
        row--;
    }
}