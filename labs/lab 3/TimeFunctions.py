import time
def time_function(func, args, n_trial = 10):
    '''
    Description: This is a Time function, which returns the number of seconds to run funcs with arg
    Returns: num of seconds (int) to run func with args
    parameters: funcs, arguments, and the number of trials
    
    '''
    times = []
    for i in range(1,n_trial + 1):
        start = time.time()
        func(args)
        end = time.time()
        times.append(end - start)
    return min(times)

def time_function_flexible(f, args, n_trials=10):
    '''
    This function will calulclate the amount of time it takes a function to run with multiple arguments.
    It takes in the function, its arguments and the number of trials. 
    It will return the float value of the time it takes to run.
    '''
    times = []
    for i in range(1,n_trials + 1):
        start = time.time()
        f(*args)
        end = time.time()
        times.append(end - start)
    return float(min(times))

if __name__ == '__main__':
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)]
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))
