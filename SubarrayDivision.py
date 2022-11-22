#!/bin/python3

import math
import os
import random
import re
import sys

#bize verilen s dizisi içerisinden 
# d = dogum günü 
# m dogdugu ay
# pastadan kaç dilim alacagini belirlemek için - Dogdugu günün sayisini dogdugu ayın sayisi kadar        sıralı elamanın toplamından elde etmesi şartı verilmiş
# dongu dogdugu aydan dizinin büyük olması gerekiyor
# eğer 0.indisten başlayıp dogdugu aya kadarki elemanların toplamı doğdugu güne eşitse şart              sağlanmış oluyor ve toplamı 1 artırıyoruz
#yan yana olan elemanları bulmak için başlangıç değerini bir arttırıyoruz

 
def birthday(s, d, m):
    i  = 0
    count = 0
    while m <= len(s):
        if sum(s[i:m]) == d:
            count+=1
        i+=1
        m+=1
    return count
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
