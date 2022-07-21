import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from Classes import *
# from mpl_toolkits.mplot3d import Axes3D
# class Part(object):
#     def __init__(self, long, *points):
#         self.long = long
#         self.points = []
#         for a in points:
#             self.points.append(a)
#
#     def add(self, point):
#         self.points.append(point)


# 1Й КЛАСС ДЛЯ РАЗБИЕНИЯ ФАЙЛА
# class rab(object):
#     def __init__(self, ln):
#         self.ln = ln
#         self.x = []
#         self.y = []
#
#     def addel(self, lin):
#         for b in lin:
#             a = 0
#             b.strip()
#             i = b
#             while i[a] != ' ':
#                 a += 1
#             if i[a - 1] == 'S':
#                 ch = float(i[:(a - 1)])
#                 ch *= (-1)
#                 self.x.append(ch)
#
#             else:
#                 self.x.append(float(i[:(a - 1)]))
#             a += 3
#             if i[a] == '-':
#                 ch = float(i[(a + 1):])
#                 ch *= -1
#                 self.y.append(ch)
#             else:
#                 self.y.append(float(i[a:]))
#
#     def pri(self):
#         print(self.ln, self.x, self.y)
#
#     def modz(self):
#         a = self.ln
#         b = len(a)
#         if a[b - 2] == "F":
#             z = float(a[:(b - 2)])
#         else:
#             z = float(a[:(b - 2)])
#             z *= -1
#         return z
#
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
# fig = plt.figure(figsize=(30,20))
# ax = plt.axes(projection="3d")
# for poli in Part2:
#     for x in poli.x:
#             ax.scatter3D(poli.modz(), x, poli.y, color='green')

parse('read.txt')
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot()
b = []
c = []
for lin in Part2:
    line = ax.plot(lin.x, lin.y, '-', color='blue', linewidth=0.5)
    a = lin.x
    for i in a:
        i*=(-1)
        b.append(i)
    for i in lin.y:
        c.append(i)
    line = ax.plot(b, c, '-', color='blue', linewidth=0.5)
    b = []
    c = []
plt.show()

