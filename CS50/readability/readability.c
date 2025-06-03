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
    float l = ((float) letters / words) * 100;
    float s = ((float) sentences / words) * 100;
    float index = 0.0588 * l - 0.296 * s - 15.8;
    int grade = round(index);
    // Print the grade level
    if (grade <= 1)
        {
            printf("Before Grade 1\n");
        }
    else if (grade >= 16)
        {
            printf("Grade 16+\n");
        }
    else
        {
            printf("Grade %d\n", grade);
        }
}

int count_letters(string text)
{
    // Return the number of letters in text
    int letters = 0;
    for (int i = 0; i < strlen(text); i++)
    {
       char letter = text[i];
       if (isalpha(letter))
        letters++;
    }
    return letters;
}

int count_words(string text)
{
    // Return the number of words in text
    int words = 1;
    for (int i = 0; i < strlen(text); i++)
    {
       char letter = text[i];
       if (letter == ' ')
        words++;
    }
    return words;
}

int count_sentences(string text)
{
    // Return the number of sentences in text
    int sentences = 0;
    for (int i = 0; i < strlen(text); i++)
    {
       char letter = text[i];
       if (letter == '.' || letter == '!' || letter == '?')
        sentences++;
    }
    return sentences;
}
