#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Compute the Coleman-Liau index
    int l = (letters / words) * 100;
    int s = (sentences / words) * 100;
    int index = 0.0588 * l - 0.296 * s - 15.8;
    // Print the grade level
    printf(index);
}

int count_letters(string text)
{
    // Return the number of letters in text
    for (int i = 0; i < strlen(text); i++)
    {
        
    }
}

int count_words(string text)
{
    // Return the number of words in text
}

int count_sentences(string text)
{
    // Return the number of sentences in text
}
