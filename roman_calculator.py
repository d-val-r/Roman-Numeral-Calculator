KEY = { # create a dictionary to hold numeric
'I': 1, # values for the Roman numerals
'V': 5,
'X': 10,
'L': 50,
'C': 100,
'D': 500,
'M': 1000,
}

KEY2 = {
    '+': 'sum',
    '-': 'difference',
    '*': 'product',
    '/': 'quotient',
    '%': 'integer remainder'
    }

lis = ['I', 'V', 'X', 'L', 'C', 'D', 'M'] # a list of Roman numerals in the SAME ORDER as the KEY dict 

def convertToNum(romNum): # fuction to conver Roman numerals to numeric values
    num = 0 # will hold the final number
    for i in range(len(romNum)):
        if (romNum[i] != romNum[-1]): # XIV
            if (KEY[romNum[i]] < KEY[romNum[i+1]]): # if the numeric value of the current
                # Roman numeral is less than the one after it, such as in IV,
                # add the value of the second value minus the first (V - I) to num
                # and then subtract the second value, since the next iteration
                # of the loop will add it right back; all the algebra for this
                # loop will look like this:
                # V - I - V + V = IV, (5 - 1 - 5 + 5 = 4), with the + 5 occuring
                # on the next iteration of the loop
                num += (KEY[romNum[i+1]] - KEY[romNum[i]] - KEY[romNum[i+1]])

            else:
                num += KEY[romNum[i]]
        else:
            num += KEY[romNum[i]]
    return num

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2 # add the returned values of
        # the conversion function with the two user-defined values passed in
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2 # THIS HAS TO BE THE INT DIVISION AND REMAINDER - NEED TO DEBUG
    elif operator == '%':
        return num1 % num2
    elif operator == '//':
        return num1 // num2


def intToRom(num):
    if (num != 0):
        romNum = ''
        while (num % 1000 >= 0 and num >= 1000):
            num -= 1000
            romNum += 'M'
        while (num % 500 >= 0 and num >= 500):
            num -= 500
            romNum += 'D'
        while (num % 100 >= 0 and num >= 100):
            num -= 100
            romNum += 'C'
        while (num % 50 >= 0 and num >= 50):
            num -= 50
            romNum += 'L'
        while (num % 10 >= 0 and num >= 10):
            num -= 10
            romNum += 'X'
        while (num % 5 >= 0 and num >= 5):
            num -= 5
            romNum += 'V'
        while (num // 1 > 0 and num >= 1):
            num -= 1
            romNum += 'I'
        for i in range(len(romNum)): #LXXXXVIIII
            if (i in range(len(romNum)) and romNum[i] != 'M'):
                if (i < (len(romNum)-3) and romNum[i] == romNum[i+1] and romNum[i] == romNum[i+2] and romNum[i] == romNum[i+3]):
                    for h in range(len(lis)): # XXXXIIII
                        if (lis[h] == romNum[i]):
                            temp = romNum
                            romNum = ''
                            romNum += temp[0:i]#, lis[h+1], temp[i+4:]
                            romNum += '{}{}'.format(temp[i], lis[h+1])
                            romNum += temp[i+4:]
        temp = ''
        for i in range(len(romNum)): #LXLVIV, MMMMMIX
            if (i in range(len(romNum)) and romNum[i] != 'M'):
                if (i < (len(romNum) - 2) and romNum[i] == romNum[i+2]) and romNum[i] != romNum[i+1]:
                    temp = romNum
                    romNum = ''
                    romNum += temp[0:i]#, temp[i+1], lis[lis.index(temp[i])+1]
                    romNum += "{}{}".format(temp[i+1], lis[lis.index(temp[i])+1])
                    romNum += temp[i+3:]
                   
        return romNum
    else:
        return 0

def main():
    equation = input("Enter a Roman Numeral, a space, your desired operation (+, -, *, /, or %),\na space, and then another Roman Numeral: ")
    equation = equation.split()
    result = (calculate(convertToNum(equation[0]), equation[1], convertToNum(equation[2])))
    print("{}".format(intToRom(result)))
main()
