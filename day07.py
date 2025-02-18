class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next


class Queue:
    def __init__(self):
        self.front=None
        self.rear = None
        self._size=0


    def enqueue(self,item):
        self._size+=1
        node = Node(item)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node


    def dequeue(self):
        if self.front is None:
            raise IndexError('pop from empty queue')
        self._size -= 1
        temp=self.front
        self.front=self.front.next
        if self.front is None:
            self.rear = None
        return temp.data


    def size(self):
        return self._size


if __name__ == "__main__":
    a = Queue()
    a.enqueue(5)
    a.enqueue(7)
    a.enqueue(1)
    print(a.size())
    print(a.dequeue())
