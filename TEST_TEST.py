# import sys
from PyQt5 import QtCore, QtGui, QtWidgets
# from first_window import *
# from Classes import *
# from vol_calc import *
# from d2_add_cargo import dd_plot
# import math
# import numpy as np

# class last_proj(QMainWindow):
#     """вывод судна в проекции с боку, отображая точки ЦТ старую ,ЦТ новую, ЦМ груза, метацентр
#     """
#     def __init__(self):
#         super().__init__()
#         self.left = 750
#         self.top = 100
#         self.title = 'Вид на судно сбоку'
#         self.width = 800
#         self.height = 600
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#         button = QPushButton('Продолжить', self)
#         button.setToolTip('Закрыть форму')
#         button.move(500, 0)
#         button.resize(140, 100)
#         button.clicked.connect(self.cls)
#         self.DraftLabel = QtWidgets.QLabel(self)
#         # DraftLabel.resize(100,100)
#         # DraftLabel.move(500,200)
#         self.DraftLabel.setGeometry(QtCore.QRect(500,200,500,100))
#         self.Draft = 'Осадка:'
#         self.DraftLabel.setText(self.Draft)
#
#         self.show()
#
#     def cls(self):
#
#         self.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # mw = last_proj()
    # mw.show()
    # sys.exit(app.exec())
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Warning)


    msg.setWindowTitle("Информация")
    msg.setText("Privet")


    okButton = msg.addButton('Окей', QtWidgets.QMessageBox.AcceptRole)
    msg.addButton('Отмена', QtWidgets.QMessageBox.RejectRole)

    msg.exec()
    # if msg.clickedButton() == okButton:
    #     print("Yes")
    # else:
    #     print("No")
    # msg.setInformativeText("InformativeText")
    # msg.setDetailedText("DetailedText")    # msg.setIconPixmap(pixmap)  # Своя картинка