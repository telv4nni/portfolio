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

    # Check if number of digits is even or odd
    if cardlen % 2 == 0:
        # if number of digits is even start counting from first digit
        for i in range(cardlen):
            # Multiply first digit by 2
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
        #if number of digits is odd start counting from second digit


    print(sum)




main()

