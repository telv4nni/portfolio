from cs50 import get_int


def main():
    number = getnumber()
    checkcard()



def getnumber():
    while True:
        number = get_int("Number: ")
        if int(number):
            return number


def checkcard(number):
    