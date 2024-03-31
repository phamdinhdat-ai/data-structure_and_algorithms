



class BinaryTree:
    def __init__(self, value) -> None:
        self.left = None 
        self.right = None
        self.value = value
        
    def insert_left(self, value):
        if self.left is None:
            self.left = BinaryTree(value)
        else: 
            new_node = BinaryTree(value=value)
            new_node.left = self.left
            self.left = new_node
    
    
    def insert_right(self, value):
        if self.right is None: 
            self.right = BinaryTree(value=value)
        else:
            new_node = BinaryTree(value=value)
            new_node.right = self.right
            self.right = new_node
            
        
    def in_order(self):
        if self.left: 
            self.left.in_order()
        print(self.value)
        if self.right:
            self.right.in_order()
            
    def pre_order(self):
        print(self.value)
        
        if self.left:
            self.left.pre_order()
            
        if self.right:
            self.right.pre_order()
            
            
    def post_order(self):
        if self.left:
            self.left.post_order()
            
        if self.right:
            self.right.post_order()
        print(self.value)    
        
    
    def bfs(self):
        queue = list()
        
        queue.append(self)
        
        while len(queue) == 0:
            
            current_node = queue.pop(0)
            
            print(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            
            if current_node.right:
                queue.append(current_node.right)
# Now we have to think about tree traversal.

# We have two options here: Depth-First Search (DFS) and Breadth-First Search (BFS).

# DFS “is an algorithm for traversing or 
# searching tree data structure. One starts at the root and 
# explores as far as possible along each branch before backtracking.” — Wikipedia
# BFS “is an algorithm for traversing or 
# searching tree data structure. It starts at the tree root and 
# explores the neighbor nodes first, before moving to the next level neighbors.” — Wikipedia          
if __name__ == "__main__":
    a_node = BinaryTree('a')
    a_node.insert_left('b')
    a_node.insert_right('c')

    b_node = a_node.left
    b_node.insert_right('d')

    c_node = a_node.right
    c_node.insert_left('e')
    c_node.insert_right('f')

    d_node = b_node.right
    e_node = c_node.left
    f_node = c_node.right

    print(a_node.value) # a
    print(b_node.value) # b
    print(c_node.value) # c
    print(d_node.value) # d
    print(e_node.value) # e
    print(f_node.value) # f
    a_node.bfs()
    
    
    
    d = [1, 2, 3, 4]
    e  = d.pop(0)
    print(e)
    print(d)