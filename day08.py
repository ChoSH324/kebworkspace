class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def delete(parent, current, delete_data):
    if current is None:
        return False  # 삭제할 노드를 찾지 못함

    if delete_data < current.data:
        return delete(current, current.left, delete_data)  # 왼쪽 서브트리로 이동
    elif delete_data > current.data:
        return delete(current, current.right, delete_data)  # 오른쪽 서브트리로 이동
    else:  # 삭제할 노드를 찾음
        # Case 1: 자식 노드가 없는 경우
        if current.left is None and current.right is None:
            if parent:  # parent가 None이 아닌 경우에만 실행
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            return True
        # Case 2: 자식 노드가 하나인 경우
        elif current.left is None:
            if parent:
                if parent.left == current:
                    parent.left = current.right
                else:
                    parent.right = current.right
            return True
        elif current.right is None:
            if parent:
                if parent.left == current:
                    parent.left = current.left
                else:
                    parent.right = current.left
            return True
        # Case 3: 자식 노드가 두 개인 경우
        else:
            # 오른쪽 서브트리에서 가장 작은 값을 찾습니다.
            successor_parent, successor = find_min(current, current.right)
            # 삭제할 노드의 값을 successor의 값으로 변경합니다.
            current.data = successor.data

            # successor를 삭제합니다.
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
            return True


def find_min(parent, node):
    current = node
    while current.left is not None:
        parent = current
        current = current.left
    return parent, current


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9, 6, 2, 16]

    node = TreeNode()
    node.data = numbers[0]
    root = node

    for group in numbers[1:]:
        node = TreeNode()
        node.data = group
        current = root
        while True:
            if group < current.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left  # move
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right  # move

    print("BST 구성 완료")

    # 삭제 기능 테스트
    delete(None, root, 10)  # 루트 노드 삭제
    print("삭제 완료")


    # (optional) 삭제 후 트리가 정확한지 확인하기 위해 트리를 순회하는 함수를 추가할 수 있습니다.
