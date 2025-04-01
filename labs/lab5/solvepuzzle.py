def solve_puzzle(L):
    return _solve_puzzle(L, 0, set())
def _solve_puzzle(L, idx, visited):
    goal = L[len(L) - 1]
    
    if idx in visited:
        return False
    if idx == len(L) - 1:
        return True
    
    visited.add(idx)
    new_idx = (idx + L[idx]) % len(L)
    new2_idx = (idx - L[idx]) % len(L)
    return _solve_puzzle(L, new_idx, visited) or _solve_puzzle(L, new2_idx, visited)

