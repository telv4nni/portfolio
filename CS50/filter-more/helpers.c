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
        for (int j = 0; j < width; j++)
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
            float sumred = 0;
            float sumgreen = 0;
            float sumblue = 0;
            int pxlcount = 0;
            //Check adjacent pixels
            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    //check if theres a pixel in the row
                    if ((i + k) < 0 || (i + k) >= height)
                    {
                        continue;
                    }
                    //check if theres a pixel in the column
                    if ((j + l) < 0 || (j + l) >= width)
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
    //create temp image
    RGBTRIPLE temp[height][width];
    //copy pixels from image to Gx and Gy
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }
    //Make kernel modifiers
    int xkernel[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int ykernel[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    //Loop rows
    for (int i = 0; i < height; i++)
    {
        //Loop columns
        for (int j = 0; j < width; j++)
        {
            //initialize sums
            float Gyredsum = 0, Gygreensum = 0, Gybluesum = 0;
            float Gxredsum = 0, Gxgreensum = 0, Gxbluesum = 0;
            int red, green, blue;
            //Check adjacent pixels
            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    //check if pixel exists
                    if ((i + k) < 0 || (i + k) >= height)
                    {
                        continue;
                    }
                    if ((j + l) < 0 || (j + l) >= width)
                    {
                        continue;
                    }
                    //Multiply in kernel
                    //Add pixel to Gx sum
                    Gxredsum += (temp[i + k][j + l].rgbtRed * xkernel[k + 1][l + 1]);
                    Gxgreensum += (temp[i + k][j + l].rgbtGreen * xkernel[k + 1][l + 1]);
                    Gxbluesum += (temp[i + k][j + l].rgbtBlue * xkernel[k + 1][l + 1]);

                    //Add pixel to Gy sum
                    Gyredsum += (temp[i + k][j + l].rgbtRed * ykernel[k + 1][l + 1]);
                    Gygreensum += (temp[i + k][j + l].rgbtGreen * ykernel[k + 1][l + 1]);
                    Gybluesum += (temp[i + k][j + l].rgbtBlue * ykernel[k + 1][l + 1]);
                }
            }
            red = (round(sqrt(pow(Gxredsum, 2) + pow(Gyredsum, 2))));
            green = (round(sqrt(pow(Gxgreensum, 2) + pow(Gygreensum, 2))));
            blue = (round(sqrt(pow(Gxbluesum, 2) + pow(Gybluesum, 2))));
            //Check if greater than 255
            if (red > 255)
            {
                red = 255;
            }
            if (green > 255)
            {
                green = 255;
            }
            if (blue > 255)
            {
                blue = 255;
            }
            //Replace pixels in image
            image[i][j].rgbtRed = red;
            image[i][j].rgbtGreen = green;
            image[i][j].rgbtBlue = blue;
        }
    }
    return;
}
