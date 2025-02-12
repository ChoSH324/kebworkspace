import math

# Last Assignment
def my_pow(a,b):
    return a**b

def my_pow_pro(b, e) -> float:
    """
    A user-defined function that receives a base and exponent and returns the power result in the form of a real number
    :param b: base number
    :param e: exponent
    :return: the power result in the form of a real number
    """
    result = 1
    i=int(e)

    if e<0:
        f = e - i
        for _ in range(i):  # for k in range(e):
            result = result * b
        if f > 0:
            result = result * math.exp(f * math.log(b))
    elif e<0:
        f = -(e - i)
        for _ in range(-i):  # for k in range(e):
            result = result * b
        if f > 0:
            result = result * math.exp(f * math.log(b))
        result = 1 / result
    else:
        result = 1

    return result

# main
print(my_pow_pro(2,9))
print(my_pow_pro(25,0.5)) # ieee 754 규격 확인
print(my_pow_pro(2,-2.2))
print(my_pow_pro(2,0))