#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:] == "PM":
        return str(12+int(s[0:2]))+s[2:-2] if s[0:2] != "12" else s[0:-2]
    return "00"+s[2:-2] if s[0:2] == "12" else s[0:-2]
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
