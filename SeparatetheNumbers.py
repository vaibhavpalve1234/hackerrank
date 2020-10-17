#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
import sys
def separateNumbers(s):
  
    if len(s) == 1:
            print("NO")
            return
    else:
        # Half iter no need to go further
        for i in range(1,len(s)//2 + 1):
            new_str = s[:i]
            prev_str = int(new_str)
            while len(new_str) < len(s):
                str1 = prev_str + 1
                new_str = new_str + str(str1)
                prev_str = str1
            if new_str == s:
                print("YES",s[:i])
                return 
        print("NO") 

    
if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)