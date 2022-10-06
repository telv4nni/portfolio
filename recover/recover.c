#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

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

    //loop through images
    for (int i = 0; i < sizeof(file); i++)
    {
    string filename = i;
    FILE *recoveredimage = fopen(sprintf(i, "%03i.jpg", 8), "w");
        //check if it's jpg
        if (datablock[0] == 0xff && datablock[1] == 0xd8 && datablock[2] == 0xff)
        {
            if (datablock[4] >= 0xe0 && datablock[4] <= 0xef)
            {
                //loop until image ends
                while (fread(datablock, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
                {
                    //save recovered blocks to new file
                    fwrite(file, BLOCK_SIZE, 1, recoveredimage);
                    free(recoveredimage);
                }
            }
        }
    }
    free(datablock);
    free(file);
    return 0;
}