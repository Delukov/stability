import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
from Classes import *
from main import *
global Part2
from Classes import *
# f = open(r'C:\Users\1\PycharmProjects\untitled4\read.txt', 'r')
#
# i = -1
# Part1 = []
# str = 'Long'
# for line in f:
#     if line.startswith(str):
#         i += 1
#         Part1.append(Part(line[7:]))
#     else:
#         Part1[i].add(line)
# # ВЫШЕ СЧИТЫВАНИЕ
# i = -1
# Part2 = []
# for ob in Part1:
#     i += 1
#     Part2.append(rab(ob.long))
#     Part2[i].addel(ob.points)
# # ВЫШЕ ПЕРЕВОД ИЗ 1ГО МАССИВА ВО 2Й
# Part2[1].pri()
# f.close()
# Part2 = parse('read.txt')
# fig = plt.figure()
# ax = fig.add_subplot()

def dd_plot():
    yy = []
    zz = []
    yyy = []
    zzz = []
    for part in Part2:
        y1 = min(part.y)
        yy.append(y1)
        zz.append(part.modz())
    for part in Part2:
        y2 = max(part.y)
        yyy.append(y2)
        zzz.append(part.modz())
    yyy.reverse()
    zzz.reverse()
    yyyy = yy + yyy
    zzzz = zz + zzz
    zzzz.append(Part2[0].modz())
    yyyy.append(min(Part2[0].y))
    return (zzzz,yyyy)


# line = ax.plot(zzzz, yyyy, '-', color='blue', linewidth=0.5)
# plt.show()
# b = []
# c = []
# for lin in Part2:
#     line = ax.plot(lin.x,lin.y,'-', color='blue', linewidth=0.5)
#     a = lin.x
#     for i in a:
#         i*=(-1)
#         b.append(i)
#     for i in lin.y:
#         c.append(i)
#     line = ax.plot(b,c,'-', color='blue', linewidth=0.5)
#     b= []
#     c= []