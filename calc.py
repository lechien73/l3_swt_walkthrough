# Every function has an error, which will be uncovered by tests.
# add: does not check for integers, so will concatenate a string
# sub: a logic error - it divides rather than subtracts
# mul: only one parameter is checked to make sure it's an integer
# div: missing "not" means that it will only work with a float or string

def add(num1, num2):

    print(num1 + num2)

def sub(num1, num2):

    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("The calculator can only accept whole numbers")
    else:
        print(num1 / num2)

def mul(num1, num2):

    if not isinstance(num1, int):
        raise ValueError("The calculator can only accept whole numbers")
    else:
        print(num1 * num2)

def div(num1, num2):

    if isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("The calculator can only accept whole numbers")
    else:
        print(num1 / num2)
