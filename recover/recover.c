#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <cs50.h>

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

    BYTE datablock[BLOCK_SIZE];

    //create name of new file and file counter
    char filename[8];
    int counter = 0;
    FILE *recoveredimage;


    //loop until file ends
    while (fread(datablock, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
        {
            //check if it's jpg
            if (datablock[0] == 0xff && datablock[1] == 0xd8 && datablock[2] == 0xff && (datablock[3] & 0xf0) == 0xe0)
            {
                if (!(counter == 0))
                {
                    fclose(recoveredimage);
                }

                //change name of new file
                sprintf(filename, "%03i.jpg", counter);

                //open new file
                recoveredimage = fopen(filename, "w");
                counter++;

                //save recovered block to new file if jpg found
                if (!(counter == 0))
                {
                    fwrite(&recoveredimage, 1, BLOCK_SIZE, recoveredimage);
                }
            }
        }
    free(file);
    return 0;
}