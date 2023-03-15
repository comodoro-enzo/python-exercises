import random
import time

# 1) naive search
def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# 2) binary search (recursive)
def binary_search_recursive(l, target, low = None, high = None):
    # low es el índice del primer elem
    # high es el índice del último elem
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if low > high:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] > target:
        return binary_search_recursive(l, target, low, midpoint - 1)
    else:
        return binary_search_recursive(l, target, midpoint + 1, high)


# 3) binary search
def binary_search(l, target):

    infimo = 0
    supremo = len(l) - 1
    midpoint = (infimo + supremo) // 2

    while l[midpoint] !=  target:

        if infimo > supremo:
            return - 1

        if l[midpoint] > target:
            supremo = midpoint - 1
            midpoint = (infimo + supremo) // 2

        else:
            infimo = midpoint + 1
            midpoint = (infimo + supremo) // 2

    return midpoint

            

if __name__ == '__main__':

    # vamos a medir el tiempo promedio que tarda cada método en encontrar cada uno de los elem. de una lista

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-10*length, 10*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()        
    print(f"Naive search time: {(end - start) / length} seconds")
 
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()        
    print(f"Binary search time: {(end - start) / length} seconds")

    start = time.time()
    for target in sorted_list:
        binary_search_recursive(sorted_list, target)
    end = time.time()        
    print(f"Binary search (recursive) time: {(end - start) / length} seconds")