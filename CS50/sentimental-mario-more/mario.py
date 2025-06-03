from cs50 import get_int


def get_height():
    while True:
        height = get_int("What's pyramid height? ")
        if height > 0 and height <= 8:
            return height


def printpyramid(n):
    size = n
    # left side
    for i in range(size):
        print(" " * (size - (i + 1)), end="")
        print("#" * (i + 1), end="")
    # right side
        print("  ", end="")
        print("#" * (i + 1))


def main():
    h = get_height()
    printpyramid(h)


main()
