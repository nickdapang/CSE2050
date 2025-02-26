'''
Task: Implement the add_first and remove_first functions inside the DoublyLinkedList class
'''

class DLLNode:
    def __init__(self, item, link, prev):
        """LL Nodes have an item and a link to the next node"""
		self.item = item
        self.link = link
        self.prev = prev

    def __repr__(self):
		"""String representation of an LLNode"""
		return f"DLLNode({self.item})"

class DoublyLinkedList:
	
    def __init__(self):
	    """Linked Lists have a head, a tail, and a length"""
        self._head = None
        self._tail = None
	    self._len = 0

	def __len__(self):
		"""Returns the number of nodes in the Doubly Linked List"""
		return self._len

	def __repr__(self):
		"""String representation of a DoublyLinkedList"""
		return f"DoublyLinkedList: head-->{self._head}, tail-->{self._tail}"

	def add_last(self, item):
		node = DLLNode(item, None, None)
		if len(self) == 0:
			self._tail = self._head = node
			self._len += 1
		else:
			node.prev = self._tail
			self._tail.link = node
			self._tail = node
			self._len +=1

		
	
    def reverse_linked_list(self):
        node = self._head
		saved_node = self._tail
		for i in range(len(self) - 1):
			future_head = self._head.link
			node.link = saved_node.link
			saved_node.link = node
			self._tail = node
			self._head = future_head
			node = self._head
    
			
	