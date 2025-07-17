class TreeNode:
    def __init__(self, x):
        self.x = x
        self.L = None
        self.R = None

def height(root):
    if root is None:
        return -1  
    
    left_height = height(root.L)
    right_height = height(root.R)
    
    return max(left_height, right_height) + 1


def insert(root, x):
    if root is None:
        return TreeNode(x)
    if x < root.x:
        root.L = insert(root.L, x)
    else:
        root.R = insert(root.R, x)
    return root


values = [4, 2, 1, 3, 6, 7, 5]
root = None
for v in values:
    root = insert(root, v)


print("Height of the tree is:", height(root))
