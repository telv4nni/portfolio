import re
from cs50 import get_string


def main():
    number = getnumber()
    check = checksum(number)
    validate(check, number)



def getnumber():
    while True:
        number = input("Number: ")
        if int(number):
            return number


def checksum(creditnumber):
    check = sum = 0
    cardlen = len(creditnumber)

    # Check if number of digits is even or odd
    if cardlen % 2 == 0:
        # if number of digits is even start counting from first digit
        for i in range(cardlen):
            # Check if digit is odd
            # Assign digit to check number
            num = int(creditnumber[i])
            if i % 2 == 0:
                # Multiply odd number by 2
                num = 2 * num
                # Check if multiplied number is greater than 10
                # Add odd number
                if num >= 10:
                    sum += num // 10
                    sum += num % 10
                else:
                    sum += num
            else:
                # add even number
                sum += num
    else:
        # if number of digits is odd, start counting from second digit
        for i in range(cardlen):
            # Check if digit is even
            # Assign digit to check number
            num = int(creditnumber[i])
            if i % 2 != 0:
                # Multiply even number by 2
                num = 2 * num
                # Check if multiplied number is greater than 10
                # Add even number
                if num >= 10:
                    sum += num // 10
                    sum += num % 10
                else:
                    sum += num
            else:
                # Add odd number
                sum += num
    print(sum)
    sum = sum % 10
    print(sum)
    if sum == 0:
        return 0
    else:
        return 1


def validate(checksum, number):
    if checksum == 1:
        print("INVALID")
    else:
        if len(number) is [13, 15, 16]:
            firstdigit = int(number[0])
            seconddigit = int(number[1])
            # Check if AMEX card
            elif firstdigit == 3 and seconddigit == 4 or seconddigit == 7:
                print("AMEX")
            # Check if Mastercard
            elif firstdigit == 5 and seconddigit is [1, 2, 3, 4, 5]:
                print("MASTERCARD")
            # Check if VISA
            elif firstdigit == 4:
                print("VISA")
            else:
                print("INVALID")
        else:
            print("INVALID")




main()

