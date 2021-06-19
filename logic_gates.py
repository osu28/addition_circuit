def AND(bit1, bit2):
    [bit1, bit2] = digitize(bit1, bit2)
    if bit1 and bit2:
        return True
    return False

def OR(bit1, bit2):
    [bit1, bit2] = digitize(bit1, bit2)
    if bit1 or bit2:
        return True
    return False

def NOT(bit1):
    if bit1 == 1 or bit1 == "1":
        bit1 = True
    if bit1 == 0 or bit1 == "0":
        bit1 = False
    return not bit1

def NAND(bit1, bit2):
    [bit1, bit2] = digitize(bit1, bit2)
    if bit1 and bit2:
        return False
    return True

def NOR(bit1, bit2):
    [bit1, bit2] = digitize(bit1, bit2)
    if bit1 or bit2:
        return False
    return True

def XOR(bit1, bit2):
    [bit1, bit2] = digitize(bit1, bit2)
    if bit1 or bit2:
        if bit1 and bit2:
            return False
        return True
    return False

def XNOR(bit1, bit2):
    [bit1, bit2] = digitize(bit1, bit2)
    if bit1 or bit2:
        if bit1 and bit2:
            return True
        return False
    return True

def digitize(bit1, bit2):
    if bit1 == 1 or bit1 == "1":
        bit1 = True
    if bit1 == 0 or bit1 == "0":
        bit1 = False
    if bit2 == 1 or bit2 == "1":
        bit2 = True
    if bit2 == 0 or bit2 == "0":
        bit2 = False
    return [bit1, bit2]