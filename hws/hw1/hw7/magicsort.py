from enum import Enum
import math

class MagicCase(Enum):
    SORTED = 0
    REVERSE_SORTED = 1
    CONSTANT_INVERSIONS = 2
    GENERAL = 3

INVERSION_BOUND = 10

def linear_scan(list):
    count = 0
    for i in range(len(list) - 1):
        if list[i] > list[i+1]:
            count += 1

    if count == len(list) - 1:
        return MagicCase.REVERSE_SORTED
    
    if count == 0:
        return MagicCase.SORTED
    
    if count <= INVERSION_BOUND:
        return MagicCase.CONSTANT_INVERSIONS
    
    return MagicCase.GENERAL

def reverse_list(list):
    n = len(list)
    for i in range(n // 2):
        list[n-1-i], list[i] =  list[i], list[n-1-i]
    return list


def magic_insertionsort(L, left, right, alg_set=None):
    for i in range(left + 1, right):
        for j in range(i, left, -1):
            if L[j] < L[j-1]:
                L[j], L[j-1] = L[j-1], L[j]
        


def magic_mergesort(L, left, right, alg_set=None):
    if right - left <= 20:
        magic_insertionsort(L, left, right)
        return
    
    mid = (left+right)//2
    magic_mergesort(L, left, mid)
    magic_mergesort(L, mid + 1, right)
    merge(L, left, mid, right)
    

def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]  # Copy left half
    right_part = arr[mid + 1:right + 1]  # Copy right half

    i = j = 0  # Pointers for left and right parts
    k = left  # Pointer for main array

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):  # Copy remaining elements from left_part
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

   

def magic_quicksort(L, left, right, depth=0, alg_set=None):
    
    if right - left <= 20:
        magic_insertionsort(L, left, right)
        return
    
    depth += 1

    if (depth > 3 * math.log2(len(L))):
        magic_mergesort(L, left, right)
        return
    
    pivot_index = partition(L, left, right)
    magic_quicksort(L, left, pivot_index)
    magic_quicksort(L, pivot_index + 1, right)
   
def partition(L, left, right):
    '''
        quick sort oartition function alg
        Parameters: list to sort, left index and right index
        Returns: None
    '''
    pivot = L[right - 1]
    i = left - 1
    for j in range(left, right - 1):
        if L[j] < pivot:
            i = i +1
            L[i], L[j] = L[j], L[i]
    
    L[i + 1], L[right - 1] = L[right - 1], L[i+1]
    return i + 1


def magicsort(L):
    '''
        magic_sort alg
        Parameters: list to sort
        Returns: None
    '''
    scan_result = linear_scan(L)

    if scan_result == MagicCase.SORTED:
        return
    elif scan_result == MagicCase.REVERSE_SORTED:
        reverse_list(L)
    elif scan_result == MagicCase.CONSTANT_INVERSIONS:
        magic_insertionsort(L, 0, len(L))
    else:
        magic_quicksort(L, 0, len(L))


