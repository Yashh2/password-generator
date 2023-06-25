import random

# default length of the password
characters = 4
numbers = 2
capitalChars = 2
spclChars = 1

# getting user input
print("CUSTOM LENGTH ? Type 'n' to get default length password")
totalLength = input("Enter length! ")

# if user choses "n", default values are used to generate the password
if totalLength == 'n':
    totalLength = characters + numbers + spclChars + capitalChars

# after the user has chosen a custom length, the password can be further customized by specifying
# the number of characters individually from the 4 available cateogries
else:
    totalLength = int(totalLength)

    # asking for further customization
    print("DO YOU WANT TO CUSTOMIZE PASSWORD?")
    customize = input("n for default values, any other char to enter custom values ")

    # if user decides to go only for the length, we use the default distribution of 50,20,20 and 10 % of the length
    if customize == 'n':
        characters = int(0.5*totalLength)
        numbers = int(0.2*totalLength)
        capitalChars = int(0.2*totalLength)
        spclChars = totalLength - (characters + numbers + capitalChars)

    # if the user wants custom lengths for each of the 4 catoegries, the earlier length is overwritten
    # new length is calculated
    else:
        print("Enter the no of english alphabets in the password, (a,b,c,d....) ")
        characters = int(input())

        print("Enter the no of numbers in the password, (0,1,2,3...) ")
        numbers = int(input())

        print("Enter the no of CAPITAL english alphabets, (A,B,C,D....) ")
        capitalChars = int(input())

        print("Enter the no of special characters in the passowrd, (@,#,$,%....) ")
        spclChars = int(input())

        totalLength = characters + numbers + spclChars + capitalChars

# displaying the password specifications to the user
print("You have chosen password of length", totalLength, "with", characters, "alphabets,", numbers, "numbers,",
      capitalChars, "CAPITAL chars and", spclChars, "special character.")

# genrating the password
password = ""

# all the available characters for the password
sampleSpace = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z'],
               [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
               ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z'],
               ['@', '#', '!', '%', '^', '&', '*', '$', ',', '.', '+', '<', '>', '?']
               ]


# looping until the desired password length isn't achieved

while len(password) != totalLength:
    n = -1
    typeOfChar = (random.randint(0, 3))

    if typeOfChar == 0 and characters != 0:
        characters -= 1
        n = len(sampleSpace[typeOfChar])
    elif typeOfChar == 1 and numbers != 0:
        numbers -= 1
        n = len(sampleSpace[typeOfChar])
    elif typeOfChar == 2 and capitalChars != 0:
        capitalChars -= 1
        n = len(sampleSpace[typeOfChar])
    elif typeOfChar == 3 and spclChars != 0:
        spclChars -= 1
        n = len(sampleSpace[typeOfChar])

    if n != -1:
        choice = random.randint(0, n)
        password += str(sampleSpace[typeOfChar][choice])

print(password)
