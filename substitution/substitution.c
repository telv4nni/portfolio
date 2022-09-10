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
    string ciphertext = 0;

    //convert key to uppercase
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (islower(argv[1][i]))
        {
           argv[1][i] = toupper(argv[1][i]);
        }
    }
    //make encryption
    for (int i = 0; i < strlen(plaintext); i++)
    {
        if isupper(plaintext[i])
        {
            int arg = (int)plaintext[i] - 65;
            ciphertext[i] = argv[1][arg];
        }
        else if islower(plaintext[i])
        {
            int arg = (int)plaintext[i] - 97;
            ciphertext[i] = argv[1][arg];
        }
    }
    printf("Ciphertext: %s", ciphertext);
}