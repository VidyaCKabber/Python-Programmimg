class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

result = []
def inorderTraversal(node):
    if node:
        inorderTraversal(node.left)
        result.append(node.data)
        inorderTraversal(node.right)
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(23)
root.left.left = TreeNode(25)
root.left.right = TreeNode(8)


print(inorderTraversal(root))
