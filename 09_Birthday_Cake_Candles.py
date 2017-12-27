#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    
    max_length = len(ar)
    max_element = max(ar) 
    #print(ar)
    arr = []
    ar.sort()
    #print(ar)
    arr.append(ar.index(max_element))
    ctr = 0
    for i in range(arr[0], max_length, 1):
        #print(ar[i])
        if ar[i] == max_element:
            ctr = ctr + 1
        else:
            break
    #print(ctr)
    return(ctr)
    
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
