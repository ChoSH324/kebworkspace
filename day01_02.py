# 주석 처리 단축키 Ctrl + "/" (풀 때도 동일하게)

""" 구구단 """
# for dan in range(2,10,1):
#     for i in range(1,10,1):
#         print(f"{dan} x {i} = {dan*i}")

# for dan in range(2,10):
#     for i in range(1,10,1):
#         print(f"{dan} x {i} = {dan*i}")

# for dan in range(2,10): # 증가량 안 쓰면 1씩 증가
#     for i in range(10): # 0부터 시작
#         print(f"{dan} x {i} = {dan*i}")

# dan = int(input("Input dan : "))
# for i in range(1,10,1):
#     print(f"{dan}*{i}={dan*i}")

""" 소수 판정 """
# n = int(input("Input Number : "))
# count =0
# for i in range(1,n+1,1):
#     if n % i ==0:
#         count=count+1
# if count ==2:
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is NOT prime number")

""" 소수 판정 조금 최적화 """
# n = int(input("Input Number : "))
# is_prime = True
#
# if n>=2:
#     for i in range(2,n,1):
#         print(i, end=' ')
#         if n % i ==0:
#
#             is_prime=False
#             break
# else:
#     is_prime =False
# if is_prime:
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is NOT prime number")

""" 소수 판정 최적화 """
# import math as m
# n = int(input("Input Number : "))
# is_prime = True
#
# if n>=2:
#     for i in range(2,int(n**0.5)+1,1): # for i in range(2, ,int(m.sqrt(n))+1,1):
#         print(i, end=' ')
#         if n % i ==0:
#             is_prime=False
#             break
# else:
#     is_prime =False
# if is_prime:
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is NOT prime number")

""" 소수 판정 함수화 """
# def is_prime(num) -> bool: # -> bool : type hint 라고 한다 반환 자료 타입을 명시해주는 것
#     """
#     A function that returns Ture if it is a prime number and False if it is not a prime number
#     : param num : integer number
#     : return : boolean type
#     """
#     if num>=2:
#          for i in range(2,int(num**0.5)+1,1):
#              if num % i ==0:
#                 return False
#     else:
#         return False
#     return True
#
# # main
# n = int(input("Input Number : "))
# if is_prime(n):
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is NOT prime number")

#help(is_prime)

# univ = "Inha university"
# print(univ)
# print(univ[5])
# # univ[5] = 'U'  # immutable
# # print(univ)
# subjects = ['python', 'c++', 'linux', 'data structure', 'database']
# print(subjects)
# print(subjects[3])
# subjects[3] = 'data structure & algorithm'  # mutable
# print(subjects)

# print(0.1)
# print(1e-1)
# print(0.01)
# print(1e-2)
# print(314.1592)
# print(0.3141592e3)
# print(21000)
# print(21_000)