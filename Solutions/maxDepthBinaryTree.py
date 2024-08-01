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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ldepth = self.maxDepth(root.left)
        rdepth = self.maxDepth(root.right)
        return max(ldepth, rdepth) + 1


root = build_tree([3, 9, 20, None, None, 15, 7])
s = solution()
print(s.maxDepth(root))
