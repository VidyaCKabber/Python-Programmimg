# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        # SOlution 1
        # def count(node):
        #     if node is None:
        #         return 0

        #     left_nodes = int(count(node.left))
        #     right_nodes = int(count(node.right))

        #     return 1 + left_nodes + right_nodes

        # return count(root)

        # SOlution 2
        stack = [root]
        count = 0

        while stack:

            if root is None:
                return 0

            curr_ele = stack.pop()
            count +=1

            if curr_ele:
                if curr_ele.left:
                    stack.append(curr_ele.left)
                if curr_ele.right:
                    stack.append(curr_ele.right)

        return count

# Complete BT -> All levels are full and last level is full from left to right
# Time complexity -> O(N) since we meet all nodes atmosts once
# Space complexity -> Since it's complete binary tree, space complexity is height of bt i.e log(N). Therefore, sc is O(log n) 
   # complete explanation : https://www.notion.so/Trees-10efabda534280a882a9d5f4cab1fefe


            
