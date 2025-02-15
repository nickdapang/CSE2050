import random
import time

def generate_lists(size):
    '''
    Generates two random lists absed on the user's input of size
    Parameters: size (int), used to determine the size of list1 and list2
    Returns: list1 and list2 that contain unique elements and 
    '''
    list1 = random.sample(range(size*2), size)
    list2 = random.sample(range(size*2), size)
    return list1, list2

def find_common(list1, list2):
              
    '''
    Description: A function that takes in two list and finds how many common elements between the two list
    Parameters: list1 and list2 (of equal length and each element is unique)
    Returns: count, the number of elements that are the same within the two list of input (list1 and list2)
    '''          
              #Costs:
    count = 0 # 1
    
    for i in range(len(list1)): # n*
        for j in range(len(list2)): # n*
            if list1[i] == list2[j]: # 3*
                count += 1 # 2
    return count # 1
                 # 1 + 6n^2 + 1 = 6n^2 + 2 = O(n^2)
            
def find_common_efficient(list1, list2):
    '''
    Description: A function that takes in two list that is more efficient (has a less running time then the other)
    and finds how many common elements between the two list
    Parameters: list1 and list2 (of equal length and each element is unique)
    Returns: count, the number of elements that are the same within the two list of input (list1 and list2)
    '''      
        # Costs:
    count = 0 # 1
    set1 = set(list1) # n
    for i in range(len(list2)): # n
        if list2[i] in set1: # 1
            count += 1 # 2
    return count # 1
                 # 1 + n + n * 1 * 2 + 1  = 3n + 2 = O(n)

def measure_time():
    '''
    Description: measures the amount of time find_common function and find_common_efficient take
    Parameters: none
    Returns: An organized table of the running time of the find_common and find_common functions with parameters of
    a changeable length of list1 and list2 (ranging from 10 to 20,000)
    '''
    list = []
    inputs = [10, 100, 1000, 10000, 20000]
    for i in inputs:
        lists = generate_lists(i)
        
        start = time.time()
        find_common(lists[0], lists[1])
        end = time.time()
        output = end - start

        start1 = time.time()
        find_common_efficient(lists[0], lists[1])
        end1 = time.time()
        output1 = end1 - start1

        list.append(tuple([i, output, output1]))

    print(' List Size         find_common Time  (s)    find_common_efficient Time (s)')
    print('----------   ----------------------------  ------------------------------------')
    for i in list:
        print(f'{i[0]:>10}' + f'{i[1]:>30}' + f'{i[2]:>30}')

if __name__ == "__main__":
    measure_time()


