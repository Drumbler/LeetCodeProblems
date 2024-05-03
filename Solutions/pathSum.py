class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst.pop(0))
    q = [root]
    while lst:
        node = q.pop(0)
        if lst:
            node.left = TreeNode(lst.pop(0))
            q.append(node.left)
        if lst:
            node.right = TreeNode(lst.pop(0))
            q.append(node.right)
    return root


from typing import Optional

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def has_sum(root: Optional[TreeNode], cur_sum: int) -> bool:
            if not root:
                return False
            if root.val is not None:
                cur_sum += root.val
            if not (root.left or root.right):
                return cur_sum == targetSum
            return has_sum(root.left, cur_sum) or has_sum(root.right, cur_sum)
        return has_sum(root, 0) 


root = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
s = Solution()
print(s.hasPathSum(root, 27))
