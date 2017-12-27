#!/bin/python3

import sys
arr = []

n = int(input().strip())
for i in range(0, n, 1):
    for j in range(0, n - 1 -i , 1):
        print(end = ' ')
    for k in range(0, i+1 , 1):
        print('#', end = '')
    print()
