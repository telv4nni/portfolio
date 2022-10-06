#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;
const int BLOCK_SIZE = 512;

int main(int argc, char *argv[])
{
    //check number of arguments
    if (argc != 2)
    {
        printf("Use: ./recover *filetorecover*.raw");
        return 1;
    }

    //load file
    FILE *file = fopen(argv[1], "r");
    //check if you can read the file
    if (file == NULL)
    {
        printf("Could not open *file*.raw");
        return 1;
    }

    BYTE *datablock = malloc(BLOCK_SIZE);

    //loop until image ends
    while (fread(datablock, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
    {

    }
}