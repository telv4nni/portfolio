from cs50 import get_int

def get_height():
    while True:
        height = get_int("What's pyramid height? ")
        if height > 0 and height <= 8:
            return height

def printpyramid(n):
    for i in range(n-1):
        print(" ", end="")
    print("#", end="")
    print()

def main():
    h = get_height()
    printpyramid(h)

main()