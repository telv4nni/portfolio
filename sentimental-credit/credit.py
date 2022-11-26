from cs50 import get_string


def main():
    number = getnumber()
    checkcard(number)



def getnumber():
    while True:
        number = input("Number: ")
        if int(number):
            return number


def checkcard(creditnumber):
    check = sum = 0
    cardlen = len(creditnumber)

    if cardlen % 2 == 0:
        for i in range(cardlen):
            num = int(creditnumber[i])
            if i % 2 == 1:
                if (num * 2) > 10:
                    num = num * 2
                    sum += num // 10
                    sum += num % 10
                else:
                    sum += num
            else:
                sum += num
    #else:
        #for i in range(creditnumber[i]):


    print(sum)




main()

