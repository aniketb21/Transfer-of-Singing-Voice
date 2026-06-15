import os
import sys
import datetime

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont

import gui.mainwindow

if __name__ == '__main__':
    # Write console outputs to log file.
    __stderr__ = sys.stderr
    date_time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    folder = os.path.exists('log')
    if not folder: 
        os.makedirs('log')
    sys.stderr = open(f'log/log {date_time}.txt', 'w')
    
    app = QApplication(sys.argv)
    app.setApplicationName("Audio Slicer")
    app.setApplicationDisplayName("Audio Slicer")

    font = QFont('Microsoft YaHei UI')
    font.setPixelSize(12)
    app.setFont(font)

    window = gui.mainwindow.MainWindow()
    window.show()

    sys.exit(app.exec())
