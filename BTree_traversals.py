'''

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Input:
		   1
		 /   \
		/	  \
	   2	   3
	  /		  / \
	 /	  	 /	 \
	4		5	  6
		   / \
		  /   \
		 7	   8

Output: [4, 2, 1, 7, 5, 8, 3, 6]

'''
class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data = data	# data field
		self.left = left	# pointer to the left child
		self.right = right	# pointer to the right child

# inorder means left, root, right
# preorder means root, left, right
# postorder means left,right, root

def findInorderTraversal(root: Node) -> list[int]:
    keys_io = []
    def inorder(root):
        if root: 
            inorder(root.left)
            keys_io.append(root.data) 
            inorder(root.right)
    inorder(root)
    return keys_io 
    
BT = Node(1)
BT.left = Node(2)
BT.left.left = Node(4)
BT.right = Node(3)
BT.right.left = Node(5)
BT.right.left.left = Node(7)
BT.right.left.right = Node(8)
BT.right.right = Node(6)

print(findInorderTraversal(BT))