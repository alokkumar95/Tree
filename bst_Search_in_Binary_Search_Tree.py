#Definition of Binary tree Node

class TreeNode:
  def __init__(self,val,left=None,right=None):
    self.val=val
    self.right=right
    self.left=left

""" Construct a Binary serach tree using an array """
class BST:
  def __init__(self,arr=[]):
    self.root=None
    self.nodes=arr
    self.constructBST()

  def constructBST(self):
    arr=self.nodes
    if arr:
      self.root=TreeNode(arr[0])

      for i in range(1,len(arr)):
        item=arr[i]
        curr_node=self.root
        prev_node=self.root

        while curr_node:
          prev_node=curr_node
          if item > curr_node.val:
            curr_node=curr_node.right
          else:
            curr_node=curr_node.left
        
        if prev_node.val>item:
          prev_node.left=TreeNode(item)
        else:
          prev_node.right=TreeNode(item)

""" Inorder Travsersal to check BST is constructed well. it will print bst in incresing order """
def inorder(root):
  if root:
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)
 
""" Search in Binary Tree """
def searchBST(root: TreeNode, val: int) -> TreeNode:
    while root and root.val!=val:
        if val>root.val:
            root=root.right
        else:
            root=root.left
    if root:
        return root
    return None


## Main Function
arr=[5,4,9,2,8,10]
bst=BST(arr)
print("Inorder traversal of BST")
inorder(bst.root)
print("\nSearch in Binary Tree print the node",searchBST(bst.root,2))
print("Search in Binary Tree print val=",searchBST(bst.root,2).val)

"""
OUTPUT:
Inorder traversal of BST
2 4 5 8 9 10 
Search in Binary Tree print the node <__main__.TreeNode object at 0x7f741ab2fa90>
Search in Binary Tree print val= 2
"""


