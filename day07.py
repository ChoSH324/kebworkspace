class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class LinkdedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if not self.head:
            self.head=Node(data)
            return
        current = self.head
        while current.next:
            current=current.next
        current.next=Node(data)
        if not self.head:
            self.head=Node(data)
            return

    def __str__(self):
        node = self.head
        while node is not None:
            print(node.data)
            node=node.next
        return print("end")

if __name__ == "__main__":
    l = LinkdedList()
    l.append(7)
    l.append(-11)
    l.append(4)
    l.__str__()