#!/usr/bin/python3

import math
import itertools

class Point:
    def __init__(self,a):
        self.x = int(a.split()[0])
        self.y = int(a.split()[1])

with open("kolmsis.txt") as f:
    N = int(f.readline())
    pts = list(map(Point, f.read().strip().split('\n')))

count = 0
cosines = set()
# c^2 = a^2 + b^2 - 2ab*cos alfa
# 2ab*cos alfa = a^2+b^2-c^2
# cos alfa = (a^2+b^2-c^2)/(2*a*b)
for A,B,C in itertools.combinations(pts, 3):
    a2 = (B.x-C.x)**2 + (B.y-C.y)**2
    b2 = (A.x-C.x)**2 + (A.y-C.y)**2
    c2 = (A.x-B.x)**2 + (A.y-B.y)**2
    if b2 + c2 <= a2:
        continue
    if a2 + b2 <= c2:
        continue
    if a2 + c2 <= b2:
        continue
    count += 1
    a2,b2,c2 = sorted([a2,b2,c2])
    cosines.add((a2,b2,c2))

open("kolmval.txt",'w').write(str(count)+"\n"+str(len(cosines)))

