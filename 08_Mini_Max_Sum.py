#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
arr.sort
length_of_array = len(arr)
max_total = 0
min_total = 0

for i in range(0,length_of_array - 1, 1 ):
    min_total = min_total + arr[i]
    
for j in range(1, length_of_array, 1):
    max_total = max_total + arr[j]
print(min_total, max_total )
