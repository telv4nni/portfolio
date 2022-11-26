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
    even = odd = sum = 0
    

main()

