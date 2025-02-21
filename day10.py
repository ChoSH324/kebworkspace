def bubble_sort_1(a_list):
    list_length = len(a_list) -1
    for i in range(list_length):
        for j in range(list_length):
            if a_list[j] > a_list [j+1]:
                a_list[j],a_list[j+1] = a_list[j+1], a_list[j]
    return a_list


def bubble_sort_2(a_list):
    list_length = len(a_list) -1
    for i in range(list_length):
        for j in range(list_length-i): # 맨 오른쪽에 큰 숫자를 뒀으니 왼쪽 정렬만 보겠다
            if a_list[j] > a_list [j+1]:
                a_list[j],a_list[j+1] = a_list[j+1], a_list[j]
    return a_list


def bubble_sort_3(a_list):
    list_length = len(a_list) -1
    for i in range(list_length):
        no_swaps = True
        for j in range(list_length-i): # 맨 오른쪽에 큰 숫자를 뒀으니 왼쪽 정렬만 보겠다
            if a_list[j] > a_list [j+1]:
                a_list[j],a_list[j+1] = a_list[j+1], a_list[j]
                no_swaps = False
    return a_list


list = [4, 6, 2, 8, 1, 20]
print(bubble_sort_1(list))
print(bubble_sort_2(list))
print(bubble_sort_3(list))