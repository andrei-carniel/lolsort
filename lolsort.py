import sys, os

from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow

import Constants
from database import DB
from objects.Group import Group
from ui_mainwindow import Ui_MainWindow
import random

list_nicknames = []
list_champions = []
list_groups = []
list_wait = []

groups_txt = ""
champ_g1_txt = ""
champ_g2_txt = ""
champ_g3_txt = ""

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        # self.main_win.setStyleSheet("{background-image: url(:/ARAMzin.png);}");

        self.ui.button_add_nickname.clicked.connect(self.on_button_add_nickname_clicked)
        self.ui.button_remove_nickname.clicked.connect(self.on_button_remove_nickname_clicked)
        self.ui.button_generate_groups.clicked.connect(self.on_button_generate_groups_clicked)
        self.ui.button_copy_group.clicked.connect(self.on_button_copy_group_clicked)

        self.ui.button_ban_chanpion.clicked.connect(self.on_button_ban_champion_clicked)
        self.ui.button_unban_chanpion.clicked.connect(self.on_button_unban_champion_clicked)
        self.ui.button_unban_all.clicked.connect(self.on_button_unban_all_clicked)
        self.ui.button_generate_champions_list.clicked.connect(self.on_button_generate_champions_groups_clicked)

        self.ui.button_cp_first.clicked.connect(self.on_button_cp_first_clicked)
        self.ui.button_cp_second.clicked.connect(self.on_button_cp_second_clicked)
        self.ui.button_cp_third.clicked.connect(self.on_button_cp_third_clicked)
        self.ui.button_show_hide.clicked.connect(self.on_button_show_hide_clicked)

    def show(self):
        self.main_win.show()
        self.load_nicknames()
        # DB.insert_all_champions()
        self.load_champions(True)

    def load_nicknames(self):
        global list_nicknames

        self.ui.list_nicknames.clear()
        list_nicknames = DB.select_all_nicknames()
        for pos in range(len(list_nicknames)):
            self.ui.list_nicknames.addItem(list_nicknames[pos].nickname)

    def load_champions(self, load_from_db):
        global list_champions

        self.ui.list_champions.clear()
        self.ui.list_banned_champions.clear()
        if load_from_db:
            list_champions = DB.select_all_champions()
        for champ in list_champions:
            if champ.ban == False:
                self.ui.list_champions.addItem(champ.name)
            else:
                self.ui.list_banned_champions.addItem(champ.name)

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
        global list_nicknames, list_groups, list_wait, groups_txt

        self.ui.label_groups.text()
        number_of_groups = len(list_nicknames)//5
        total_players = number_of_groups * 5
        arr2 = list_nicknames.copy()
        list_groups = []
        list_wait = []

        for pos in range(total_players, len(list_nicknames)):
            list_wait.append(list_nicknames[pos])

        for pos in range(total_players, len(list_nicknames)):
            arr2.pop(total_players)

        for pos in range(1, (number_of_groups + 1)):
            list_groups.append(Group(("Equipe " + str(pos)), []))

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

        groups_txt = ""
        for pos_x in range(len(list_groups)):
            grp = list_groups[pos_x]

            if groups_txt == "":
                groups_txt = grp.name
            else:
                groups_txt += "\n" + grp.name

            for pos_y in range(len(grp.list_members)):
                groups_txt += "\n\t" + grp.list_members[pos_y].nickname

            groups_txt += "\n"

        if len(list_wait) > 0:
            if groups_txt == "":
                groups_txt += "Lista de espera"
            else:
                groups_txt += "\n\nLista de espera"

            for pos in range(len(list_wait)):
                groups_txt += "\n\t" + list_wait[pos].nickname

        self.ui.label_groups.setText(groups_txt)

    def on_button_copy_group_clicked(self):
        global groups_txt

        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(groups_txt, mode=cb.Clipboard)

    def on_button_ban_champion_clicked(self):
        list_items = self.ui.list_champions.selectedItems()

        if len(list_items) == 0:
            return

        for item in list_items:
            self.update_champ(item.text(), True)

        self.load_champions(False)

    def on_button_unban_champion_clicked(self):
        list_items = self.ui.list_banned_champions.selectedItems()

        if len(list_items) == 0:
            return

        for item in list_items:
            self.update_champ(item.text(), False)

        self.load_champions(False)

    def on_button_unban_all_clicked(self):
        global list_champions

        for champ in list_champions:
            champ.ban = False

        self.load_champions(False)

    def update_champ(self, name_champ, ban_status):
        global list_champions

        for champ in list_champions:
            if champ.name == name_champ:
                champ.ban = ban_status
                return

    def on_button_generate_champions_groups_clicked(self):
        global list_champions, champ_g1_txt, champ_g2_txt, champ_g3_txt

        list_champ_name = []
        champ_g1_txt = "Equipe Azul\n"
        champ_g2_txt = "Equipe Vermelha\n"
        champ_g3_txt = "Equipe Branca\n"

        for champ in list_champions:
            if champ.ban == False:
                list_champ_name.append(champ.name)

        if len(list_champ_name) < 46:
            showdialog("Erro", "Não há campeões não banidos suficientes para o sorteio.")
            champ_g1_txt = ""
            champ_g2_txt = ""
            champ_g3_txt = ""
            self.ui.label_champions_g1.setText("")
            self.ui.label_champions_g2.setText("")
            self.ui.label_champions_g3.setText("")
            return

        blue_team_list = []
        red_team_list = []
        white_team_list = []

        for pos_y in range(15):
            rdn1 = self.get_random(list_champ_name)
            # champ_g1_txt += "\n\t" + list_champ_name[rdn1]
            blue_team_list.append(list_champ_name[rdn1])
            list_champ_name.pop(rdn1)

            rdn2 = self.get_random(list_champ_name)
            # champ_g2_txt += "\n\t" + list_champ_name[rdn2]
            red_team_list.append(list_champ_name[rdn2])
            list_champ_name.pop(rdn2)

            rdn3 = self.get_random(list_champ_name)
            # champ_g3_txt += "\n\t" + list_champ_name[rdn3]
            white_team_list.append(list_champ_name[rdn3])
            list_champ_name.pop(rdn3)

        self.ui.label_champions_g1.setText("")
        self.ui.label_champions_g2.setText("")
        self.ui.label_champions_g3.setText("")

        champ_g1_txt += self.organize_and_create_list(blue_team_list)
        champ_g2_txt += self.organize_and_create_list(red_team_list)
        champ_g3_txt += self.organize_and_create_list(white_team_list)

        showdialog("Sucesso", "As listas de campeões foram geradas.")

    def organize_and_create_list(self, list):
        list.sort()
        text = ""

        for champ in list:
            text += "\n  " + champ

        return text

    def get_random(self, arr2):
        if (len(arr2) - 1) > 0:
            return random.randint(0, (len(arr2) - 1))
        else:
            return 0

    def on_button_show_hide_clicked(self):
        global champ_g1_txt, champ_g2_txt

        t1 = self.ui.label_champions_g1.text()
        t2 = self.ui.label_champions_g2.text()
        t3 = self.ui.label_champions_g3.text()

        if len(t1) > 0 or len(t2) > 0 or len(t3) > 0:
            self.ui.label_champions_g1.setText("")
            self.ui.label_champions_g2.setText("")
            self.ui.label_champions_g3.setText("")
        else:
            self.ui.label_champions_g1.setText(champ_g1_txt)
            self.ui.label_champions_g2.setText(champ_g2_txt)
            self.ui.label_champions_g3.setText(champ_g3_txt)

    def on_button_cp_first_clicked(self):
        global champ_g1_txt, champ_g2_txt

        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(champ_g1_txt, mode=cb.Clipboard)

    def on_button_cp_second_clicked(self):
        global champ_g2_txt

        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(champ_g2_txt, mode=cb.Clipboard)

    def on_button_cp_third_clicked(self):
        global champ_g3_txt

        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(champ_g3_txt, mode=cb.Clipboard)

def showdialog(title, message):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(message)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Ok)

    returnValue = msgBox.exec()
    # if returnValue == QMessageBox.Ok:
    #     print('OK clicked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    isExist = os.path.exists(Constants.DB_PATH)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(Constants.DB_PATH)
    DB.create_all_tables()
    main_win = MainWindow()
    main_win.show()

    sys.exit(app.exec_())