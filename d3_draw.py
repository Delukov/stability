# import pylab
from mpl_toolkits import mplot3d
import numpy as np
from Classes import *
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D




# f = open('read.txt', 'r')
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
# fig = pylab.figure()
# ax = fig.add_subplot(111, projection='3d')
# #Axes3D(fig)
#
# pylab.show()
Part2 = parse('read')
fig = plt.figure(figsize=(10, 8))
# ax = plt.axes(projection="3d")
ax = fig.add_subplot(111, projection='3d')
#     z_points = Part2[1].modz()
# for x in Part2[1].x:
#     for y in Part2[1].y:
# z_line = np.linspace(0, 15, 1000)
# x_line = np.cos(z_line)
# y_line = np.sin(z_line)
# ax.plot3D(x_line, y_line, z_line, 'gray')

# z_points = 15 * np.random.random(100)
# x_points = np.cos(z_points) + 0.1 * np.random.randn(100)
# y_points = np.sin(z_points) + 0.1 * np.random.randn(100)
# ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap='hsv');
# for poli in Part2:
#     i = 0
#     for x in poli.x:
#         ax.plot(x, poli.modz(), poli.y[i], color='blue')
#         # xx = x * -1
#         # ax.scatter3D(poli.y[i], poli.modz(), xx, color='blue')
#         i += 1
for pol in Part2:
    i = 0
    xx = []
    yy = []
    zz = []
    ix = []
    for x in pol.x:
        xx.append(x)
        yy.append(pol.y[i])
        zz.append(pol.modz())
        ix.append(-x)
        i += 1
    ax.plot(zz, xx, yy, color='blue', linewidth=1)
    ax.plot(zz, ix, yy, color='blue', linewidth=1)
    # for x in poli.x:
    #     xx = -x
    #     ax.scatter3D(poli.y[i], poli.modz(), xx, color='blue')
    #      i += 1
print(Part2[1].modz())

plt.show()
