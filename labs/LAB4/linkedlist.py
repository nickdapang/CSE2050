
class Node:
    def __init__(self, item, link = None):
        '''
        Parameters: item and link
        Description: Initializes item and link

        '''
        self.item = item
        self.link = link

    def __repr__(self):
        '''
        Description: returns the string representation of the item
        returns: the string representation of self.item
        '''
        
        return str({Node(self.item)})

class LinkedList:

    def __init__(self, items = None):
        '''
        Desciption:
        Initializes the length
        of the linked list, the 
        head into none and the
        tail as none
        for each item in items,
        adds item to the linked list
        Parameters: items
        '''
        self._len = 0
        self._head = None
        self._tail = None
        
        if items != None:
            for item in items:
                self.add_last(item)
    
    def get_head(self):
        '''
        Description: returns the head of the linked list
        Returns: self._head, the head of the linked list
        '''
        if self._len >= 1:
            return self._head.item
        else:
            return None
    def get_tail(self):
        '''
        Description: returns the tail of the linked list
        Returns: self._tail, the tao; of the linked list
        '''
        if self._tail is None:
            return None
        else:
            return self._tail.item

    def add_first(self, item):
        '''
        Description: adds the node to the front of linkedlist with item
        Parameters: item
        '''
        
        self._len += 1
        node = Node(item)
        if self._tail is None:
            self._head = node
            self._tail = node

        else:    
            
            node.link = self._head
            self._head = node

    def add_last(self, item):
        '''
        Description: adds the node to the end of linkedlist with item
        Parameters: item
        '''
        self._len += 1
        node = Node(item)
        
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            self._tail.link = node
            self._tail = node

    def remove_first(self):
        '''
        removes last node from LinkedList and returns its item
        raises a RuntimeError if LinkedList is empty when called
        '''
        old = self.head.item
        try:
            self._head = self._head.link
        
        except:
            raise RuntimeError

        self._len -= 1
        return old
    
    def remove_last(self):
        '''
        removes last node from LinkedList and returns its item
        raises a RuntimeError if LinkedList is empty when called
        Returns: the tail you removed
        '''
       
        try:
            node = self._head
            prev = None
            old_tail = self._tail.item
            while node != self._tail:
                prev = node
                node = node.link

            if prev == None:
                self._head = self._tail = None
            else:
                prev.link = None
                self._tail = prev

            self._len -= 1            

            return old_tail
        
        except:
            raise RuntimeError 

    def __len__(self):
        '''
        returns length of the linked list
        '''
        return self._len

