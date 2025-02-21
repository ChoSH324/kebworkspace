n, k = map(int, input().split())

list_1 = [i + 1 for i in range(n)]
list_2 = [0] * n  # 0은 생존, 1은 제거

current = 0  # 현재 위치
count = 0  # 제거된 사람 수

print('<', end='')
for _ in range(n):  # n명이 모두 제거될 때까지 반복
    inner_count = 0  # k번째 사람을 세기 위한 카운트
    i = 0
    while inner_count < k:
        index = (current + i) % n  # 현재 위치에서 탐색 시작
        if list_2[index] == 0:  # 아직 제거되지 않은 사람인 경우
            inner_count += 1
        i += 1

    list_2[index] = 1  # 제거 표시
    print(list_1[index], end='')  # list_1에서 값을 바로 출력
    if count < n - 1:
        print(', ', end='')  # 마지막이 아니면 쉼표 출력
    current = (index + 1) % n  # 다음 시작 위치 업데이트
    count += 1  # 제거된 사람 수 증가

print('>')
