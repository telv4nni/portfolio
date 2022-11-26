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
            # Check if digit is odd
            if i % 2 == 0:
                #multiply odd number by 2
                num = 2 * int(creditnumber[i])
                # Check if multiplied number is greater than 10
                if num > 10:
                    # Add odd number
                    sum += num // 10
                    sum += num % 10
            else:
                #add even number
                sum += num


    print(sum)




main()

