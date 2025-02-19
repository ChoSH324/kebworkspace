class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

node1 = TreeNode()
node1.data = 'hs'

node2 = TreeNode()
node2.data = 'sl'
node1.left = node2

node3 = TreeNode()
node3.data = 'mb'
node1.right = node3

node4 = TreeNode()
node4.data = 'hw'
node2.left = node4

node5 = TreeNode()
node5.data = 'zz'
node2.right = node5

node6 = TreeNode()
node6.data = 'sm'
node3.left = node6


def pre_order(node):
    """
    Preorder : Process --> Left --> Right
    :param node: tree node
    :return:
    """
    if node is None:
        return
    print(node.data,end = "-")
    pre_order(node.left)
    pre_order(node.right)


def post_order(node):
    """
    postorder : Left --> Right --> Process
    :param node:
    :return:
    """
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end = "-")


print("Preorder")
pre_order(node1)
print("\nPostorder:")
post_order(node1)