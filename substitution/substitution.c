#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    string convert(string key);
    string encrypt(string key, string plaintext);
    int check(int numberofarguments, string key);

    check(argc, argv[1]);
    convert(argv[1]);
    string plaintext = get_string("plaintext: ");
    encrypt(argv[1], plaintext);
}

int check(int numberofarguments, string key)
{
// Check if proper number of arguments
    if (numberofarguments != 2)
        {
            printf("Usage: ./substitution key\n");
            return 1;
        }
    // Check if argument is correct length
    if (strlen(key) != 26)
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
    // Check if argument is valid
    for (int i = 0; i < strlen(key); i++)
    {
        for (int n = i + 1; n < strlen(key); n++)
        {
            if (key[i] == key[n])
            {
            printf("Key invalid\n");
            return 1;
            }
        }
        if (isalpha(key[i]) == 0)
        {
            printf("Key invalid\n");
            return 1;
        }
    }
    return 0;
}

string convert(string key)
{
    //convert key to uppercase
    for (int i = 0; i < strlen(key); i++)
    {
        if (islower(key[i]))
        {
           key[i] = toupper(key[i]);
        }
    }
    return key;
}

string encrypt(string key, string plaintext)
{
    string ciphertext = plaintext;
    for (int i = 0; i < strlen(plaintext); i++)
    {
        if isupper(plaintext[i])
        {
            ciphertext[i] = key[(int)plaintext[i] - 65];
        }
        else if islower(plaintext[i])
        {
            ciphertext[i] = key[(int)plaintext[i] - 97];
            ciphertext[i] = tolower(ciphertext[i] );
        }
    }
    printf("ciphertext: %s\n", ciphertext);
    return ciphertext;
}
