import time
# decorator
def description(f):  # closure
    def inner(*args):
        print(f.__name__)
        print(f.__doc__)
        r = f(*args)
        return r

    return inner


def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'실행시간 : {e - s}초')
        return r
    return wrapper

#@time_decorator
#@description
def squares(n):
    """
    제곱 함수
    """
    return n * n



f1 = squares(2)
f2 = description(time_decorator(squares))
print(f1)
print(f2(3))
# squares(4)가 먼저 진행하여 time_decorator의 인자로 16을 주므로 의도되로 진행X
print(description(time_decorator(squares(4))))
# 2중 데코레이터 적용 가장 쉬운 방법
@time_decorator
@description  # 데코레이터를 쓰는 순서로도 차이를 보인다
# description 함수 호출에 대한 걸 마지막에 씌워야 한다
def squares1(n):
    """
    제곱 함수
    """
    return n * n

print(squares1(5))