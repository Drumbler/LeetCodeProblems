from typing import Optional


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


class Solution:
    def is_symmetric(self, root: Optional[TreeNode]):
        def symmetric(left, rigth):
            if not left and not rigth:
                return True
            if (not left) ^ (not rigth):
                return False
            if left.val == rigth.val:
                left_branch = symmetric(left.left, rigth.right)
                rigth_branch = symmetric(left.right, rigth.left)
                return left_branch and rigth_branch
            return False
        return symmetric(root.left, root.right)


root = build_tree([1,2,2,None,3,None,3])
s = Solution()
print(s.is_symmetric(root))
