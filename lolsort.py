import sys
from PyQt5.QtWidgets import QApplication, QListWidget, QMessageBox, QWidget, QComboBox, QAbstractItemView, QLabel, \
    QMainWindow, QTableWidgetItem, QPushButton, QVBoxLayout, QDialog, QHBoxLayout, QDialogButtonBox, QAction, QFileDialog

from database import DB
from objects.Group import Group
from ui_mainwindow import Ui_MainWindow
import random

list_nicknames = []
list_champions = []
list_groups = []
list_wait = []

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.button_add_nickname.clicked.connect(self.on_button_add_nickname_clicked)
        self.ui.button_remove_nickname.clicked.connect(self.on_button_remove_nickname_clicked)
        self.ui.button_generate_groups.clicked.connect(self.on_button_generate_groups_clicked)

    def show(self):
        self.main_win.show()
        self.load_nicknames()
        # DB.insert_all_champions()
        self.load_champions()

    def load_nicknames(self):
        global list_nicknames

        self.ui.list_nicknames.clear()
        list_nicknames = DB.select_all_nicknames()
        for pos in range(len(list_nicknames)):
            self.ui.list_nicknames.addItem(list_nicknames[pos].nickname)

    def load_champions(self):
        global list_champions

        self.ui.list_champions.clear()
        list_champions = DB.select_all_champions()
        for pos in range(len(list_champions)):
            self.ui.list_champions.addItem(list_champions[pos].name)

    def on_button_add_nickname_clicked(self):
        nickname = self.ui.line_nickname.text()
        if len(nickname) > 0:
            DB.insert_to_nickname(nickname)

            self.load_nicknames()
            self.ui.line_nickname.setText("")

    def on_button_remove_nickname_clicked(self):
        global list_nicknames

        pos = self.ui.list_nicknames.currentRow()

        if pos >= 0:
            DB.delete_nickname(list_nicknames[pos].id)
            self.load_nicknames()

    def on_button_generate_groups_clicked(self):
        global list_nicknames, list_groups, list_wait

        self.ui.label_groups.text()
        number_of_groups = len(list_nicknames)//5
        total_players = number_of_groups * 5
        arr2 = list_nicknames.copy()
        list_groups = []
        list_wait = []

        print("ll")

        for pos in range(total_players, len(list_nicknames)):
            list_wait.append(list_nicknames[pos])

        for pos in range(total_players, len(list_nicknames)):
            arr2.pop(total_players)

        for pos in range(1, (number_of_groups + 1)):
            list_groups.append(Group(("Group " + str(pos)), []))

        for pos_x in range(len(list_groups)):
            list = []

            for pos_y in range(5):

                if (len(arr2) - 1) > 0:
                    rdn = random.randint(0, (len(arr2) - 1))
                else:
                    rdn = 0


                list.append(arr2[rdn])
                arr2.pop(rdn)
            list_groups[pos_x].list_members = list

        text = ""
        for pos_x in range(len(list_groups)):
            grp = list_groups[pos_x]

            if text == "":
                text = grp.name + "\n"
            else:
                text += "\n" + grp.name + "\n"

            for pos_y in range(len(grp.list_members)):
                text += "\n\t" + grp.list_members[pos_y].nickname + "\n"

        if len(list_wait) > 0:
            if text == "":
                text += "Wait list"
            else:
                text += "\n\n Wait list"

            for pos in range(len(list_wait)):
                text += "\n\t" + list_wait[pos].nickname

        self.ui.label_groups.setText(text)

    def get_members(self, arr):
        list = []



if __name__ == '__main__':
    app = QApplication(sys.argv)
    DB.create_all_tables()
    main_win = MainWindow()
    main_win.show()

    sys.exit(app.exec_())