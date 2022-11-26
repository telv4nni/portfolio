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
    cardlen = len(str(number))

    if cardlen % 2 == 0:
        for i in range(cardlen):
            digit = 2 * number[i]
            if digit > 10:
                sum = digit[0] + digit[1]
            else:
                sum = digit

    print(sum)




main()

