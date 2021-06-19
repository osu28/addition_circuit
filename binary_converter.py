# Converts a decimal integer into binary integer form
# decimal -> binary
def binary(decimal):
    remainders = []

    quotient = int(decimal/2)
    remainders.append(decimal % 2)
    while quotient != 0:
        remainders.append(quotient % 2)
        quotient = int(quotient/2)

    binaryStr = ""
    for remainder in reversed(remainders):
        binaryStr += str(remainder)
    return int(binaryStr)

# Converts a binary integer into decimal integer form
# binary -> decimal
def decimal(binary):
    binaryList = list(str(binary))

    decimal = 0
    for k in range(len(binaryList)):
        bit = binaryList[k]
        exponent = len(binaryList) - k - 1
        decimal += int(bit) * 2**exponent
    return decimal

