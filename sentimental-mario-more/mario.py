from cs50 import get_int

def get_height():
    while True:
        height = get_int("What's pyramid height? ")
        if height > 0 and height <= 8:
            return height

def printpyramid(n):
    size = n
    row = size
    //switch column
    for i in range(size):
        //draw a new row
        for j in range(row):
            //draw empty space
            print(" ")
        //Draw left blocks
        for k in range


def main():
    h = get_height()
    printpyramid(h)

main()