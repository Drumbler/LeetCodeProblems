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


class solution(object):
    def sum_numbers(self, root: Optional[TreeNode]) -> int:
        def dfs_func(root, res):
            if not root:
                return 0
            res = res * 10 + root.val
            if not root.left and not root.right:
                return res
            return dfs_func(root.left, res) + dfs_func(root.right, res)
        return dfs_func(root, 0)


root = build_tree([4, 9, 0, 5, 1, 6, None, 6])
s = solution()
print(s.sum_numbers(root))
