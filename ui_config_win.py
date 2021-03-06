# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_winMNuPlk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_configWindow(object):
    def setupUi(self, configWindow):
        if not configWindow.objectName():
            configWindow.setObjectName(u"configWindow")
        configWindow.setEnabled(True)
        configWindow.resize(337, 352)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(configWindow.sizePolicy().hasHeightForWidth())
        configWindow.setSizePolicy(sizePolicy)
        configWindow.setMinimumSize(QSize(337, 352))
        configWindow.setMaximumSize(QSize(337, 352))
        # icon = QIcon()
        # icon.addFile(u"CalculaINF/config.png", QSize(), QIcon.Normal, QIcon.Off)
        appIcon2 = QIcon("icon.png")
        configWindow.setWindowIcon(appIcon2)
        configWindow.setAutoFillBackground(False)
        configWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(configWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.date_refer = QDateEdit(self.centralwidget)
        self.date_refer.setObjectName(u"date_refer")
        self.date_refer.setGeometry(QRect(40, 40, 51, 21))
        font = QFont()
        font.setPointSize(11)
        self.date_refer.setFont(font)
        self.date_refer.setAlignment(Qt.AlignCenter)
        self.date_refer.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date_refer.setDateTime(QDateTime(QDate(2020, 3, 31), QTime(0, 0, 0)))
        self.date_refer.setMaximumDateTime(QDateTime(QDate(2500, 12, 31), QTime(23, 59, 59)))
        self.date_refer.setMinimumDateTime(QDateTime(QDate(1950, 1, 1), QTime(0, 0, 0)))
        self.date_refer.setDate(QDate(2020, 2, 31))
        self.botao_salvar = QPushButton(self.centralwidget)
        self.botao_salvar.setObjectName(u"botao_salvar")
        self.botao_salvar.setGeometry(QRect(40, 300, 161, 31))
        self.t_pri = QLineEdit(self.centralwidget)
        self.t_pri.setObjectName(u"t_pri")
        self.t_pri.setGeometry(QRect(40, 110, 131, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 90, 131, 16))
        self.t_seg = QLineEdit(self.centralwidget)
        self.t_seg.setObjectName(u"t_seg")
        self.t_seg.setGeometry(QRect(40, 160, 131, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 140, 131, 16))
        self.t_ter = QLineEdit(self.centralwidget)
        self.t_ter.setObjectName(u"t_ter")
        self.t_ter.setGeometry(QRect(40, 210, 131, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 190, 131, 16))
        self.t_qua = QLineEdit(self.centralwidget)
        self.t_qua.setObjectName(u"t_qua")
        self.t_qua.setGeometry(QRect(40, 260, 131, 21))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 240, 131, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 20, 151, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(220, 60, 61, 51))
        self.label_6.setLineWidth(1)
        self.label_6.setWordWrap(True)
        self.r_pri = QLineEdit(self.centralwidget)
        self.r_pri.setObjectName(u"r_pri")
        self.r_pri.setGeometry(QRect(230, 110, 21, 21))
        self.r_pri.setAlignment(Qt.AlignCenter)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(180, 110, 41, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 110, 47, 21))
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(180, 160, 41, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(260, 160, 47, 21))
        self.r_seg = QLineEdit(self.centralwidget)
        self.r_seg.setObjectName(u"r_seg")
        self.r_seg.setGeometry(QRect(230, 160, 21, 21))
        self.r_seg.setAlignment(Qt.AlignCenter)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(180, 210, 41, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(260, 210, 47, 21))
        self.r_ter = QLineEdit(self.centralwidget)
        self.r_ter.setObjectName(u"r_ter")
        self.r_ter.setGeometry(QRect(230, 210, 21, 21))
        self.r_ter.setAlignment(Qt.AlignCenter)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(180, 260, 41, 16))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(260, 260, 47, 21))
        self.r_qua = QLineEdit(self.centralwidget)
        self.r_qua.setObjectName(u"r_qua")
        self.r_qua.setGeometry(QRect(230, 260, 21, 21))
        self.r_qua.setAlignment(Qt.AlignCenter)
        configWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(configWindow)
        self.statusbar.setObjectName(u"statusbar")
        configWindow.setStatusBar(self.statusbar)

        self.retranslateUi(configWindow)

        QMetaObject.connectSlotsByName(configWindow)
    # setupUi

    def retranslateUi(self, configWindow):
        configWindow.setWindowTitle(QCoreApplication.translate("configWindow", u"Configura\u00e7\u00f5es", None))
        self.date_refer.setDisplayFormat(QCoreApplication.translate("configWindow", u"dd/MM", None))
        self.botao_salvar.setText(QCoreApplication.translate("configWindow", u"Salvar", None))
#if QT_CONFIG(shortcut)
        self.botao_salvar.setShortcut(QCoreApplication.translate("configWindow", u"KP_Enter", None))
        self.botao_salvar.setShortcut(QCoreApplication.translate("configWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.t_pri.setText(QCoreApplication.translate("configWindow", u"INFANTIL B", None))
        self.label.setText(QCoreApplication.translate("configWindow", u"Primeira turma do Infantil:", None))
        self.t_seg.setText(QCoreApplication.translate("configWindow", u"INFANTIL C", None))
        self.label_2.setText(QCoreApplication.translate("configWindow", u"Segunda turma do Infantil:", None))
        self.t_ter.setText(QCoreApplication.translate("configWindow", u"INFANTIL D", None))
        self.label_3.setText(QCoreApplication.translate("configWindow", u"Terceira turma do Infantil:", None))
        self.t_qua.setText(QCoreApplication.translate("configWindow", u"INFANTIL D1", None))
        self.label_5.setText(QCoreApplication.translate("configWindow", u"Quarta turma do Infantil:", None))
        self.label_4.setText(QCoreApplication.translate("configWindow", u"Data refer\u00eancia para o c\u00e1lculo:", None))
        self.label_6.setText(QCoreApplication.translate("configWindow", u"Resultado do c\u00e1lculo:", None))
        self.r_pri.setText(QCoreApplication.translate("configWindow", u"2", None))
        self.label_7.setText(QCoreApplication.translate("configWindow", u"anos", None))
        self.label_8.setText(QCoreApplication.translate("configWindow", u"anos", None))
        self.r_seg.setText(QCoreApplication.translate("configWindow", u"3", None))
        self.label_9.setText(QCoreApplication.translate("configWindow", u"anos", None))
        self.r_ter.setText(QCoreApplication.translate("configWindow", u"4", None))
        self.label_10.setText(QCoreApplication.translate("configWindow", u"anos", None))
        self.r_qua.setText(QCoreApplication.translate("configWindow", u"5", None))
    # retranslateUi

