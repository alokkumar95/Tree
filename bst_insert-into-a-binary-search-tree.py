""" NOTE: You can use Basic Implementation of BST given in README.MD. Here just definition of function is given """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

""" fucntion to insert value in BST """

def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    if not root:
        root=TreeNode(val)
        return root
    
    prev_node=root
    curr_node=root
    
    while curr_node:
        prev_node=curr_node
        if curr_node.val>val:
            curr_node=curr_node.left
        else:
            curr_node=curr_node.right
            
    if prev_node.val>val:
        prev_node.left=TreeNode(val)
    else:
        prev_node.right=TreeNode(val)
    return root

print("Inorder Travsersal Before insertion")
inorder(bst.root)

root=insertIntoBST(bst.root,3)

print("\nInorder Traversal after insertion")
inorder(bst.root)

""" OUTPUT
Inorder Travsersal Before insertion
2 4 5 8 9 10 
Inorder Traversal after insertion
2 3 4 5 8 9 10 
"""
