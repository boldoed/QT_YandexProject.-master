# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dania\OneDrive\Рабочий стол\QT_YandexProject\add_elem.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(501, 307)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Dialog.setPalette(palette)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.cat_edit = QtWidgets.QComboBox(Dialog)
        self.cat_edit.setObjectName("cat_edit")
        self.cat_edit.addItem("")
        self.cat_edit.addItem("")
        self.cat_edit.addItem("")
        self.cat_edit.addItem("")
        self.cat_edit.addItem("")
        self.cat_edit.addItem("")
        self.cat_edit.addItem("")
        self.cat_edit.addItem("")
        self.gridLayout.addWidget(self.cat_edit, 2, 1, 1, 1)
        self.cat_label = QtWidgets.QLabel(Dialog)
        self.cat_label.setObjectName("cat_label")
        self.gridLayout.addWidget(self.cat_label, 2, 0, 1, 1)
        self.date_label = QtWidgets.QLabel(Dialog)
        self.date_label.setObjectName("date_label")
        self.gridLayout.addWidget(self.date_label, 3, 0, 1, 1)
        self.date_edit = QtWidgets.QDateEdit(Dialog)
        self.date_edit.setObjectName("date_edit")
        self.gridLayout.addWidget(self.date_edit, 3, 1, 1, 1)
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.summa_label = QtWidgets.QLabel(Dialog)
        self.summa_label.setObjectName("summa_label")
        self.gridLayout.addWidget(self.summa_label, 1, 0, 1, 1)
        self.name_edit = QtWidgets.QLineEdit(Dialog)
        self.name_edit.setObjectName("name_edit")
        self.gridLayout.addWidget(self.name_edit, 0, 1, 1, 1)
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setObjectName("ok_btn")
        self.gridLayout.addWidget(self.ok_btn, 5, 0, 1, 1)
        self.summa_edit = QtWidgets.QSpinBox(Dialog)
        self.summa_edit.setMaximum(999999999)
        self.summa_edit.setObjectName("summa_edit")
        self.gridLayout.addWidget(self.summa_edit, 1, 1, 1, 1)
        self.cancel_btn = QtWidgets.QPushButton(Dialog)
        self.cancel_btn.setObjectName("cancel_btn")
        self.gridLayout.addWidget(self.cancel_btn, 6, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cat_edit.setItemText(0, _translate("Dialog", "Супермаркеты"))
        self.cat_edit.setItemText(1, _translate("Dialog", "Рестораны и кафе"))
        self.cat_edit.setItemText(2, _translate("Dialog", "Транспорт"))
        self.cat_edit.setItemText(3, _translate("Dialog", "Отдых и развлечения"))
        self.cat_edit.setItemText(4, _translate("Dialog", "Одежда и аксессуары"))
        self.cat_edit.setItemText(5, _translate("Dialog", "Здоровье и красота"))
        self.cat_edit.setItemText(6, _translate("Dialog", "Коммунальные платежи, связь, интернет"))
        self.cat_edit.setItemText(7, _translate("Dialog", "Другое"))
        self.cat_label.setText(_translate("Dialog", "Категория:"))
        self.date_label.setText(_translate("Dialog", "Дата:"))
        self.name_label.setText(_translate("Dialog", "Наименование:"))
        self.summa_label.setText(_translate("Dialog", "Сумма:"))
        self.ok_btn.setText(_translate("Dialog", "OK"))
        self.cancel_btn.setText(_translate("Dialog", "Назад"))
