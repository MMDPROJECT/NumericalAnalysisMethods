import sys
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
    QTableWidget, QTableWidgetItem, QWidget)
from PySide6.QtGui import QPainter, QLinearGradient, QColor
from PySide6.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
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
        self.tableWidget.setGeometry(QRect(50, 310, 701, 192))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 100, 58, 16))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(300, 220, 191, 41))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(250, 100, 113, 21))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(490, 100, 113, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(430, 100, 58, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 80, 91, 51))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 180, 61, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 170, 21, 16))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(250, 180, 113, 21))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(190, 180, 58, 16))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(427, 180, 161, 20))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(350, 40, 113, 21))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(197, 40, 151, 20))
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"result", None))
        self.lineEdit_2.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"b = ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Itervals : (a,b)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"|a-b| < 10", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"-k", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"k = ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Add 'k' as Maximum Error", None))
        self.lineEdit_4.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Add Desire Function = ", None))
    # retranslateUi
        def paintEvent(self, event):
            painter = QPainter(self)
            gradient = QLinearGradient(0, 0, 200, 200)
            gradient.setColorAt(0, QColor(Qt.white))
            gradient.setColorAt(1, QColor(Qt.blue))
            painter.setBrush(gradient)
            painter.drawRect(0, 0, 200, 200)


        def onClicked():

            statement = self.lineEdit_4.text()
            # print(statement)
            if statement in ['cos(x)', 'sin(x)', 'tan(x)', 'cot(x)']:
               statement = statement.replace(statement , "np."+statement)
            function = bisection.string_to_function(statement)
            self.lineEdit.setText(str(bisection.root_interval_finder(function)))
            array = bisection.bisection_method(function,*bisection.root_interval_finder(function), 10 ** (-50), 50)[1]
            self.tableWidget.setRowCount(len(array[0]))
            n=0
            for arr in array:
                for item in arr:
                    items = QTableWidgetItem()
                    self.tableWidget.setItem(0, n, items)
                    items.setText(str(item))
                    n = n + 1

            # self.tableWidget
        self.pushButton.clicked.connect(onClicked)


if __name__ == "__main__":
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec())

