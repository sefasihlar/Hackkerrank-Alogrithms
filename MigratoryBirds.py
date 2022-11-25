#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# verilen dizi icersinde en cok tekrar eden sayilar arasindan en kucuk olani bulan algoritma

def migratoryBirds(arr):
    # Write your code here
    liste2=[]

    listeTekrar =[]

    for deger in arr:
        
        if deger not in liste2:
            liste2.append(deger)
        else:
            listeTekrar.append(deger)
            
    return max(set(listeTekrar), key=listeTekrar.count)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
