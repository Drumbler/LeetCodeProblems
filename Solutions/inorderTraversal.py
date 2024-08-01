from typing import List, Optional


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


res = []


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if root == None:
        return
    inorderTraversal(root.left)
    res.append(root.val)
    inorderTraversal(root.right)
    return res
    
    


head = build_tree([100, 8, None, -83, None, 48, None, 72, None, -4])
#   [97, 78, 32, 80, 79, 29, -29, None, 45, None, -20,
#       None, -20, 13, None, 97, -41, -100, 94, None]
#   [73, -55, 76, None, 71, -71, 72, None, -63, None, -34, None, -9, None, -98, -19, -87, -83, 63, -70, None, 77, None, -36, None, -77, 6, None, 29, None])

print(inorderTraversal(head))
