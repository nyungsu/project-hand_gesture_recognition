# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1203, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 700))
        MainWindow.setMaximumSize(QtCore.QSize(10000, 100000))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 400))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("QLabel{\n"
"    font: 75 20pt \"Agency FB\";\n"
"    border-radius: 10px;\n"
"    background-color:rgb(98, 255, 0);\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("QLabel{\n"
"    font: 75 20pt \"Agency FB\";\n"
"    border-radius: 10px;\n"
"    background-color:rgb(98, 255, 0);\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.img_me = QtWidgets.QLabel(self.widget_3)
        self.img_me.setText("")
        self.img_me.setAlignment(QtCore.Qt.AlignCenter)
        self.img_me.setObjectName("img_me")
        self.gridLayout.addWidget(self.img_me, 1, 0, 1, 1)
        self.img_you = QtWidgets.QLabel(self.widget_3)
        self.img_you.setText("")
        self.img_you.setAlignment(QtCore.Qt.AlignCenter)
        self.img_you.setObjectName("img_you")
        self.gridLayout.addWidget(self.img_you, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 250))
        self.widget_4.setStyleSheet("QWidget{\n"
"    border: 2px solid rgb(0, 170, 0);\n"
"    border-radius: 4px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_start = QtWidgets.QPushButton(self.widget_4)
        self.btn_start.setObjectName("btn_start")
        self.verticalLayout_3.addWidget(self.btn_start)
        self.btn_stop = QtWidgets.QPushButton(self.widget_4)
        self.btn_stop.setObjectName("btn_stop")
        self.verticalLayout_3.addWidget(self.btn_stop)
        self.label = QtWidgets.QLabel(self.widget_4)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat with Snoopy"))
        self.label_4.setText(_translate("MainWindow", "YOU"))
        self.label_3.setText(_translate("MainWindow", "SNOOPY"))
        self.btn_start.setText(_translate("MainWindow", "start"))
        self.btn_stop.setText(_translate("MainWindow", "stop"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>안녕! 나는 스누피야 </p><p>나랑 대화하고 싶다면 나를 불러줘 </p><p>우리 같이 가위바위보 할까?</p><p>(chatscript 받아오기)</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())