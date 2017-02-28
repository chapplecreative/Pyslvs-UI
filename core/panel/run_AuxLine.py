# -*- coding: utf-8 -*-
from ..QtModules import *
from ..calculation.color import colorName
from .Ui_run_AuxLine import Ui_Form as AuxLine_Form

class AuxLine_show(QWidget, AuxLine_Form):
    Point_change = pyqtSignal(int, int, int, bool, bool, bool, bool, bool)
    def __init__(self, table, pt, color, limit_color, parent=None):
        super(AuxLine_show, self).__init__(parent)
        self.setupUi(self)
        re_Color = colorName()
        for i in range(table.rowCount()): self.Point.insertItem(i, QIcon(QPixmap(":/icons/point.png")), table.item(i, 0).text())
        for i in range(len(re_Color)): self.Color.insertItem(i, re_Color[i])
        for i in range(len(re_Color)): self.Color_l.insertItem(i, re_Color[i])
        self.Point.setCurrentIndex(pt)
        self.Color.setCurrentIndex(color)
        self.Color_l.setCurrentIndex(limit_color)
    
    @pyqtSlot(int)
    def on_Point_currentIndexChanged(self, index): self.Change_set(True)
    @pyqtSlot(int)
    def on_Color_currentIndexChanged(self, index): self.Change_set()
    @pyqtSlot()
    def on_H_line_clicked(self): self.Change_set()
    @pyqtSlot()
    def on_V_line_clicked(self): self.Change_set()
    @pyqtSlot()
    def on_Max_Limit_clicked(self): self.Change_set()
    @pyqtSlot()
    def on_Min_Limit_clicked(self): self.Change_set()
    @pyqtSlot(int)
    def on_Color_l_currentIndexChanged(self, index): self.Change_set()
    
    def Change_set(self, pt = False):
        self.Point_change.emit(
            self.Point.currentIndex(), self.Color.currentIndex(), self.Color_l.currentIndex(),
            self.H_line.checkState(), self.V_line.checkState(),
            self.Max_Limit.checkState(), self.Min_Limit.checkState(), pt)
