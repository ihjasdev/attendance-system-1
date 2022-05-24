# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guibzEjHc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(565, 526)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listWidget = QListWidget(self.frame_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(14)
        self.listWidget.setFont(font)

        self.verticalLayout_3.addWidget(self.listWidget)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cam_lbl = QLabel(self.frame_4)
        self.cam_lbl.setObjectName(u"cam_lbl")
        self.cam_lbl.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.cam_lbl)

        self.clear_btn = QPushButton(self.frame_4)
        self.clear_btn.setObjectName(u"clear_btn")
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(16)
        self.clear_btn.setFont(font1)
        self.clear_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.clear_btn)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start_btn = QPushButton(self.frame_3)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setMaximumSize(QSize(16777215, 40))
        self.start_btn.setFont(font)
        self.start_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.start_btn)

        self.download_btn = QPushButton(self.frame_3)
        self.download_btn.setObjectName(u"download_btn")
        self.download_btn.setMaximumSize(QSize(16777215, 40))
        self.download_btn.setFont(font)
        self.download_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.download_btn)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cam_lbl.setText("")
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear list", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.download_btn.setText(QCoreApplication.translate("MainWindow", u"Load data", None))
    # retranslateUi

