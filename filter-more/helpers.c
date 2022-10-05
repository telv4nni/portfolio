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
    RGBTRIPLE average;
    average.rgbtRed = 0;
    average.rgbtGreen = 0;
    average.rgbtBlue = 0;
    //Go to next row
    for (int i = 0; i < height; i++)
    {
        //Go to next pixel
        for (int j = 0; j < (width - 1); j++)
        {
            int pxltoblur = 0;
            for(int column = -1; column < 2; column++)
            {
                //Sum all of the nearby pixels
                for (int row = -1; row < 2; row++)
                {
                    if ((i + column) >= 0 && (i + column) < height && (j + row) >= 0 && (j + row) < (width - 1))
                    {
                        average.rgbtRed += image[i + column][j + row].rgbtRed;
                        average.rgbtGreen += image[i + column][j + row].rgbtGreen;
                        average.rgbtBlue += image[i + column][j + row].rgbtBlue;
                        pxltoblur++;
                    }
                }
            }
            //Change pixel to average value
            average.rgbtRed = round(average.rgbtRed) / pxltoblur;
            average.rgbtBlue = round(average.rgbtBlue) / pxltoblur;
            average.rgbtGreen = round(average.rgbtGreen) / pxltoblur;
            image[i][j] = average;
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
