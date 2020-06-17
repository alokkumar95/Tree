""" NOTE: You can use Basic Implementation of BST given in README.MD. Here just definition of function is given """
""" Although this question is related to #Binary tree,but bst is also a kind of #Binary Tree """

## Postorder Traversal Iteratively
def postorderTraversal(root: TreeNode):
      final=[]
      stack=[]
      
      while 1:
          while root:
              final.append(root.val)
              stack.append(root)
              root=root.right

          if stack==[]:
              break
          root=stack.pop()
          root=root.left
      # print(final)
      return final[::-1]
      
## Postorder trversal iteratively
def postorderTraversal2(root:TreeNode,arr):
  if root:
    postorderTraversal2(root.left,arr)
    postorderTraversal2(root.right,arr)
    arr.append(root.val)

arr=[]
postorderTraversal2(bst.root,arr)
print("Postorder Traversal recursively=",arr)
print("Postorder traversal iteratively=",postorderTraversal(bst.root))

"""OUTPUT
Postorder Traversal recursively= [3, 2, 4, 8, 10, 9, 5]
Postorder traversal iteratively= [3, 2, 4, 8, 10, 9, 5]
"""
