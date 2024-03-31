

class BinarySearchTree:
    
    def __init__(self, value) -> None:
        self.value = value
        self.left = None 
        self.right = None 
        
    def insert_node(self, value):
        
        if value <= self.value and self.left:
            self.left.insert_node(value)
        elif value <= self.value:
            self.left = BinarySearchTree(value=value)
        elif value > self.value and self.right:
            self.right.insert_node(value)
        else:
            self.right = BinarySearchTree(value=value)
            
    
    def search_value(self, value):
        
        if value < self.value and self.left:
            self.left.search_value(value=value)
        if value > self.value and self.right:
            self.right.search_value(value=value)
            
        return value == self.value
    
    def clear_node(self):
        self.value = None 
        self.left = None 
        self.right = None
    
    
    def find_minimum(self):
        
        if self.left:
            return self.left.find_minimum()
        else:
            return self.value
        
        
    def remove_node(self, value, parent):
        
        if value < self.value and self.left:
            return self.left.remove_node(value, self)
        elif value < self.value:
            return False
        elif value > self.value and self.right:
            return self.right.remove_node(value, self)
        elif value > self.value:
            return False
        else:
            if self.left is None and self.right is None and self == parent.left:
                parent.left = None
                self.clear_node()
            elif self.left is None and self.right is None and self == parent.right:
                parent.right = None
                self.clear_node()
            elif self.left and self.right is None and self == parent.left:
                parent.left = self.left
                self.clear_node()
            elif self.left and self.right is None and self == parent.right:
                parent.right = self.left
                self.clear_node()
            elif self.right and self.left is None and self == parent.left:
                parent.left = self.right
                self.clear_node()
            elif self.right and self.left is None and self == parent.right:
                parent.right = self.right
                self.clear_node()
            else:
                self.value = self.right.find_minimum()
                self.right.remove_node(self.value, self)

            return True
        
    def in_order(self):
        
        if self.left:
            self.left.in_order()
        
        print(self.value)
        if self.right:
            self.right.in_order()
        
        
        
if __name__ == "__main__":
    bst = BinarySearchTree(15)
    bst.insert_node(10)
    bst.insert_node(8)
    bst.insert_node(12)
    bst.insert_node(20)
    bst.insert_node(17)
    bst.insert_node(25)
    bst.insert_node(19)
    
    print(bst.search_value(17))
    
    print(bst.remove_node(20, None))
    print(bst.find_minimum())
    bst.in_order()