#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
#print(a)  ##--Debug to check the matrix
sum_of_left_diagonal = 0
for i in range(0, n , 1):
    sum_of_left_diagonal = sum_of_left_diagonal + a[i][i]
sum_of_right_diagonal = 0
for j in range(0, n, 1):
    sum_of_right_diagonal = sum_of_right_diagonal + a[j][n-1-j]
diff = sum_of_left_diagonal - sum_of_right_diagonal
if(diff<0):
    diff = diff * -1
print(diff)
   
