'''

Given the root of a binary tree, return the minimum depth of the binary tree. 
The minimum depth is the total number of nodes along the shortest path in binary tree from the root node down to the nearest leaf node.

Input:

				1
			  /   \
			/		\
		  /			  \
		 2			   3
	   /   \		 /   \
	  /		\		/	  \
	 4		 5	   6	   7
	  \		  \			  / \
	   \	   \		 /   \
		8		9		10	 11
		 \
		  \
		  12

Output: 3

Explanation: The shortest path is 1 —> 3 —> 6.

'''

class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.right = Node(8)
root.left.right.right = Node(9)
root.right.right.left = Node(10)
root.right.right.left = Node(11)
root.left.left.right.right = Node(12)

def findMinDepth(root):
    if root is None:
        return 0
    
    l = findMinDepth(root.left)
    r = findMinDepth(root.right)

    if root.left is None:
        print(f'val: {root.data} with left none')
        return 1 + r

    if root.right is None:
        return 1 + l
    
    print(f"l,r: {l},{r}")

    return min(l,r) + 1

print(findMinDepth(root))