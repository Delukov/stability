from Classes import *
from main import *
import math
def calculate_vol():
    vo = []
    vol = 0
    for Poly in Part2:
        i = 0
        s = 0
        while i < (len(Poly.y) - 2):
            s += Poly.x[i] * Poly.y[i+1]
            i += 1
        s += Poly.x[i+1] * Poly.y[1]
     #   i -= 1
        while i > 1:
            s -= Poly.x[i] * Poly.y[i-1]
            i -= 1
        s -= Poly.x[1] * Poly.y[len(Poly.y) - 1]
        vo.append((math.fabs(s)))
    i = 0
    while i < len(vo) - 2:
        vol += (vo[i] + vo[i+1]) * (math.fabs(Part2[i].modz() - Part2[i+1].modz()))
        i += 1
    return (vol)