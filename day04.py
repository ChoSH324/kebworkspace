# SOLID
# Open Closed Principle : 개방 폐쇄 원칙 (확장에는 열려 있고 수정에는 닫혀 있는 원칙)
def factorial_repetition(n) -> int:
    result=1
    for _ in range(2,n+1):
        result = result*_
    return result


number = int(input())
print(f"{number}! = {factorial_repetition(number)}")