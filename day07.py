def is_queue_full():
    global rear, front, size, queue
    if (rear + 1) % size == front:
        return True
    else:
        return False


def is_queue_empty():
    global size, queue, front, rear
    if front == rear:
        return True
    else:
        return False


def en_queue(data):
    global size, queue, front, rear
    if is_queue_full():
        print("큐가 꽉 찼습니다.")
        return
    rear = (rear + 1) % size
    queue[rear] = data


def de_queue():
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    front = (front + 1) % size
    data = queue[front]
    queue[front] = None
    return data


def peek():
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    return queue[(front + 1) % size]


def print_queue():
    global size, queue, front, rear
    if is_queue_empty():
        print("큐: 비어 있음")
        return

    # 큐의 내용을 담을 리스트
    queue_contents = []

    # front 다음 위치부터 rear까지 순회하며 큐 내용을 리스트에 추가
    index = (front + 1) % size
    while index != (rear + 1) % size:
        queue_contents.append(queue[index])
        index = (index + 1) % size

    print("큐:", queue_contents)


size = int(input("큐의 크기를 입력 : "))+1
queue = [None for _ in range(size)]
front = rear = 0

if __name__ == "__main__":
    while True:
        menu = input("삽입(E)/삭제(D)/확인(P)/종료(X) : ")
        if menu == 'X' or menu == 'x':
            break
        elif menu == 'E' or menu == 'e':
            data = input("입력할 데이터 : ")
            en_queue(data)
            print_queue()  # 변경된 부분: print(queue) 대신 print_queue() 호출
        elif menu == 'D' or menu == 'd':
            print("삭제된 데이터 : ", de_queue())
            print_queue()  # 변경된 부분: print(queue) 대신 print_queue() 호출
        elif menu == 'P' or menu == 'p':
            print("확인된 데이터 : ", peek())
            print_queue()  # 변경된 부분: print(queue) 대신 print_queue() 호출
        else:
            print("입력이 잘못됨")
    print("프로그램 종료!")
