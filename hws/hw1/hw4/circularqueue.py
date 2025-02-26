class CircularQueue:
    """A circular queue to allow us to run processes turn-by-turn"""
    def __init__(self, processes = None):
        '''
        Description: intializes head into None, len into zero, and creates a dictionary
        parameters: processes
        '''
        self._head = None
        self._len = 0
        self._d_processes = {}
        if processes is not None:
            for process in processes:
                self.add_process(process)

    def __len__(self):
        '''
        Description: length function
        Returns: self._len
        '''
        return self._len

    def __repr__(self):
        '''
        Description: returns a string representation of Circular Queue
        Returns: Circular Queue and contents
        '''
        if self._head is None:
            return "CircularQueue([])"
        process = []
        current = self._head
        for i in range(self._len):
            process.append(repr(current)) 
            current = current.link
        return "CircularQueue(" + ", ".join(process) + ")"
    
    def add_process(self, process):
        '''
        Description: Add processes to the dictionaries
        Parameters: process
        '''
        if self._len == 0:
            process.link = process.prev = process
            self._head = process
        
        else:
            save_prev = self._head.prev
            save_prev.link = process
            process.link = self._head
            process.prev = save_prev
            self._head.prev = process
        self._d_processes[process.pid] = process
        self._len += 1


    def remove_process(self, process):
        '''
        Description: Removes a process that you want to remove from the circular queue, given by user's input
        Parameters: process
        Returns: the process that is removed
        '''
        if self._len == 0:
            return None
        
        elif self._len == 1:
            store = self._head
            self._head = None
            self._len = 0
            self._d_processes.pop(process.pid)
            return store
        
        else:
            save_prev = process.prev
            save_next = process.link
            save_prev.link = save_next
            save_next.prev = save_prev
            process.prev = None
            process.link = None
            if process == self._head:
                self._head = save_next
            self._d_processes.pop(process.pid)
            self._len -= 1
            return process
            
    
    def kill(self, pid):
        '''
        Description: Removes and returns a process with the given pid
        parameters: PID
        Returns: the removed process
        '''
        process = self._d_processes[pid]
        return self.remove_process(process)
    
    

        
    
