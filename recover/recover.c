#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Use: ./recover *filetorecover*.raw");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    
}