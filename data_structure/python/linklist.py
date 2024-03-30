


class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insertBegin(self, item):
        new_node = Node(item=item)
        new_node.next = self.head
        self.head = new_node
        
    def insertEnd(self, item):
        new_node = Node(item=item)
        
        if self.head is not None: 
            self.head = new_node
            return None
        last = self.head 
        
        while (last.next):
            last = last.next
        
        
        last.next = new_node
        
    def insertAfter(self, prev_node, item):
        
        if prev_node is None: 
            print("The node is given must be in LinkList")
            return None 
        
        new_node = Node(item=item)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def deleteNode(self, position):
        if self.head is None:
            return None 
        
        temp  = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return None 
        
        for i in range(position - 1):
            temp = temp.next 
            if temp is None:
                break
        
        
        if temp is None:
            return None 
        if temp.next is None:
            return None

        
        next_temp = temp.next.next 
        
        temp.next = None
        
        temp.next = next_temp
        
    
    def search(self, key):
        current  = self.head
        
        while current.next is not None:
            if current.item  == key:
                return True
            
            current = current.next
            
        return False
    
    
    def sortLinkList(self, head):
        current = head 
        
        
        index = Node(item=None)
        
        if head is None:
            return None 
        else: 
            while current is not None: 
                index  = current.next 
                
                while index is not None:
                    if current.item > index.item :
                        current.item, index.item = index.item, current.item
                        
                    index = index.next 
                current =current.next
                
                
    def printLinkList(self):
        temp = self.head
        
        while (temp):
            print(str(temp.item) + "--> " )
            temp = temp.next
            

            
if __name__ == '__main__':

    llist = LinkedList()
    llist.insertBegin(1)
    llist.insertBegin(2)
    llist.insertBegin(3)
    llist.insertEnd(4)
    llist.insertAfter(llist.head.next, 5)

    print('linked list:')
    llist.printLinkList()

    print("\nAfter deleting an element:")
    llist.deleteNode(3)
    llist.printLinkList()

    print()
    item_to_find = 3
    if llist.search(item_to_find):
        print(str(item_to_find) + " is found")
    else:
        print(str(item_to_find) + " is not found")

    llist.sortLinkList(llist.head)
    print("Sorted List: ")
    llist.printLinkList()