from cs50 import get_int

while True:
    height = get_int("What's pyramid height? ")
    if height > 0 or height <= 8:
        break

for i in range(height):
        print("#")