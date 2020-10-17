import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    if not s:
        return "Empty String"
    for i in range(len(s)-1):
        if i<len(s):
            if s[i]==s[i+1]:
                return superReducedString(s[:i]+s[i+2:])
    return s



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()