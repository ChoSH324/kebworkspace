
# Last Assignment
def my_pow(a,b):
    return a**b

def is_prime(num) -> bool: # -> bool : type hint 라고 한다 반환 자료 타입을 명시해주는 것
    """
    A function that returns Ture if it is a prime number and False if it is not a prime number
    : param num : integer number
    : return : boolean type
    """
    if num>=2:
         for i in range(2,int(my_pow(num,0.5))+1,1):
             if num % i == 0:
                return False
    else:
        return False
    return True
# main
n = int(input("Input Number : "))
if is_prime(n):
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number")
