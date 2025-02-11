# 주석 처리 단축키 Ctrl + "/" (풀 때도 동일하게)

# 구구단
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

# 소수 찾기
# n = int(input("Input Number : "))
# count =0
# for i in range(1,n+1,1):
#     if n % i ==0:
#         count=count+1
# if count ==2:
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is NOT prime number")

# 조금 더 최적화
n = int(input("Input Number : "))
is_prime = True

if n>=2:
    for i in range(2,n,1):
        if n % i ==0:
            is_prime=False
            break
else:
    is_prime =False
if is_prime:
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number")