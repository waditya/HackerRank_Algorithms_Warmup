#!/bin/python3

import sys

def simpleArraySum(n, ar):
    total = 0
    for counter in range(0, n, 1):
        total = total + ar[counter]
    return total
    
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
