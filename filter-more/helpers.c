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
    //create Gx and Gy
    RGBTRIPLE Gx[height][width];
    RGBTRIPLE Gy[height][width];
    //copy pixels from image to Gx and Gy
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            Gx[i][j] = image[i][j];
            Gy[i][j] = image[i][j];
        }
    }

    //Loop rows
    for (int i = 0; i < height; i++)
    {
    //Loop columns
        for (int j = 0; j < width; j++)
        {
            //initialize sums
            int Gyredsum = 0, Gygreensum = 0, Gybluesum = 0;
            int Gxredsum = 0, Gxgreensum = 0, Gxbluesum = 0;
            int pxlcount = 0;
            //Check adjacent pixels
            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    //check if pixel exists
                    if ((i + k) < 0 || (i + k) > height)
                    {
                        continue;
                    }
                    if ((j + l) < 0 || (j + l) > width)
                    {
                        continue;
                    }
                    //Multiply in kernel
                    //Add pixel to Gx sum
                    Gxredsum += (Gx[i + k][j + l].rgbtRed * l);
                    Gxgreensum += (Gx[i + k][j + l].rgbtGreen * l);
                    Gxbluesum += (Gx[i + k][j + l].rgbtBlue * l);
                    if (k == 0)
                    {
                        Gxredsum *= 2;
                        Gxgreensum *= 2;
                        Gxbluesum *= 2;
                    }
                    //Add pixel to Gy sum
                    Gyredsum += (Gy[i + k][j + l].rgbtRed * k);
                    Gygreensum += (Gy[i + k][j + l].rgbtGreen * k);
                    Gybluesum += (Gy[i + k][j + l].rgbtBlue * k);
                    if (l == 0)
                    {
                        Gyredsum *= 2;
                        Gygreensum *= 2;
                        Gybluesum *= 2;
                    }
                    pxlcount++;
                }
            }
            //Divide sum by count of pixels
            Gxredsum /= pxlcount;
            Gxgreensum /= pxlcount;
            Gxbluesum /= pxlcount;
            Gyredsum /= pxlcount;
            Gygreensum /= pxlcount;
            Gybluesum /= pxlcount;
            image[i][j].rgbtRed = (round(sqrt(pow(Gxredsum, 2) + pow(Gyredsum, 2))));
            image[i][j].rgbtGreen = (round(sqrt(pow(Gxgreensum, 2) + pow(Gygreensum, 2))));
            image[i][j].rgbtBlue = (round(sqrt(pow(Gxbluesum, 2) + pow(Gybluesum, 2))));
        }
    }

    //Multiply adjacent pixels by kernel
    //Combine Gx and Gy in image
    return;
}
