# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ahshoe\Desktop\Pyslvs-PyQt5\core\panel\run_Triangle_Solver.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(488, 387)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.directionsTable = QtWidgets.QTableWidget(Form)
        self.directionsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.directionsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.directionsTable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.directionsTable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.directionsTable.setObjectName("directionsTable")
        self.directionsTable.setColumnCount(5)
        self.directionsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/TS.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.directionsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.directionsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.directionsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.directionsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.directionsTable.setHorizontalHeaderItem(4, item)
        self.directionsTable.horizontalHeader().setDefaultSectionSize(80)
        self.directionsTable.horizontalHeader().setMinimumSectionSize(80)
        self.horizontalLayout.addWidget(self.directionsTable)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.targetNum = QtWidgets.QLabel(Form)
        self.targetNum.setText("")
        self.targetNum.setObjectName("targetNum")
        self.horizontalLayout_3.addWidget(self.targetNum)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.pluse_PLAP = QtWidgets.QPushButton(Form)
        self.pluse_PLAP.setObjectName("pluse_PLAP")
        self.verticalLayout_2.addWidget(self.pluse_PLAP)
        self.pluse_PLLP = QtWidgets.QPushButton(Form)
        self.pluse_PLLP.setObjectName("pluse_PLLP")
        self.verticalLayout_2.addWidget(self.pluse_PLLP)
        self.pluse_PLPP = QtWidgets.QPushButton(Form)
        self.pluse_PLPP.setObjectName("pluse_PLPP")
        self.verticalLayout_2.addWidget(self.pluse_PLPP)
        self.remove_botton = QtWidgets.QPushButton(Form)
        self.remove_botton.setObjectName("remove_botton")
        self.verticalLayout_2.addWidget(self.remove_botton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.clear_botton = QtWidgets.QPushButton(Form)
        self.clear_botton.setObjectName("clear_botton")
        self.verticalLayout_2.addWidget(self.clear_botton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.Solve = QtWidgets.QPushButton(Form)
        self.Solve.setEnabled(False)
        self.Solve.setObjectName("Solve")
        self.horizontalLayout_2.addWidget(self.Solve)
        self.Merge = QtWidgets.QPushButton(Form)
        self.Merge.setEnabled(False)
        self.Merge.setObjectName("Merge")
        self.horizontalLayout_2.addWidget(self.Merge)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p>Use triangles to find the solution.</p></body></html>"))
        item = self.directionsTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Type"))
        item = self.directionsTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Result"))
        item = self.directionsTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "p1"))
        item = self.directionsTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "p2"))
        item = self.directionsTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Condition"))
        self.label_2.setText(_translate("Form", "Target(s):"))
        self.pluse_PLAP.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Point(A), Length(L0), Angle(β), Point(B)</span></p><p><img src=\":/icons/preview/PLAP.png\"/></p></body></html>"))
        self.pluse_PLAP.setText(_translate("Form", "+PLAP"))
        self.pluse_PLLP.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Point(A), Length(L0), Length(R0), Point(B)</span></p><p><img src=\":/icons/preview/PLLP.png\"/></p></body></html>"))
        self.pluse_PLLP.setText(_translate("Form", "+PLLP"))
        self.pluse_PLPP.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Point(A), Length(L0), Point(B), Point(C)</span></p><p><img src=\":/icons/preview/PLPP.png\"/></p></body></html>"))
        self.pluse_PLPP.setText(_translate("Form", "+PLPP"))
        self.remove_botton.setText(_translate("Form", "-"))
        self.clear_botton.setText(_translate("Form", "Clear"))
        self.Solve.setText(_translate("Form", "Solve"))
        self.Merge.setText(_translate("Form", "Merge"))

import icons_rc
import preview_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

