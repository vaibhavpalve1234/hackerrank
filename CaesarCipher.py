
import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(string, k):
    alphabet_low = ['a', 'b', 'c', 'd', 'e', 'f' ,'g',
                    'h', 'i', 'j', 'k', 'l', 'm', 'n',
                    'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z']
    alphabet_big = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                    'H', 'I', 'J', 'K', 'L', 'M', 'N',
                    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                    'V', 'W', 'X', 'Y', 'Z']
    chars = list(string)
    output_string = ''
    for char in chars:
        if char in alphabet_low:
            index = alphabet_low.index(char) + k
            n = len(alphabet_low)
            while index >= n:
                index -= n
            char = alphabet_low[index]
        elif char in alphabet_big:
            index = alphabet_big.index(char) + k
            n = len(alphabet_big)
            while index >= n:
                index -= n
            char = alphabet_big[index]
        output_string += char
    return output_string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()