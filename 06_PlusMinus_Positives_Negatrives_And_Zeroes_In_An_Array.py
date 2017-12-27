#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
count_of_positive = 0
count_of_negative = 0
count_of_zeroes = 0

for i in range(0, n, 1):
    if arr[i] > 0:
        count_of_positive = count_of_positive +1
    elif arr[i] < 0:
        count_of_negative = count_of_negative + 1
    else:
        count_of_zeroes = count_of_zeroes + 1
        
print(count_of_positive/n)   
print(count_of_negative/n)
print(count_of_zeroes/n)
