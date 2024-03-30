
# in this video, I'm going to learn and code tree data structure
# stay focus and happy


# let's talk about tree: 
# a tree is a nonlinear hierarchical data structrure that consists of node connected by edges. 


# tree terminologies 
# Node

# A Node is an entity that contains a key or value and pointers to its child nodes
    # The last nodes of each path are called leaf nodes or external nodes that do not contain a link/edges/pointers to child nodes

# Edges
    # Edges is the link between any two nodes
# Root
    # is the topmost node of a tree 

# Height of a Node 
    # A height of a node is the number of edges from the node to deepest leaf
    
# Deep of a Node
    # the Deep of a node is the number of edges from root to the node 

# Height of the a tree
    # is the height of the root node of the depth ofo the deepest node. 
    

# Tree traversal 
# Traversal in tree means visiting every node in the tree. You might, for instance, want to add all values in the tree or find
# the largest one. For all the operations, you will need to visit each node of the tree. 
# There are three main traversal methods: In-order, Pre-order, Post-order

# In-order 
# First, visit all nodes in the left subtree.
# Then to the root node.
# Finally, visit all nodes in the right subtree.

# Pre-order
#1. Visit to root node. 
#2. Visit all the nodes in the left subtree. 
#3. Visit all the nodes in the right subtree.

#Post-order
# 1. Visit all the nodes in the left subtree
# 2. Visit all the nodes in the right subtree 
# 3. Visit to the root

# Let's Code together !

# First, we need to create a class Node with left, right and value attributes
class Node:
    def __init__(self, item) -> None:
        self.left = None 
        self.right = None 
        self.value = item
        
        
        
        
        
        
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.value) + "-->", end='')
        inorder(root.right)


def preorder(root):
    if root: 
        print(str(root.value) + "-->", end='')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.value) + "-->", end='')

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print(" In order Traversal ")
    inorder(root=root)
    
    print("\n Pre-order Traversal")
    preorder(root=root)
    
    print("\n Post order Traversal")
    postorder(root=root)
    
    
        
        
        
        
        
# #create a tree 
# class Tree:
#     def __init__(self) -> None:
#         self.root  = None
    
#     def add_note(self, value, side = 'left'):
#         node = Node(value)
#         self.root = node 
        
        
#     def inorder(self):