import re
import sys

import numpy as np
from PySide6 import QtCore
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import Figure
from sympy import lambdify

import bisection

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(1334, 817)
        MainWindow.setCursor(QCursor(Qt.OpenHandCursor))
        MainWindow.setStyleSheet(u"background-color:#243340;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 290, 711, 441))
        self.tableWidget.viewport().setProperty("cursor", QCursor(Qt.OpenHandCursor))
        self.tableWidget.setStyleSheet(u"color:\"white\";\n"
"font-weight:bold;\n"
"font-size:14px;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(463, 80, 58, 16))
        self.label.setStyleSheet(u"color:\"white\";\n"
"font-weight:bold;\n"
"font-size:15px;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(720, 150, 191, 41))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"#pushButton{\n"
"border:none;\n"
"border-radius:15px;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0 y2:0, stop:0 #7036be , stop:1 #269ef1);\n"
"font-weight:bold;\n"
"color:#fff;\n"
"font-size:20px;\n"
"\n"
"}\n"
"#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0 y2:0, stop:0 #269ef1 , stop:1 #7036be);\n"
"\n"
"}")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(523, 80, 113, 21))
        self.lineEdit.setStyleSheet(u"border-color:#212554;\n"
"border-radius:10px;\n"
"color:\"white\";\n"
"border:2px solid white;\n"
"padding-left:5px;\n"
"font-weight:bold;")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(763, 80, 113, 21))
        self.lineEdit_2.setStyleSheet(u"border-color:#212554;\n"
"border-radius:10px;\n"
"border:2px solid white;\n"
"color:\"white\";\n"
"padding-left:5px;\n"
"font-weight:bold;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(703, 80, 58, 16))
        self.label_2.setStyleSheet(u"color:\"white\";\n"
"font-weight:bold;\n"
"font-size:15px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(313, 60, 101, 51))
        self.label_3.setStyleSheet(u"color:\"white\";\n"
"font-weight:bold;\n"
"font-size:15px;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(313, 160, 71, 20))
        self.label_4.setStyleSheet(u"color:\"white\";\n"
"font-weight:bold;\n"
"font-size:15px;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(380, 150, 21, 16))
        self.label_5.setStyleSheet(u"color:\"white\";\n"
"font-weight:bold;")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(523, 160, 113, 21))
        self.lineEdit_3.setStyleSheet(u"border-color:#212554;\n"
"border-radius:10px;\n"
"border:2px solid white;\n"
"color:\"white\";\n"
"padding-left:5px;\n"
"font-weight:bold;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(463, 160, 58, 16))
        self.label_6.setStyleSheet(u"color:\"white\";\n"
"font-weight:bold;\n"
"font-size:15px;")
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(623, 20, 113, 21))
        self.lineEdit_4.setStyleSheet(u"border-color:#212554;\n"
"border-radius:10px;\n"
"border:2px solid white;\n"
"color:\"white\";\n"
"padding-left:5px;\n"
"font-weight:bold;")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(440, 20, 161, 20))
        self.label_8.setStyleSheet(u"color:\"white\";\n"
"font-weight:bold;\n"
"font-size:15px;")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(750, 280, 571, 461))
        self.label_9.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0 y2:0, stop:0 #7036be , stop:1 #269ef1);")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 280, 731, 461))
        self.label_10.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1 y2:0, stop:0 #7036be , stop:1 #269ef1);")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(230, 430, 241, 131))
        self.label_12.setStyleSheet(u"font-size:100px;\n"
"font-weight:bold;\n"
"color:qlineargradient(spread:pad, x1:60, y1:95, x2:100 y2:1, stop:0 #7036be , stop:1 #269ef1);")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(759, 289, 551, 441))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setCursor(QCursor(Qt.OpenHandCursor))
        self.widget.setStyleSheet(u"background-size: cover;")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(180, 130, 241, 131))
        self.label_7.setStyleSheet(u"font-size:100px;\n"
"font-weight:bold;\n"
"color:qlineargradient(spread:pad, x1:50, y1:1, x2:0 y2:25, stop:0 #7036be , stop:1 #269ef1);")

        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.label_5.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.tableWidget.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lineEdit_3.raise_()
        self.label_6.raise_()
        self.lineEdit_4.raise_()
        self.label_8.raise_()
        self.label_12.raise_()
        self.verticalLayoutWidget.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"f(a)", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"f(b)", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"c", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"f(c)", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"iteration", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"a = ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.lineEdit_2.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"b = ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Itervals : (a,b)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"|a-b| < 10", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"-k", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"k = ", None))
        self.lineEdit_4.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Add Desire Function = ", None))
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Table", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"plot", None))
    # retranslateUi

        def onClicked():
            ''''TABLE'''
            self.label_12.lower()
            statement = self.lineEdit_4.text()
            if statement.__contains__("(" and ")"):
                    result = statement[statement.find("(")+1:statement.rfind(")")]
                    for extract in re.finditer('[a-zA-Z]', result):
                            result = extract[0]
                            break

            elif re.search('[a-zA-Z]', statement) is not None:
                for extract in re.finditer('[a-zA-Z]', statement):
                    result = extract[0]
                    break

            function = lambdify(result , statement,'numpy')

            a = int(self.lineEdit.text()) ; b = int(self.lineEdit_2.text());
            k = self.lineEdit_3.text()
            if k == "":
                k = 2
            array = bisection.bisection_method(function, a, b, 10**(-int(k)))
            print(array)
            print(array[1])
            self.tableWidget.setRowCount(len(array[1]))
            self.tableWidget.setColumnCount(max(len(arr) for arr in array[1]))
            for i, arr in enumerate(array[1]):
                for j, item in enumerate(arr):
                    new_item = QTableWidgetItem()
                    new_item.setText(str(item))
                    self.tableWidget.setItem(i, j, new_item)
            iteration_points = np.array(array[1])[:, [0, 2, 4]].reshape(-1)
            x_final = array[0]

            '''PLOT'''
            for i in reversed(range(self.verticalLayout.count())):
                    widget = self.verticalLayout.itemAt(i).widget()
                    if widget is not None:
                            widget.setParent(None)

            fig = Figure(figsize=(8,6))
            ax = fig.add_subplot()
            self.widget = FigureCanvas(fig)
            canvas = FigureCanvasQTAgg(fig)
            self.verticalLayout.addWidget(canvas)
            # generating an array of points around the obtained interval by a small tolerance
            x = np.linspace(min(iteration_points), max(iteration_points), 1000)
            y = function(x)
            # scatter plot
            abc_tuples = np.array(array[1])[:, [0, 2, 4]]
            colors = np.random.rand(len(abc_tuples), 3)

            for i, abc_tuple in enumerate(abc_tuples):
                    a, b, c = abc_tuple[0], abc_tuple[1], abc_tuple[2]
                    ax.scatter(c, function(c), color=colors[i], label=f'i={i}')

            ax.scatter(x_final, function(x_final), color='red', label='answer')

            ax.plot(x, y)
            ax.set_xlabel('x')
            ax.set_ylabel('f(x)')
            ax.set_title('Plot of f(x)')
            ax.legend()
            ax.grid(True)
            self.widget.draw()

        self.pushButton.clicked.connect(onClicked)


if __name__ == "__main__":
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec())

