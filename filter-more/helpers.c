#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            average = round((round(image[i][j].rgbtRed) + round(image[i][j].rgbtGreen) + round(image[i][j].rgbtBlue)) / 3);
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < (width / 2); j++)
        {
            tmp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = tmp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //create temporary image
    RGBTRIPLE temp[height][width];
    //copy all the pixels from image to temp image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < (width - 1); j++)
        {
            temp[i][j] = image[i][j];
        }
    }
    //Sum adjacent pixels
    //Next Row
    for (int i = 0; i < height; i++)
    {
        //Next Pixel
        for (int j = 0; j < width; j++)
        {
            int sumred = 0;
            int sumgreen = 0;
            int sumblue = 0;
            int pxlcount = 0;
            //Check adjacent pixels
            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    //check if theres a pixel in the row
                    if ((i + k) < 0 || (i + k) > height)
                    {
                        continue;
                    }
                    //check if theres a pixel in the column
                    if ((j + l) < 0 || (j + l) > width)
                    {
                        continue;
                    }
                    //Add pixel to sum
                    sumred += temp[i + k][j + l].rgbtRed;
                    sumgreen += temp[i + k][j + l].rgbtGreen;
                    sumblue += temp[i + k][j + l].rgbtBlue;
                    pxlcount++;
                }
            }
            //make pixel blurred
            image[i][j].rgbtRed = round(sumred / pxlcount);
            image[i][j].rgbtGreen = round(sumgreen / pxlcount);
            image[i][j].rgbtBlue = round(sumblue / pxlcount);
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
