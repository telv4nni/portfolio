#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    // Check if proper number of arguments
    if (argv[2] != NULL || argv[1] == NULL)
        {
            printf("Usage: ./substitution key\n");
            return 1;
        }
    // Check if argument is correct length
     if (strlen(argv[1]) != 26)
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }

    string plaintext = get_string("Plaintext: ");
    string ciphertext;
    printf("%c\n", argv[1][2]);
    for (int i = 0; i < strlen(argv[1]); i++)
    {
    }
}