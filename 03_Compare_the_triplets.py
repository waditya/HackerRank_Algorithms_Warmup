#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    alice_point = 0
    bob_point = 0
    dummy = 0
    arr = []
    
    ##Computation for problem clarity
    if a0 - b0 > 0:
        alice_point = alice_point + 1
    elif a0 < b0 :
        bob_point = bob_point + 1
    else:
        dummy = 0
        
    ##Computation for Originality
    if a1 - b1 > 0:
        alice_point = alice_point + 1
    elif a1 < b1 :
        bob_point = bob_point + 1
    else:
        dummy = 0
        
    ##Computation for Difficulty
    if a2 - b2 > 0:
        alice_point = alice_point + 1
    elif a2 < b2 :
        bob_point = bob_point + 1
    else:
        dummy = 0
    arr.append(alice_point)    
    arr.append(bob_point)
    return(arr)
    

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))


