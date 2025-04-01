def solve_puzzle(L):
    """Returns _solve_puzzle given with parameter L"""
    return _solve_puzzle(L, idx=0, visited=set())
def _solve_puzzle(L, idx, visited):
    '''
    _solve_puzzle
    '''
    
    
    if idx == len(L) - 1:
        return True
    if idx in visited:
        return False
    
    visited.add(idx)
    cw = (idx+L[idx]) % len(L)
    ccw = (idx-L[idx]) % len(L)

    return  _solve_puzzle(L,cw, visited) or _solve_puzzle(L, ccw, visited)

