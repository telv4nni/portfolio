from cs50 import get_int


def main():
    number = getnumber()
    checkcard(number)



def getnumber():
    while True:
        number = get_int("Number: ")
        if int(number):
            return number


def checkcard(number):
    check = sum = 0
    cardlen = len(number)

    if cardlen != 13 and cardlen != 15 and cardlen != 16:
        print("INVALID")

    if cardlen % 2 == 0:
        for i in range(cardlen):
            digit = number[i]
            if i%




main()

