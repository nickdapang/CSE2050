def trib(k):
    '''Helper function'''
    solved = {0:0, 1:0, 2:1}
    return _trib(k-1, solved)

def _trib(k, solved):
    '''
    Calculates the nth tribonotric number through recursion
    Returns: the sovled value
    Parameters: solved
    '''
    if k not in solved:
        solved[k] = _trib(k-1, solved) + _trib(k-2, solved) + _trib(k-3, solved)   
    
    return solved[k]




