class Process:
    def __init__(self, pid, cycles = 100):
        '''
        Description: initializes pid and cycles given by user_input and link and previous to None 
        Parameters: pid and cycles
        '''
        self.cycles = cycles
        self.pid = pid
        self.link = None
        self.prev = None
        
    def __eq__(self, other):
        '''
        Description: Returns if self.pid == other.pid
        Return: True if self.pid = other.pid, or False if this condition is not true
        '''
        
        return self.pid == other.pid
       

    def __repr__(self):
        '''Return a string representation of the instance pid and cycles'''
        return f'Process({self.pid} {self.cycles})'