""" NOTE: You can use Basic Implementation of BST given in README.MD. Here just definition of function is given """
""" Although this question is related to #Binary tree,but bst is also a kind of #Binary Tree """

## Flatten Binary Tree to Linked List
def flatten(root: TreeNode) -> None:
    if not root:
        return None
    left=flatten(root.left)
    right=flatten(root.right)
    
    if left and right:
        curr=root.left
        while curr.right:
            curr=curr.right
        curr.right=right
    if left:    
        root.right=left
    root.left=None
    return root

flatten(bst.root)
inorder(bst.root)

""" OUTPUT
5 4 2 3 9 8 10 
"""
