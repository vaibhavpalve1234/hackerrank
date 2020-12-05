#!/bin/python3

import math
import os
import random
import re
import sys 

# Complete the anagram function below.
def anagram(s):
    s1 = list(s[:len(s)//2])
    s2 = list(s[len(s)//2:])
    count = 0
    if len(s) % 2 != 0:
        return -1
    for char in s1:
        if char in s2:
            s2.remove(char)
        else:
            count += 1
    return count

    # l=len(s)
    # d,z=0,0
    # b=s[:l//2]
    # c=s[l//2:]
    # for i in b:
    #     for j in c:
    #         if i == j:
    #             d+=1
    #         else :
    #             z+=1
    #     if d < 0:
    #         return -1
    # return z-d
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()