import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from first_window import *
from Classes import *
from vol_calc import *
from d2_add_cargo import dd_plot
import math
import numpy as np

def gidro_table():
    "1. Найти 2/3 высоты судна"
    "2. Найти 1/3, и в цикле до половины от 1/3 прибавлять осадку ~5 раз, записывая данные в массив т.о. - [осадка : объём или вес воды]"
    "3. скомпилить массив в таблицу и вывести"
    immers_arr = []
    y = 0
    AreaSum = 0
    for poly in Part2:
        if y < max(poly.y):
            y = max(poly.y)
    # print(y)
    y /= 3
    step = y / 6
    # print(y,step)
    for i in range(6):
        AreasSum = []
        for part in Part2:
            vol = 0
            IsEmpty = True
            AreaSum = 0
            xy = []
            for k in range(len(part.y)- 1):
                if (part.y[k] <= y):
                    xy.append((part.x[k], part.y[k]))
                    maxk = k
                    IsEmpty = False
            if IsEmpty == False:
                xy.append((((part.x[maxk]+(math.fabs(part.x[maxk] - part.x[maxk - 1])))/2), y))
            j = 0
            while j < len(xy)-2:
                AreaSum += xy[j][0]*xy[j+1][1]
                j += 1
            if len(xy) > 0:
                AreaSum += xy[len(xy)-1][0] * xy[0][1]
            while j > 1:
                AreaSum -= xy[j][0] * xy[j-1][1]
                j -= 1
            if len(xy) > 0:
                AreaSum -= xy[0][0] * xy[len(xy)-1][1]
            AreasSum.append(math.fabs(AreaSum))
        for l in range(len(AreasSum) - 2):
            vol += (AreasSum[l] + AreasSum[l+1])/2 * math.fabs((Part2[l].modz() - Part2[l+1].modz()))
        vol *= 1030
        vol /= 1000
        immers_arr.append((vol,y))
        y += step
    # print(immers_arr)
    return (immers_arr)


def recalc():
    """
    Пересчитать ЦТ судна, и вес
    :return:
    """
    some_ship_info.grav_centr[0] = (some_ship_info.grav_centr[0] * some_ship_info.weight + cargo_info.mass_center[0] * cargo_info.weight) / (some_ship_info.weight + cargo_info.weight)
    some_ship_info.grav_centr[1] = (some_ship_info.grav_centr[1] * some_ship_info.weight + cargo_info.mass_center[1] * cargo_info.weight) / (some_ship_info.weight + cargo_info.weight)
    some_ship_info.weight += cargo_info.weight
    print(some_ship_info.grav_centr[0],some_ship_info.grav_centr[1],"weight:",some_ship_info.weight)


def GetDraft():
# """aWEQEQWEQWEQWEQWEQWEEQWQEW"""
    immersion = gidro_table()
    immersion = immersion[0]
    idx = np.searchsorted(immersion, some_ship_info.weight)
    # idx = np.clip(idx, 1, len(immersion) - 1)
    # left = immersion[idx - 1]
    # right = immersion[idx]
    # idx -= some_ship_info.weight - left < right - some_ship_info.weight
    immersion = gidro_table()

    CurWeight = some_ship_info.weight / immersion[idx][0]
    print(CurWeight)
    print(immersion[idx][1],immersion[idx][0])
    CurWeight *= immersion[idx][1]
    print('GG')
    return (CurWeight)


def validation(vol):
    vali = False
    volum = calculate_vol()
    volum /= vol
    if ((volum > 0.94) and (volum < 1.053)):

        vali = True

    return vali


def get_file():

    # взяли ссылку на файл у пользователя
    PATH = QtWidgets.QFileDialog.getOpenFileName(parent=None)
    # Распарсили файл
    parse(PATH[0])


def get_proj():
    x,y = dd_plot()
    return x,y


# def file_miss():
#     er = file_er()

# def get_vol():
#     Dialog.close()
#     Dialog1 = QtWidgets.QDialog()
#     ui1 = Ui_Dialog1()
#     ui.setupUi(Dialog1)
#     Dialog1.show()


if __name__ == "__main__":

    # create App
    app = QtWidgets.QApplication(sys.argv)

    # init
    #Dialog = QtWidgets.QDialog()
    ui = Main_window()
    # ui1 = get_vol_window()

    # HOOK LOGIC
    # ui.toolButton.clicked.connect(get_file)
    # parse(file=path_name)


    # Main loop
    sys.exit(app.exec_())