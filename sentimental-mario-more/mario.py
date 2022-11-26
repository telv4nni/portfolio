from cs50 import get_int

def get_height():
    while True:
        height = get_int("What's pyramid height? ")
        if height > 0 and height <= 8:
            return height

def printpyramid(n):
    size = n
    row = size
    #switch column
    for i in range(size):
        #draw a new row
        for j in range(row):
            #draw empty space
            print(" ", end="")
        #Draw left blocks
        #count hashes
        count = 1
        for k in range(size - count):
            print("#", end="")
            count + 1
        print()


def main():
    h = get_height()
    printpyramid(h)

main()