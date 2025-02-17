def is_even(n) -> bool:
    """
    짝수 판정 함수
    :param n: int
    :return: 짝수면 True, 홀수면 False
    """
    return not n&1
a=int(input())
print(is_even(a))

# a=10 # 0000 1010
# b=11 # 0000 1011
# print(a & b) # AND 연산 --> 0000 1010
# print(a | b) # OR 연산 --> 0000 1011
# print(a ^ b) # BETA 연산 --> 0000 0001