# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("QMainWindow#MainWindow {\n"
"     background-image: url(\"C://Users//Franex//Desktop//fpl_tool//pics//background_premier_league.png\")\n"
"}\n"
"\n"
"\n"
"QMainWindow QPushButton{ \n"
"    background-color: red\n"
"}\n"
"\n"
"QMainWidnow QWidget {\n"
"    background-color: transparent\n"
"}\n"
"")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget {\n"
"     background-image: url(\"C://Users//Franex//Desktop//fpl_tool//pics//background_premier_league.png\")\n"
"}\n"
"\n"
"\n"
"QWidget QPushButton{ \n"
"    background-color: #505050;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.TeamDifficulty = QtWidgets.QPushButton(self.centralwidget)
        self.TeamDifficulty.setGeometry(QtCore.QRect(40, 140, 181, 51))
        self.TeamDifficulty.setObjectName("TeamDifficulty")
        self.scenes = QtWidgets.QStackedWidget(self.centralwidget)
        self.scenes.setGeometry(QtCore.QRect(239, 0, 761, 661))
        self.scenes.setObjectName("scenes")
        self.planner_page = QtWidgets.QWidget()
        self.planner_page.setStyleSheet("")
        self.planner_page.setObjectName("planner_page")
        self.scenes.addWidget(self.planner_page)
        self.team_difficulty_page = QtWidgets.QWidget()
        self.team_difficulty_page.setAutoFillBackground(False)
        self.team_difficulty_page.setObjectName("team_difficulty_page")
        self.difficulty_button_1 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_1.setGeometry(QtCore.QRect(130, 80, 161, 41))
        self.difficulty_button_1.setObjectName("difficulty_button_1")
        self.difficulty_button_2 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_2.setGeometry(QtCore.QRect(170, 130, 161, 41))
        self.difficulty_button_2.setObjectName("difficulty_button_2")
        self.difficulty_button_3 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_3.setGeometry(QtCore.QRect(130, 180, 161, 41))
        self.difficulty_button_3.setObjectName("difficulty_button_3")
        self.difficulty_button_4 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_4.setGeometry(QtCore.QRect(170, 230, 161, 41))
        self.difficulty_button_4.setObjectName("difficulty_button_4")
        self.difficulty_button_5 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_5.setGeometry(QtCore.QRect(130, 280, 161, 41))
        self.difficulty_button_5.setObjectName("difficulty_button_5")
        self.difficulty_button_6 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_6.setGeometry(QtCore.QRect(170, 330, 161, 41))
        self.difficulty_button_6.setObjectName("difficulty_button_6")
        self.difficulty_button_7 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_7.setGeometry(QtCore.QRect(130, 380, 161, 41))
        self.difficulty_button_7.setObjectName("difficulty_button_7")
        self.difficulty_button_8 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_8.setGeometry(QtCore.QRect(170, 430, 161, 41))
        self.difficulty_button_8.setObjectName("difficulty_button_8")
        self.difficulty_button_9 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_9.setGeometry(QtCore.QRect(130, 480, 161, 41))
        self.difficulty_button_9.setObjectName("difficulty_button_9")
        self.difficulty_button_10 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_10.setGeometry(QtCore.QRect(170, 530, 161, 41))
        self.difficulty_button_10.setObjectName("difficulty_button_10")
        self.difficulty_button_15 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_15.setGeometry(QtCore.QRect(450, 280, 161, 41))
        self.difficulty_button_15.setObjectName("difficulty_button_15")
        self.difficulty_button_11 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_11.setGeometry(QtCore.QRect(450, 80, 161, 41))
        self.difficulty_button_11.setObjectName("difficulty_button_11")
        self.difficulty_button_12 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_12.setGeometry(QtCore.QRect(490, 130, 161, 41))
        self.difficulty_button_12.setObjectName("difficulty_button_12")
        self.difficulty_button_13 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_13.setGeometry(QtCore.QRect(450, 180, 161, 41))
        self.difficulty_button_13.setObjectName("difficulty_button_13")
        self.difficulty_button_14 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_14.setGeometry(QtCore.QRect(490, 230, 161, 41))
        self.difficulty_button_14.setObjectName("difficulty_button_14")
        self.difficulty_button_16 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_16.setGeometry(QtCore.QRect(490, 330, 161, 41))
        self.difficulty_button_16.setObjectName("difficulty_button_16")
        self.difficulty_button_17 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_17.setGeometry(QtCore.QRect(450, 380, 161, 41))
        self.difficulty_button_17.setObjectName("difficulty_button_17")
        self.difficulty_button_18 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_18.setGeometry(QtCore.QRect(490, 430, 161, 41))
        self.difficulty_button_18.setObjectName("difficulty_button_18")
        self.difficulty_button_19 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_19.setGeometry(QtCore.QRect(450, 480, 161, 41))
        self.difficulty_button_19.setObjectName("difficulty_button_19")
        self.difficulty_button_20 = QtWidgets.QPushButton(self.team_difficulty_page)
        self.difficulty_button_20.setGeometry(QtCore.QRect(490, 530, 161, 41))
        self.difficulty_button_20.setObjectName("difficulty_button_20")
        self.label = QtWidgets.QLabel(self.team_difficulty_page)
        self.label.setGeometry(QtCore.QRect(40, 70, 51, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logos/logo_1.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 51, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logos/logo_2.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 51, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("logos/logo_3.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_4.setGeometry(QtCore.QRect(80, 220, 51, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("logos/logo_4.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_5.setGeometry(QtCore.QRect(40, 270, 51, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("logos/logo_5.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_6.setGeometry(QtCore.QRect(80, 320, 51, 61))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("logos/logo_6.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_7.setGeometry(QtCore.QRect(40, 370, 51, 61))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("logos/logo_7.png"))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_8.setGeometry(QtCore.QRect(80, 420, 51, 61))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("logos/logo_8.png"))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_9.setGeometry(QtCore.QRect(40, 470, 51, 61))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("logos/logo_9.png"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_10.setGeometry(QtCore.QRect(80, 520, 51, 51))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("logos/logo_10.png"))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_11.setGeometry(QtCore.QRect(360, 70, 51, 61))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("logos/logo_11.png"))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_12.setGeometry(QtCore.QRect(400, 120, 51, 61))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("logos/logo_12.png"))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_13.setGeometry(QtCore.QRect(360, 170, 51, 61))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("logos/logo_13.png"))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_14.setGeometry(QtCore.QRect(400, 220, 51, 61))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("logos/logo_14.png"))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_15.setGeometry(QtCore.QRect(360, 270, 51, 61))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("logos/logo_15.png"))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_16.setGeometry(QtCore.QRect(400, 320, 51, 61))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("logos/logo_16.png"))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_17.setGeometry(QtCore.QRect(360, 370, 51, 61))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("logos/logo_17.png"))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_18.setGeometry(QtCore.QRect(400, 420, 51, 61))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("logos/logo_18.png"))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_19.setGeometry(QtCore.QRect(360, 470, 51, 61))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("logos/logo_19.png"))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.team_difficulty_page)
        self.label_20.setGeometry(QtCore.QRect(400, 520, 51, 61))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("logos/logo_20.png"))
        self.label_20.setObjectName("label_20")
        self.scenes.addWidget(self.team_difficulty_page)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.scenes.addWidget(self.page_5)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(0, 90, 51, 361))
        self.label_21.setStyleSheet("background-color: #505050")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.Planner = QtWidgets.QPushButton(self.centralwidget)
        self.Planner.setGeometry(QtCore.QRect(40, 90, 181, 51))
        self.Planner.setObjectName("Planner")
        self.TeamDifficulty.raise_()
        self.scenes.raise_()
        self.Planner.raise_()
        self.label_21.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.scenes.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TeamDifficulty.setText(_translate("MainWindow", "Team Difficulty"))
        self.difficulty_button_1.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_2.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_3.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_4.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_5.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_6.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_7.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_8.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_9.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_10.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_15.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_11.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_12.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_13.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_14.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_16.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_17.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_18.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_19.setText(_translate("MainWindow", "medium"))
        self.difficulty_button_20.setText(_translate("MainWindow", "medium"))
        self.Planner.setText(_translate("MainWindow", "Planner"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
