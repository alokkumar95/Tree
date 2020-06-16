# Tree
All Questions Related to Tree Data structure. Their detailed Explanations and Python implementation as well

# All Bst questions file name would be  Prefixed with Bst_
For example.

Search in a Binary search  Tree.
So, file name would be bst_Search_in_Binary_Tree.py

# Basic Implementation of Binary Search Tree Given Below, You can use this in every questions Related to BST


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
    
    """ Main function """
    arr=[5,4,9,2,8,10]
    bst=BST(arr)
    print("Inorder traversal of BST")
    inorder(bst.root)
