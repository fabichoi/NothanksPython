# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proto_nothanks_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import random
import sys, threading, time
from proto_nothanks import Board
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    b = Board()
    b.ready(6, 7, 6)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Player = [QtWidgets.QGroupBox(self.centralwidget) for _ in range(7)]
        self.Player[0].setVisible(False)
        self.n = [[QtWidgets.QLabel(self.Player[0]) for _ in range(36)]]
        # Player 설정
        pInitX,pInitY = 480,220
        sInitX,sInitY = 15,10
        limitX, limitY = 42, 60
        initX1, initY1 = 10, 20

        self.Player[1].setStyleSheet("background-color: green")
        for j in range(1,7):
            self.Player[j].setGeometry(QtCore.QRect(sInitX+(500*int((j-1)%2)), sInitY+(230*(int((j+1)/2)-1)), pInitX, pInitY))
            self.Player[j].setObjectName("Player%d" %j)

            self.n.append([QtWidgets.QLabel(self.Player[j]) for _ in range(36)])
            for i in range(36):
                self.n[j][i].setGeometry(QtCore.QRect(initX1+limitX*(int(i%11)), initY1+(limitY)*int(i/11), limitX, limitY))
                self.n[j][i].setPixmap(QtGui.QPixmap("./pic/%d.jpg" %(i+3)))
                self.n[j][i].setScaledContents(True)
                self.n[j][i].setObjectName("n%d" %i)
                self.n[j][i].setVisible(False)

        # Player Label
        self.NowPlayerLabel = QtWidgets.QLabel(self.centralwidget)
        self.NowPlayerLabel.setGeometry(QtCore.QRect(720, 680, 130, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.NowPlayerLabel.setFont(font)
        self.NowPlayerLabel.setObjectName("Player")

        # PlayerCoin Label
        self.PlayerCoinLabel = QtWidgets.QLabel(self.centralwidget)
        self.PlayerCoinLabel.setGeometry(QtCore.QRect(860, 680, 130, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.PlayerCoinLabel.setFont(font)
        self.PlayerCoinLabel.setObjectName("PlayerCoinLabel")


        # Coin Label
        self.NowCoinLabel = QtWidgets.QLabel(self.centralwidget)
        self.NowCoinLabel.setGeometry(QtCore.QRect(30, 700, 130, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.NowCoinLabel.setFont(font)
        self.NowCoinLabel.setObjectName("CoinLabel")


        # Card Label
        self.NowCardLabel = QtWidgets.QLabel(self.centralwidget)
        self.NowCardLabel.setGeometry(QtCore.QRect(150, 700, 130, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.NowCardLabel.setFont(font)
        self.NowCardLabel.setObjectName("NowCardLabel")

        self.NowCard = QtWidgets.QLabel(self.centralwidget)
        self.NowCard.setGeometry(QtCore.QRect(300, 700, 42, 60))
        self.NowCard.setMinimumSize(QtCore.QSize(42, 60))
        self.NowCard.setText("")
        self.NowCard.setPixmap(QtGui.QPixmap("./pic/back.jpg"))
        self.NowCard.setScaledContents(True)
        self.NowCard.setObjectName("NowCard")

        self.NowCardRemain = QtWidgets.QLabel(self.centralwidget)
        self.NowCardRemain.setGeometry(QtCore.QRect(380, 700, 160, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.NowCardRemain.setFont(font)
        self.NowCardRemain.setObjectName("NowCardRemain")

        self.btnOpenCard = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenCard.setGeometry(QtCore.QRect(570, 700, 100, 60))
        self.btnOpenCard.setObjectName("btnOpenCard")

        self.btnNoThanks = QtWidgets.QPushButton(self.centralwidget)
        self.btnNoThanks.setGeometry(QtCore.QRect(710, 735, 100, 25))
        self.btnNoThanks.setObjectName("btnNoThanks")

        self.btnTakeIt = QtWidgets.QPushButton(self.centralwidget)
        self.btnTakeIt.setGeometry(QtCore.QRect(850, 735, 100, 25))
        self.btnTakeIt.setObjectName("btnTakeIt")

        # Btn 클릭시
        self.btnOpenCard.clicked.connect(self.OpenCard)
        self.btnNoThanks.clicked.connect(self.NoThanks)
        self.btnTakeIt.clicked.connect(self.TakeIt)

        self.btnOpenCard.setEnabled(True)
        self.btnNoThanks.setEnabled(False)
        self.btnTakeIt.setEnabled(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 17))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")

        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")

        MainWindow.setStatusBar(self.statusBar)
        self.actionNew_Game = QtWidgets.QAction(MainWindow)
        self.actionNew_Game.setObjectName("actionNew_Game")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menu.addAction(self.actionNew_Game)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menubar.addAction(self.menu.menuAction())

        self.Winner = QtWidgets.QLabel(self.centralwidget)
        self.Winner.setGeometry(QtCore.QRect(50, 300, 900, 60))
        self.Winner.setStyleSheet("background-color: blue")
        self.Winner.setVisible(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def TakeIt(self):
        np = self.b.nowPlayer
        pl = self.b.p[np]
        pl.takeIt(self.b.nowCoin,self.b.nowCard)

        self.b.nowCoin = 0
        self.NowCard.setPixmap(QtGui.QPixmap("./pic/back.jpg"))
        self.n[np][self.b.nowCard-3].setVisible(True)

        self.btnOpenCard.setEnabled(True)
        self.btnNoThanks.setEnabled(False)
        self.btnTakeIt.setEnabled(False)

        self.NextTurn()

    def NoThanks(self):
        np = self.b.nowPlayer
        self.b.p[np].noThanks()
        self.b.nowCoin += 1

        self.NextTurn()

    def NextTurn(self):
        np = self.b.nowPlayer
        self.Player[np].setStyleSheet("background-color: normal")
        np = self.b.getNextPlayer()
        self.b.setNextPlayer()
        self.NowPlayerLabel.setText("Player: %d" % np)
        self.NowCoinLabel.setText("Coin: %d" % (self.b.nowCoin))
        self.PlayerCoinLabel.setText("Coin: %d" % self.b.p[np].coin)
        self.Player[np].setStyleSheet("background-color: green")
        self.getScores()

        if np != 1:

            self.WaitTurn()



    counting = False

    def WaitTurn(self):
        if not self.counting:
            self.counting = True
            thread = threading.Thread(target=self.something)
            thread.start()

    def something(self):
        for x in range(100):
            time.sleep(.01)
        self.counting = False
        self.ComAction()



    def ComAction(self):
        com = self.b.p[self.b.nowPlayer]
        if self.b.nowCoin == 0:
            self.OpenCard()
        if com.coin == 0:
            self.TakeIt()
        else:
            if self.b.checkCon():
                self.TakeIt()
            else:
                if self.b.nowCard <= 15:
                    self.TakeIt()
                else:
                    self.NoThanks()


    def CalScore(self):
        self.Winner.setVisible(True)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.white)
        self.Winner.setPalette(palette)
        self.Winner.setFont(font)
        self.Winner.setText(" Winner is Player %d" %(self.b.calScore()))


    def OpenCard(self):
        if self.b.deck == []: #더이상 카드 없으므로 점수 계산
            self.CalScore()
        else:
            self.b.nowCard = self.b.openCard()
            self.NowCard.setPixmap(QtGui.QPixmap("./pic/%d.jpg" %self.b.nowCard))

            self.btnOpenCard.setEnabled(False)
            self.btnNoThanks.setEnabled(True)
            self.btnTakeIt.setEnabled(True)

            self.NowCardRemain.setText("Remain: %d" % len(self.b.deck))


    def getScores(self):
        for i in range(1,self.b.numOfPlayer+1):
            self.Player[i].setTitle("Player%d [ %d ]" %(i,self.b.p[i].getScore()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        for i in range(1,7):
            self.Player[i].setTitle(_translate("MainWindow", "Player %d" %i))
        self.NowPlayerLabel.setText(_translate("MainWindow", "Player: %d" %self.b.nowPlayer))
        self.PlayerCoinLabel.setText(_translate("MainWindow", "Coin: %d" % self.b.p[self.b.nowPlayer].coin))
        self.NowCoinLabel.setText(_translate("MainWindow", "Coin: %d" %self.b.nowCoin))
        self.btnOpenCard.setText(_translate("MainWindow", "Open Card"))
        self.btnNoThanks.setText(_translate("MainWindow", "No Thanks!"))
        self.btnTakeIt.setText(_translate("MainWindow", "Take It"))
        self.NowCardLabel.setText(_translate("MainWindow", "NowCard:"))
        self.NowCardRemain.setText(_translate("MainWindow", "Remain: %d" %len(self.b.deck)))
        self.menu.setTitle(_translate("MainWindow", "새 게임"))
        self.actionNew_Game.setText(_translate("MainWindow", "새 게임 시작"))
        self.actionExit.setText(_translate("MainWindow", "종료"))
        self.Winner.setText(_translate("MainWindow", ""))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())





