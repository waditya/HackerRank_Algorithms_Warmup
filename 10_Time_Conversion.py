#!/bin/python3

import sys

def timeConversion(s):
    ##print(s) ##-- Debug 
    var_am_pm = (s[-2:])
    time_string = s[:-2]
    hh = s[:2]
    mm = s[3:5]
    ss = s[6:8]
    
    if var_am_pm == 'AM':
        if hh == '12':
            time_string = time_string[2:]
            time_string='00'+ time_string
    else:
            time_string = time_string[2:]
            time_string = str((int(hh) + 12))+ time_string
    #print(time_string) ##-- Debug 
    return(time_string)

s = input().strip()
result = timeConversion(s)
print(result)
