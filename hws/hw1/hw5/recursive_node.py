class Node:
    """Reucrsively implementes Linked List functionality"""
    def __init__(self, data, link=None):
        """Instantiates a new Node with given data"""
        self.data = data
        self.link = link

    def __repr__(self):
        """Returns string representation of node"""
        return f"Node({self.data})"
    
    def __len__(self):
        """Recursively calculates length of sublist starting at this node
        returns: len of sublist"""
        if self.link is None:
            return 1
        
        return 1 + len(self.link)

    def get_tail(self):
        '''
        Description: returns tail
        Returns: data at the tail
        '''
        if self.link is not None:
            return self.link.get_tail()
        else:
            return self.data
        

    
    def add_last(self, data):
        """
        Recursively adds to end of this sublist
        Parameters: data
        """
        if self is None:
            self = Node(data)

        if self.link is None:
            self.link = Node(data)
        
        else:
            self.link.add_last(data)
        
            

    def total(self):
        """Recusrively adds all items
        returns: the total sum of all the items in the linked list"""
        if self.link is None:
            return self.data
        else:
            return self.data + self.link.total()
        
    
    def remove_last(self):
        """Recursively removes last item in sublist
            Returns a tuple of (new_head, data). The new_head is the
            new head of this sublist after removing the tail.

            OUTPUT
            ------
            new_head, tail_data
                * new_head: Node or None
                    The new link for whatever node called this function
                
                * tail_data: Any
                    The data that was found in the tail node
        """

        if self.link is None:
            return None, self.data

        returned = self.link.remove_last()
        self.link = returned[0]
        return self, returned[1]

        
    
    def reverse(self, prev):
        """Recursively reverse list"""
        """Recursively reverses the linked list
        Outputs: the reversed list
        """
        if self.link is None:
            self.link = prev
            return self
        
        else:
            new_head = self.link.reverse(self)
            self.link = prev
            return new_head


        
        


        
