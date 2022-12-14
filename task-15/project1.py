#!/bin/python3

import sys

numbers=[]
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    numbers.append(n)

list1=[]
for number in numbers:
    list1=[]
    for i in range(1,number):
        if(i%3==0 or i%5==0):
            list1.append(i)
    print(sum(list1))