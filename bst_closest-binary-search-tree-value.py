""" NOTE: You can use Basic Implementation of BST given in README.MD. Here just definition of function is given """

""" Given a non-empty Binary search tree and a target value, find the value in BST that is closest to the target """

def closestValue(root, target):
    diff=float('inf')
    new=None
    while root:
        sub=abs(target-root.val)
        if sub <diff:
            diff=sub
            new=root.val
            
        if target > root.val:
            root=root.right
        else:
            root=root.left

                
    return new

closestvalue=closestValue(bst.root,6.124780)
print(closestvalue)

""" OUTPUT
5
"""
