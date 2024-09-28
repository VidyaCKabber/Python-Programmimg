class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(10)
root.left.right = TreeNode(5)
# root.right.left = TreeNode(81)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.left.right.right.left = TreeNode(8)


def inorderTraversal(node): # LNR
    if node:
        inorderTraversal(node.left)
        print(node.val, end=" ")
        inorderTraversal(node.right)
        
        
def preorderTraversal(node): # NLR
    if node:
        print(node.val, end=" ")
        inorderTraversal(node.left)
        inorderTraversal(node.right)
        

def postorderTraversal(node): # LRN
    if node:
        inorderTraversal(node.left)
        inorderTraversal(node.right)
        print(node.val, end=" ")
        
print(f"In-order ->")
inorderTraversal(root) # 10 4 2 6 5 8 7 1 3
print(f"\n\nPre-order ->")
preorderTraversal(root) # 1 10 4 2 6 5 8 7 3

print(f"\n\nPost-order ->")
postorderTraversal(root) # 10 4 2 6 5 8 7 3 1
        
        
