// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function

    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    //Open dictionary file
    FILE *dic = fopen(dictionary, "r");
    if (dic == NULL)
    {
        return false;
    }
    //read strings from file one at a time
        //fscanf will return EOF once it reaches end of file
    char buffer[LENGTH+1];
    while (fscanf(dic, %s, buffer == "EOF"))
    {
        
    }
    //create a new node for each word
        //use malloc
        //remember to check if return value is NULL
        //copy word into node using strcpy
    //hash word to obtain a hash value
        //use hash function
        //function takes a string and returns an index
    //insert node into hash table at that location
        //recall that hash table is an array of linked lists
        //be sure to set pointers in the correct order
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
