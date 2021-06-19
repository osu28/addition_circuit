from logic_gates import *
from binary_converter import *
# This program will use binary addition to sum multiple bit numbers.
# Knowledge of binary addition circuits learned from: https://www.youtube.com/watch?v=wvJc9CZcvBc
# The Least Significant Bit will be a half adder while the More Significant
# Bits will be full adders which will take the carry of the previous adder.


def boolean_to_binary(boolean):
    if boolean:
        return 1
    return 0


def half_adder(a, b):
    sum = XOR(a, b)
    carry = AND(a, b)
    sum = boolean_to_binary(sum)
    carry = boolean_to_binary(carry)
    return [carry, sum]


def full_adder(a, b, c_input):
    [carry1, sum1] = half_adder(a, b)
    [carry2, sum2] = half_adder(sum1, c_input)
    c_out = boolean_to_binary(OR(carry1, carry2))
    return [c_out, sum2]


def addition(num1, num2):
    num1 = list(str(num1)[::-1])
    num2 = list(str(num2)[::-1])

    if len(num1) < len(num2):               # ensure binary forms of num1 and num2 are the same length
        difference = len(num2) - len(num1)
        for k in range(difference):
            num1.append("0")
    if len(num2) < len(num1):
        difference = len(num1) - len(num2)
        for k in range(difference):
            num2.append("0")

    count = 0
    new_num = []
    for a, b in zip(num1, num2):    # first set is always a half-adder and the remainders are full-adders
        if count == 0:
            [c_out, sum] = half_adder(a, b)
        else:
            [c_out, sum] = full_adder(a, b, c_out)
        new_num.append(sum)
        count += 1
    new_num.append(c_out)
    new_num = new_num[::-1]

    toRet = ""
    for num in new_num:
        toRet += str(num)
    return toRet


def start():
    num_system = input("type 'binary' or 'decimal': ")

    while num_system != "decimal" and num_system != "binary":
        print("please enter either 'binary' or 'decimal' as your number system")
        start()
    number1 = input("first number: ")
    number2 = input("second number: ")

    if num_system == "decimal":
        number1 = binary(int(number1))
        number2 = binary(int(number2))
        print(decimal(int(addition(number1, number2))))
    elif num_system == "binary":
        print(addition(number1, number2))


start()  # start the program here!

