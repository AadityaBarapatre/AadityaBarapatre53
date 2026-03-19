#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    total=0
    
    for i in range(len(arr)):
        total=total+arr[i]
        
    mini=arr[0]
    maxx=arr[0]    
    for i in range(len(arr)):
        if arr[i]<mini:
            mini=arr[i]
        if arr[i]>maxx:
            maxx=arr[i]

    min_sum=total-maxx
    max_sum=total-mini
    
    print(min_sum,max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
