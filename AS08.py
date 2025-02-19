class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None


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

    parent = None
    current = root


def delete(node,delete_data):
    parent = None
    current = root
    # 루트에서 없어지지 않는다면
    if current.left is None and current.right is None:
       if parent.right == current.data:
             parent.right = None
          else:
             parent.left = None

        # 자식 노드가 왼쪽에만 있는 경우
    elif current.left is not None and current.right is None:
        if parent.right == current.data:
            parent.right = current.left
          else:
               parent.left = current.left
    elif current.left is None and current.right is not None:
        if parent.right == current.data:
              parent.right = current.right
        else:
            parent.left = current.right
    else: