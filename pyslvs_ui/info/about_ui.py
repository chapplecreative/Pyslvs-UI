# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyslvs_ui/info/about.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(586, 494)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_7.setContentsMargins(-1, 6, 6, 6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.iconLabel = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconLabel.sizePolicy().hasHeightForWidth())
        self.iconLabel.setSizePolicy(sizePolicy)
        self.iconLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.iconLabel.setObjectName("iconLabel")
        self.verticalLayout_2.addWidget(self.iconLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setText("")
        self.title_label.setObjectName("title_label")
        self.verticalLayout_3.addWidget(self.title_label)
        self.tab_widget = QtWidgets.QTabWidget(Dialog)
        self.tab_widget.setObjectName("tab_widget")
        self.AboutTab = QtWidgets.QWidget()
        self.AboutTab.setObjectName("AboutTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.AboutTab)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.description_text = QtWidgets.QTextBrowser(self.AboutTab)
        self.description_text.setObjectName("description_text")
        self.verticalLayout_4.addWidget(self.description_text)
        self.tab_widget.addTab(self.AboutTab, "")
        self.LicenseTab = QtWidgets.QWidget()
        self.LicenseTab.setObjectName("LicenseTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.LicenseTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.license_text = QtWidgets.QTextBrowser(self.LicenseTab)
        self.license_text.setObjectName("license_text")
        self.verticalLayout.addWidget(self.license_text)
        self.tab_widget.addTab(self.LicenseTab, "")
        self.VersionsTab = QtWidgets.QWidget()
        self.VersionsTab.setObjectName("VersionsTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.VersionsTab)
        self.verticalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.ver_text = QtWidgets.QTextBrowser(self.VersionsTab)
        self.ver_text.setObjectName("ver_text")
        self.verticalLayout_6.addWidget(self.ver_text)
        self.tab_widget.addTab(self.VersionsTab, "")
        self.ArgumentsTab = QtWidgets.QWidget()
        self.ArgumentsTab.setObjectName("ArgumentsTab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.ArgumentsTab)
        self.verticalLayout_9.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.args_text = QtWidgets.QTextBrowser(self.ArgumentsTab)
        self.args_text.setObjectName("args_text")
        self.verticalLayout_9.addWidget(self.args_text)
        self.tab_widget.addTab(self.ArgumentsTab, "")
        self.verticalLayout_3.addWidget(self.tab_widget)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.button_box = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_box.sizePolicy().hasHeightForWidth())
        self.button_box.setSizePolicy(sizePolicy)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.horizontalLayout_2.addWidget(self.button_box)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        self.tab_widget.setCurrentIndex(0)
        self.button_box.accepted.connect(Dialog.accept)
        self.button_box.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About Pyslvs"))
        self.iconLabel.setWhatsThis(_translate("Dialog", "Pyslvs Icon!"))
        self.iconLabel.setText(_translate("Dialog", "<html><head/><body><p><img width=\"80\" src=\":/icons/main.png\"/></p></body></html>"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.AboutTab), _translate("Dialog", "About"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.LicenseTab), _translate("Dialog", "LICENSE"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.VersionsTab), _translate("Dialog", "Versions"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.ArgumentsTab), _translate("Dialog", "Arguments"))
        self.button_box.setWhatsThis(_translate("Dialog", "Click to exit"))
from pyslvs_ui import icons_rc
