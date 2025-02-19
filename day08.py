class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def delete_node(root, delete_name):
    if root is None:
        return root

    current = root
    parent = None

    # 삭제할 노드 검색
    while current is not None and current.data != delete_name:
        parent = current
        if delete_name < current.data:
            current = current.left
        else:
            current = current.right

    # 삭제할 노드가 없는 경우
    if current is None:
        print(f"{delete_name} 없음")
        return root


    if current.left is None and current.right is None:
        if current == root:
            return None
        if parent.left == current:
            parent.left = None
        else:
            parent.right = None
        del current
        return root


    if current.left is None:
        if current == root:
            return current.right
        if parent.left == current:
            parent.left = current.right
        else:
            parent.right = current.right
        del current
        return root
    if current.right is None:
        if current == root:  # 루트 노드인 경우
            return current.left
        if parent.left == current:
            parent.left = current.left
        else:
            parent.right = current.left
        del current
        return root

    # 삭제할 노드가 두 개의 자식 노드를 가진 경우
    # 오른쪽 서브트리의 가장 작은 값(successor)을 찾습니다.
    successor = current.right
    successor_parent = current
    while successor.left is not None:
        successor_parent = successor
        successor = successor.left


    current.data = successor.data


    if successor_parent.left == successor:
        successor_parent.left = successor.right
    else:
        successor_parent.right = successor.right

    del successor
    return root


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    # BST 구성
    for num in numbers:
        node = TreeNode()
        node.data = num
        if root is None:
            root = node
        else:
            current = root
            while True:
                if num < current.data:
                    if current.left is None:
                        current.left = node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        break
                    current = current.right

    print("BST 구성 완료")

    # 노드 검색
    find_group = int(input("찾을 숫자 입력: "))

    current = root
    while True:
        if current is None:
            print(f"{find_group}이(가) 존재하지 않습니다")
            break
        if find_group == current.data:
            print(f"{find_group}을(를) 찾았습니다")
            break
        elif find_group < current.data:
            current = current.left
        else:
            current = current.right

    # 노드 삭제
    delete_name = int(input("삭제할 숫자 입력: "))
    root = delete_node(root, delete_name)

    print("삭제 완료")
