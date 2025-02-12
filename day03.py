import math

# Last Assignment
def my_pow(a,b):
    return a**b

def my_pow_Pro(b, e) -> float:
    """
    A user-defined function that receives a base and exponent and returns the power result in the form of a real number
    :param b: base number
    :param e: exponent
    :return: the power result in the form of a real number
    """
    result = 1
    i=int(e)
    f=e-i

    for _ in range(i): # for k in range(e):
        result = result * b
    if f > 0:
        result = result*math.exp(f*math.log(b))
    return result

# main
print(my_pow_Pro(2,9))
print(my_pow_Pro(3,4.5))
print(my_pow_Pro(25,0.5)) # ieee 754 규격 확인