from cs50 import get_int


def main():
    number = getnumber()
    checkcard(number)



def getnumber():
    while True:
        number = get_int("Number: ")
        if int(number):
            return number


def checkcard(number / 2):
    check = 0
    for i in range(number):
        check += 2 * (number(number - (i * 2 - 1)))


