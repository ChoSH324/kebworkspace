# Day02 assignment 3
# for 구문을 while 구문
# 구간 소수 잡는 걸 while 구문
# ** 대신 pow 함수

# First Assignment

def is_print_while(num):
    """
    Function to determine prime number using while statement
    input : int
    output : none
    """
    i=2
    if num==2:
        print(f"{num} is prime number")
    elif num>=2:
        while i<=(int(num**0.5)+1):
            if num % i==0:
                print(f"{num} is NOT prime number")
                break
            else:
                if i==(int(num**0.5)+1):
                    print(f"{num} is prime number")
                    break
                else:
                    i=i+1
    else:
        print(f"{num} is NOT prime number")
n = int(input("Input Number : "))
is_print_while(n)

# Second Assignment

numbers = input("Input first second number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1

number = n1
while number <= n2:
    is_prime = True

    if number < 2: # 소수 판별은 2이상부터 가능하므로
        number += 1
        continue

    i = 2
    while i < number:
        if number % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(number, end=' ')

    number += 1

#Third Assignment
import math
def is_prime(num) -> bool: # -> bool : type hint 라고 한다 반환 자료 타입을 명시해주는 것
    """
    A function that returns Ture if it is a prime number and False if it is not a prime number
    : param num : integer number
    : return : boolean type
    """
    if num>=2:
         for i in range(2,int(math.pow(num,0.5))+1,1):
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
