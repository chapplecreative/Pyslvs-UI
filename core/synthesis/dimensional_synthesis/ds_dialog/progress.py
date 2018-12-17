# -*- coding: utf-8 -*-

"""The progress dialog of dimensional synthesis algorithm."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2018"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from typing import List, Dict, Any
from core.QtModules import (
    QDialog,
    Qt,
    QTimer,
    pyqtSlot,
)
from .Ui_progress import Ui_Dialog
from .thread import WorkerThread
from .options import AlgorithmType


class ProgressDialog(QDialog, Ui_Dialog):

    """Progress dialog.

    + Batch execute function.
    + Interrupt function.
    """

    def __init__(
        self,
        type_num: AlgorithmType,
        mech_params: Dict[str, Any],
        setting: Dict[str, Any],
        parent
    ):
        """Input the algorithm settings."""
        super(ProgressDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.rejected.connect(self.__close_work)

        self.mechanisms: List[Dict[str, Any]] = []

        # Batch label.
        if 'maxGen' in setting:
            self.limit = setting['maxGen']
            if self.limit > 0:
                self.batch_label.setText(f"{self.limit} generation(s)")
            else:
                self.batch_label.setText('∞')
            self.limit_mode = 'maxGen'
        elif 'minFit' in setting:
            self.limit = setting['minFit']
            self.batch_label.setText(f"fitness less then {self.limit}")
            self.limit_mode = 'minFit'
        elif 'maxTime' in setting:
            self.limit = setting['maxTime']
            self.batch_label.setText(
                f"{self.limit // 3600:02d}:"
                f"{self.limit % 3600 // 60:02d}:"
                f"{self.limit % 3600 % 60:02d}"
            )
            self.limit_mode = 'maxTime'
        self.loopTime.setEnabled(self.limit > 0)

        # Timer.
        self.time = 0
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.__set_time)
        self.time_spend = 0.

        # Worker thread.
        self.work = WorkerThread(type_num, mech_params, setting)
        self.work.progress_update.connect(self.__set_progress)
        self.work.result.connect(self.__get_result)
        self.work.done.connect(self.__finish)

    @pyqtSlot(int, str)
    def __set_progress(self, progress: int, fitness: str):
        """Progress bar will always full."""
        value = progress + self.limit * self.work.currentLoop
        if self.limit_mode in {'minFit', 'maxTime'} or self.limit == 0:
            self.progressBar.setMaximum(value)
        self.progressBar.setValue(value)
        self.fitness_label.setText(fitness)

    @pyqtSlot()
    def __set_time(self):
        """Set time label."""
        self.time += 1
        self.time_label.setText(
            f"{self.time // 3600:02d}:"
            f"{self.time % 3600 // 60:02d}:"
            f"{self.time % 3600 % 60:02d}"
        )

    @pyqtSlot(name='on_start_button_clicked')
    def __start(self):
        """Start the process."""
        loop = self.loopTime.value()
        self.progressBar.setMaximum(self.limit * loop)
        if self.limit_mode in {'minFit', 'maxTime'} or self.limit == 0:
            # Progress bar will show generations instead of percent.
            self.progressBar.setFormat("%v generations")
        self.work.setLoop(loop)
        self.timer.start()
        self.work.start()
        self.start_button.setEnabled(False)
        self.loopTime.setEnabled(False)
        self.interrupt_button.setEnabled(True)

    @pyqtSlot(dict, float)
    def __get_result(
        self,
        mechanism: Dict[str, Any],
        time_spend: float
    ):
        """Get the result."""
        self.mechanisms.append(mechanism)
        self.time_spend += time_spend

    @pyqtSlot()
    def __finish(self):
        """Finish the process."""
        self.timer.stop()
        self.accept()

    @pyqtSlot(name='on_interrupt_button_clicked')
    def __interrupt(self):
        """Interrupt the process."""
        if self.work.isRunning():
            self.work.stop()
            print("The thread has been interrupted.")

    @pyqtSlot()
    def __close_work(self):
        """Close the thread."""
        if self.work.isRunning():
            self.work.stop()
            print("The thread has been canceled.")
