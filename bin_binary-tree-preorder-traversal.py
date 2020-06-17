""" NOTE: You can use Basic Implementation of BST given in README.MD. Here just definition of function is given """
""" Although this question is related to #Binary tree,but bst is also a kind of #Binary Tree """
## Preorder traversal of a Binary tree iteratively
def preorderTraversal(root:TreeNode):
  final=[]
  stack=[]

  while 1:
    while root:
      final.append(root.val)
      stack.append(root)
      root=root.left
    if stack==[]:
      break
    root=stack.pop()
    root=root.right

  return final

## Preorder traversal of a Binary tree recursively
def preorderTraversal2(root:TreeNode,arr):
  if root:
    arr.append(root.val)
    preorderTraversal2(root.left,arr)
    preorderTraversal2(root.right,arr)

arr=[]
preorderTraversal2(bst.root,arr)
print("Preorder Traversal of a binary Tree recursiverly",arr)
print("Preorder Traversal of a binary Tree iteratively=",preorderTraversal(bst.root))
  
"""OUTPUT
Preorder Traversal of a binary Tree recursiverly [5, 4, 2, 3, 9, 8, 10]
Preorder Traversal of a binary Tree iteratively= [5, 4, 2, 3, 9, 8, 10]
"""
