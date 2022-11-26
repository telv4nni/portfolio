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
            # Assign digit to check number
            num = int(creditnumber[i])
            if i % 2 == 0:
                # Multiply odd number by 2
                num = 2 * num
                # Check if multiplied number is greater than 10
                # Add odd number
                if num > 10:
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
                if num > 10:
                    sum += num // 10
                    sum += num % 10
                else:
                    sum += num
            else:
                # Add odd number
                sum =+ num

    print(num)
    print(sum)




main()

