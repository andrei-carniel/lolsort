# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1183, 664)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1163, 603))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid black;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line_nickname = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line_nickname.setFont(font)
        self.line_nickname.setObjectName("line_nickname")
        self.horizontalLayout.addWidget(self.line_nickname)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_add_nickname = QtWidgets.QPushButton(self.groupBox)
        self.button_add_nickname.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_add_nickname.setFont(font)
        self.button_add_nickname.setObjectName("button_add_nickname")
        self.verticalLayout.addWidget(self.button_add_nickname)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.button_remove_nickname = QtWidgets.QPushButton(self.groupBox)
        self.button_remove_nickname.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_remove_nickname.setFont(font)
        self.button_remove_nickname.setObjectName("button_remove_nickname")
        self.verticalLayout.addWidget(self.button_remove_nickname)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.list_nicknames = QtWidgets.QListWidget(self.groupBox)
        self.list_nicknames.setMinimumSize(QtCore.QSize(150, 300))
        self.list_nicknames.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.list_nicknames.setFont(font)
        self.list_nicknames.setObjectName("list_nicknames")
        self.verticalLayout_7.addWidget(self.list_nicknames)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.button_generate_groups = QtWidgets.QPushButton(self.groupBox)
        self.button_generate_groups.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_generate_groups.setFont(font)
        self.button_generate_groups.setObjectName("button_generate_groups")
        self.verticalLayout_6.addWidget(self.button_generate_groups)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_6.addItem(spacerItem3)
        self.button_copy_group = QtWidgets.QPushButton(self.groupBox)
        self.button_copy_group.setMinimumSize(QtCore.QSize(150, 0))
        self.button_copy_group.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_copy_group.setFont(font)
        self.button_copy_group.setObjectName("button_copy_group")
        self.verticalLayout_6.addWidget(self.button_copy_group)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(150, 0))
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 199, 535))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_groups = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_groups.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_groups.setFont(font)
        self.label_groups.setText("")
        self.label_groups.setObjectName("label_groups")
        self.gridLayout_2.addWidget(self.label_groups, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_4.addWidget(self.scrollArea_2)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"    border: 1px solid black;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.list_champions = QtWidgets.QListWidget(self.groupBox_2)
        self.list_champions.setMinimumSize(QtCore.QSize(150, 400))
        self.list_champions.setMaximumSize(QtCore.QSize(200, 400))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.list_champions.setFont(font)
        self.list_champions.setObjectName("list_champions")
        self.verticalLayout_2.addWidget(self.list_champions)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.button_ban_chanpion = QtWidgets.QPushButton(self.groupBox_2)
        self.button_ban_chanpion.setMinimumSize(QtCore.QSize(160, 35))
        self.button_ban_chanpion.setMaximumSize(QtCore.QSize(160, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_ban_chanpion.setFont(font)
        self.button_ban_chanpion.setObjectName("button_ban_chanpion")
        self.horizontalLayout_5.addWidget(self.button_ban_chanpion)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.button_unban_chanpion = QtWidgets.QPushButton(self.groupBox_2)
        self.button_unban_chanpion.setMinimumSize(QtCore.QSize(160, 35))
        self.button_unban_chanpion.setMaximumSize(QtCore.QSize(160, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_unban_chanpion.setFont(font)
        self.button_unban_chanpion.setObjectName("button_unban_chanpion")
        self.horizontalLayout_6.addWidget(self.button_unban_chanpion)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        spacerItem10 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.button_unban_all = QtWidgets.QPushButton(self.groupBox_2)
        self.button_unban_all.setMinimumSize(QtCore.QSize(160, 35))
        self.button_unban_all.setMaximumSize(QtCore.QSize(160, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_unban_all.setFont(font)
        self.button_unban_all.setObjectName("button_unban_all")
        self.horizontalLayout_7.addWidget(self.button_unban_all)
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        spacerItem13 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem13)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.list_banned_champions = QtWidgets.QListWidget(self.groupBox_2)
        self.list_banned_champions.setMinimumSize(QtCore.QSize(150, 400))
        self.list_banned_champions.setMaximumSize(QtCore.QSize(200, 400))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.list_banned_champions.setFont(font)
        self.list_banned_champions.setObjectName("list_banned_champions")
        self.verticalLayout_4.addWidget(self.list_banned_champions)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 2, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.button_generate_champions_list = QtWidgets.QPushButton(self.groupBox_2)
        self.button_generate_champions_list.setMinimumSize(QtCore.QSize(130, 0))
        self.button_generate_champions_list.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_generate_champions_list.setFont(font)
        self.button_generate_champions_list.setObjectName("button_generate_champions_list")
        self.horizontalLayout_9.addWidget(self.button_generate_champions_list)
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem14)
        self.button_show_hide = QtWidgets.QPushButton(self.groupBox_2)
        self.button_show_hide.setMinimumSize(QtCore.QSize(150, 0))
        self.button_show_hide.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_show_hide.setFont(font)
        self.button_show_hide.setObjectName("button_show_hide")
        self.horizontalLayout_9.addWidget(self.button_show_hide)
        spacerItem15 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem15)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 6, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.button_cp_first = QtWidgets.QPushButton(self.groupBox_2)
        self.button_cp_first.setMinimumSize(QtCore.QSize(130, 0))
        self.button_cp_first.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_cp_first.setFont(font)
        self.button_cp_first.setStyleSheet("QPushButton {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.button_cp_first.setObjectName("button_cp_first")
        self.horizontalLayout_8.addWidget(self.button_cp_first)
        spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem16)
        self.button_cp_second = QtWidgets.QPushButton(self.groupBox_2)
        self.button_cp_second.setMinimumSize(QtCore.QSize(130, 0))
        self.button_cp_second.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_cp_second.setFont(font)
        self.button_cp_second.setAutoFillBackground(False)
        self.button_cp_second.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 82, 82);\n"
"}")
        self.button_cp_second.setObjectName("button_cp_second")
        self.horizontalLayout_8.addWidget(self.button_cp_second)
        spacerItem17 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem17)
        self.button_cp_third = QtWidgets.QPushButton(self.groupBox_2)
        self.button_cp_third.setMinimumSize(QtCore.QSize(130, 0))
        self.button_cp_third.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_cp_third.setFont(font)
        self.button_cp_third.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.button_cp_third.setObjectName("button_cp_third")
        self.horizontalLayout_8.addWidget(self.button_cp_third)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_champions_g1 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_champions_g1.setFont(font)
        self.label_champions_g1.setText("")
        self.label_champions_g1.setObjectName("label_champions_g1")
        self.horizontalLayout_10.addWidget(self.label_champions_g1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem18)
        self.label_champions_g2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_champions_g2.setFont(font)
        self.label_champions_g2.setText("")
        self.label_champions_g2.setObjectName("label_champions_g2")
        self.horizontalLayout_10.addWidget(self.label_champions_g2)
        spacerItem19 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem19)
        self.label_champions_g3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_champions_g3.setFont(font)
        self.label_champions_g3.setText("")
        self.label_champions_g3.setObjectName("label_champions_g3")
        self.horizontalLayout_10.addWidget(self.label_champions_g3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.gridLayout_3.addLayout(self.verticalLayout_5, 1, 0, 1, 3)
        self.gridLayout_5.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1183, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lolsort para ARAM v1.1.1 - by Slarav"))
        self.groupBox.setTitle(_translate("MainWindow", "Sortear Equipes"))
        self.label.setText(_translate("MainWindow", "Nickname:"))
        self.button_add_nickname.setText(_translate("MainWindow", "Adicionar Nickname"))
        self.button_remove_nickname.setText(_translate("MainWindow", "Remover Nickname"))
        self.button_generate_groups.setText(_translate("MainWindow", "Gerar Equipes"))
        self.button_copy_group.setText(_translate("MainWindow", "Copiar Equipes"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Sortear Campe??es"))
        self.label_2.setText(_translate("MainWindow", "Lista de Campe??es"))
        self.button_ban_chanpion.setText(_translate("MainWindow", "Banir Campe??o >>"))
        self.button_unban_chanpion.setText(_translate("MainWindow", "<< Desbanir Campe??o"))
        self.button_unban_all.setText(_translate("MainWindow", "<<< Limpar Bans"))
        self.label_3.setText(_translate("MainWindow", "Campe??es Banidos"))
        self.button_generate_champions_list.setText(_translate("MainWindow", "Gerar Listas"))
        self.button_show_hide.setText(_translate("MainWindow", "Exibir/Esconder Lista"))
        self.button_cp_first.setText(_translate("MainWindow", "Equipe Azul"))
        self.button_cp_second.setText(_translate("MainWindow", "Equipe Vermelha"))
        self.button_cp_third.setText(_translate("MainWindow", "Equipe Branca"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
