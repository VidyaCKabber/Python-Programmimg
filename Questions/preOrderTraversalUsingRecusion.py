class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

result = []
def preOrderTraversal(node):
    # NLR
    if node:
        result.append(node.data)
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(23)
root.right.left = TreeNode(9)
root.right.right = TreeNode(7)

root.left.left = TreeNode(25)
root.left.left.left = TreeNode(0)
root.left.right = TreeNode(8)


print(preOrderTraversal(root))
