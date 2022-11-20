#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    #başlagiçta maximum ve minimum recorları 0 dan eşit halde başlıyor
    maximum = scores[0]
    minimum = scores[0]

    # scor sayilarının tutulması için değişkenler ihtiyacımız var 
    maxscore = 0
    minscore = 0
 
    # Maria kendi recorlarının tutuldugu bir tablo hazırlıyor.En düşük ve En yüksek recorlarını kac kez      tekrarladıgını bulan alogritma 
    
    for i in range(1, len(scores)):
        if scores[i] < minimum :
            minscore +=1
            # yeni minimum scor değeri
            minimum = scores[i]
        elif scores[i] > maximum:
            maxscore +=1
            # yeni maximum scor değeri
            maximum = scores[i]
        
    return  maxscore, minscore

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
