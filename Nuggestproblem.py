# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 13:39:55 2017

@author: JaceDonaldBroadbent
"""
def is_nugget_number(candidate):
    for a in range(0,candidate//6 + 1):
        for b in range (0,candidate//9 + 1):
            for c in range(0,candidate//20 + 1):
                if 6*a + 9*b + 20*c == candidate:
                    return True
    return False

def main():
    success = 0
    biggest = 0
    candidate = 6
    while success != 6:
        if(is_nugget_number(candidate)):
            success += 1
        else:
            success = 0
            biggest = candidate
        candidate += 1
    print("The highest number of nuggest you cannot buy is", biggest,)
    
main()