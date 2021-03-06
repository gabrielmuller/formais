from nfa import NFA
from parser import *
from regex import Regex
from dialog_af_ui import Ui_Dialog as AF_Dialog
from dialog_gr_ui import Ui_Dialog as GR_Dialog
from words_ui import Ui_words_of_size as Words_Dialog
from window_ui import Ui_MainWindow
from misc import crop

import copy
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QMainWindow, QTableWidgetItem, QFileDialog, QListWidgetItem, 
    QErrorMessage, QDialog)

class GUI(QMainWindow, Ui_MainWindow, AF_Dialog, GR_Dialog):

    def __init__(self):
        QMainWindow.__init__(self)

        #self.fa = NFA({}, "", {})
        self.fa = None
        self.rg = RegularGrammar("",{})

        self.setupUi(self)
        #self.resize(600, 400)

        # Botões
        self.regex_to_fa_button.clicked.connect(self.regex_to_fa)
        self.determinize_button.clicked.connect(self.determinize)
        self.minimize_button.clicked.connect(self.minimize)
        self.reverse_button.clicked.connect(self.reverse)
        self.complement_button.clicked.connect(self.complement)
        self.test_button.clicked.connect(self.test_word)
        self.rg_to_fa_button.clicked.connect(self.rg_to_fa)
        self.fa_to_rg_button.clicked.connect(self.fa_to_rg)
        self.open_button.clicked.connect(self.open_fa)
        self.save_button.clicked.connect(self.save_fa)
        self.list.itemClicked.connect(self.select_fa)
        self.operations_button.clicked.connect(self.fa_op_dialog)
        self.rg_operations_button.clicked.connect(self.rg_op_dialog)
        self.words_button.clicked.connect(self.words_op_dialog)
        self.transition_table.cellClicked.connect(self.click_cell)

        # Ações
        self.actionSalvar.triggered.connect(self.save_fa)
        self.actionAbrir.triggered.connect(self.open_fa)
        self.actionSalvar_GR.triggered.connect(self.save_rg)
        self.actionImportar_GR.triggered.connect(self.open_rg)
        self.actionSalvar_ER.triggered.connect(self.save_regex)
        self.actionImportar_ER.triggered.connect(self.open_regex)

        # Correspondência entre index do QListWidgetItem e autômato
        self.list_fas = []

    def click_cell(self):
        self.table_label.setText(self.transition_table.currentItem().text())
    def select_fa(self):
        self.fa = self.list_fas[self.list.currentRow()]
        self.update_fa_table()

    def regex_to_fa(self):
        regex_str = self.regex_input.text()
        try:
            self.fa = Regex(regex_str).dfa
        except SyntaxError as e:
            self.show_error(e)
            return

        self.fa.regex_str = regex_str
        self.add_fa_to_list()

    def fa_to_rg(self):
        if self.fa:
            self.rg = RegularGrammar.from_nfa(self.fa)
            self.update_rg_text()
        else:
            self.show_error("Não há AF selecionado!")
            return

    def show_error(self, e):
        box = QErrorMessage(self) 
        box.showMessage(str(e))

    def rg_to_fa(self):
        if self.rg_text.toPlainText():
            try:
                self.rg = parse_rg(self.rg_text.toPlainText())
            except SyntaxError as e:
                self.show_error(e)
                return
                
            self.fa = NFA.from_rg(self.rg)
            self.fa.rg_str = self.rg.rg_str
            self.add_fa_to_list()
        else:
            self.show_error("Defina uma gramática!")
            return

    def determinize(self):
        if not self.fa:
            self.show_error("Não há AF selecionado!")
            return
        fa = copy.deepcopy(self.fa)
        fa.determinize()
        self.fa = fa
        self.add_fa_to_list()

    def minimize(self):
        if not self.fa:
            self.show_error("Não há AF selecionado!")
            return
        fa = copy.deepcopy(self.fa)
        fa.minimize()
        self.fa = fa
        self.add_fa_to_list()

    def reverse(self):
        if not self.fa:
            self.show_error("Não há AF selecionado!")
            return
        self.fa = self.fa.reverse()
        self.add_fa_to_list()

    def complement(self):
        if not self.fa:
            self.show_error("Não há AF selecionado!")
            return
        fa = copy.deepcopy(self.fa)
        fa.complement()
        self.fa = fa
        self.add_fa_to_list()

    def test_word(self):
        if not self.fa:
            self.show_error("Não há AF selecionado!")
            return
        if self.fa.accepts(self.word_input.text()):
            self.statusbar.showMessage("Sentença aceita")
        else:
            self.statusbar.showMessage("Sentença rejeitada")

    def update_fa_table(self):
        # restaura regex / gramática
        if self.fa.regex_str:
            self.regex_input.setText(self.fa.regex_str)
        if self.fa.rg_str:
            self.rg_text.setPlainText(self.fa.rg_str)

        alphabet = sorted(self.fa.alphabet())
        states = []
        for state in self.fa.states():
            special = ""
            if state == '-':
                continue
            if state in self.fa.accepting:
                special += "*"
            if state is self.fa.initial:
                special += "->"
            states.append(special + state)

        self.transition_table.setRowCount(len(states))
        self.transition_table.setColumnCount(len(alphabet))
        self.transition_table.setVerticalHeaderLabels(states)
        self.transition_table.setHorizontalHeaderLabels(alphabet)

        transitions = self.fa.transitions
        for i, state in enumerate(self.fa.states()):
            for j, symbol in enumerate(alphabet):
                transition = '-'
                if state in transitions:
                    if symbol in transitions[state]:
                        transition = ", ".join(  \
                            sorted(transitions[state][symbol]))
                self.transition_table.setItem(
                    i, j, QTableWidgetItem(transition))

    def add_fa_to_list(self):
        fa = self.fa
        name = self.name_field.text()
        if name:
            fa.name = name
        self.list_fas.append(fa)
        item = QListWidgetItem(crop(fa.name), self.list)
        self.list.setCurrentItem(item)
        self.update_fa_table()

    def save_fa(self):
        if not self.fa:
            self.show_error("Não há AF selecionado!")
            return

        path, _ = QFileDialog.getSaveFileName(self)
        if path:
            self.fa.save(path)

    def open_fa(self):
        path, _ = QFileDialog.getOpenFileName(self)
        if path:
            nfa = NFA.open(path)
            self.fa = nfa
            self.add_fa_to_list()

    def fa_op_dialog(self):
        Dialog = QtWidgets.QDialog()
        ui = AF_Dialog()
        ui.setupUi(Dialog)

        ui.union_radio.setChecked(True)
        ui.fa_1_combo.addItems(fa.name for fa in self.list_fas)
        ui.fa_2_combo.addItems(fa.name for fa in self.list_fas)
        ui.op_buttonBox.accepted.connect(lambda:self.create_fa_by_op(ui))

        Dialog.exec_()

    def words_op_dialog(self):
        Dialog = QtWidgets.QDialog()
        ui = Words_Dialog()
        ui.setupUi(Dialog)
        
        try:
            size = int(self.n_field.text()) if self.n_field.text() else 3
        except:
            self.show_error("Tamanho deve ser um número")

        if not self.fa:
            self.show_error("Não há autômato selecionado")
            return

        words = self.fa.words_of_size(size)
        msg = "Palavras de tamanho " + str(size) + " em " + self.fa.name
        if len(words) == 10000:
            msg += "\nPalavras demais, mostrando resultado parcial"
        ui.words.setPlainText(msg + '\n\n' + '\n'.join(words))
        Dialog.exec_()
        

    def create_fa_by_op(self, dialog):
        fa1 = self.list_fas[dialog.fa_1_combo.currentIndex()]
        fa2 = self.list_fas[dialog.fa_2_combo.currentIndex()]
        if dialog.difference_radio.isChecked():
            self.difference(fa1, fa2)
        elif dialog.intersection_radio.isChecked():
            self.intersection(fa1, fa2)
        else:
            self.union(fa1, fa2)

    def difference(self, fa1, fa2):
        self.fa = fa1.difference(fa2)
        self.add_fa_to_list()

    def intersection(self, fa1, fa2):
        self.fa = fa1.intersection(fa2)
        self.add_fa_to_list()

    def union(self, fa1, fa2):
        self.fa = fa1.union(fa2)
        self.add_fa_to_list()

    def rg_op_dialog(self):
        Dialog = QtWidgets.QDialog()
        ui = GR_Dialog()
        ui.setupUi(Dialog)

        ui.unionrg_radio.setChecked(True)
        ui.import_gr_1_button.clicked.connect(lambda:self.open_rg_dialog(ui,1))
        ui.import_gr_2_button.clicked.connect(lambda:self.open_rg_dialog(ui,2))
        ui.op_rg_buttonBox.accepted.connect(lambda:self.create_rg_by_op(ui))

        Dialog.exec_()

    def create_rg_by_op(self, dialog):
        rg1 = None
        rg2 = None
        if dialog.rg_1_input.toPlainText():
            rg1 = self.parse_rg(dialog.rg_1_input.toPlainText())
        if dialog.rg_2_input.toPlainText():
            rg2 = self.parse_rg(dialog.rg_2_input.toPlainText())

        if dialog.concatenation_radio.isChecked():
            if not rg1 or not rg2:
                self.show_error("Defina duas gramáticas!")
                return
            self.concatenation(rg1, rg2)
        elif dialog.kleene_radio.isChecked():
            if not rg1 and not rg2 or rg1 and rg2:
                self.show_error("Defina apenas uma gramática!")
                return
            if rg1: self.kleene(rg1)
            elif rg2: self.kleene(rg2)
        else:
            if not rg1 or not rg2:
                self.show_error("Defina duas gramáticas!")
                return
            self.union_rg(rg1, rg2)

    # Importa GR no diálogo de operações
    def open_rg_dialog(self, dialog, input_number):
        path, _ = QFileDialog.getOpenFileName(self)
        rg_string = ""
        if path:
            file = open(path, 'r')
            rg_string = file.read()
            file.close()
            rg = parse_rg(rg_string)
        else:
            return
        if input_number is 1: dialog.rg_1_input.setPlainText(rg.to_string())
        else: dialog.rg_2_input.setPlainText(rg.to_string())

    def concatenation(self, rg1, rg2):
        self.rg = rg1.concatenation(rg2)
        self.update_rg_text()

    def kleene(rg1):
        self.rg = rg1.kleene_closure()
        self.update_rg_text()

    def union_rg(self, rg1, rg2):
        self.rg = rg1.union(rg2)
        self.update_rg_text()

    def update_rg_text(self):
        self.rg_text.setPlainText(self.rg.to_string())

    # Salva GR da janela principal
    def save_rg(self):
        rg = parse_rg(self.rg_text.toPlainText())

        path, _ = QFileDialog.getSaveFileName(self)
        if path:
            file = open(path, 'w')
            file.write(rg.to_string())
            file.close()
        else:
            return

    # Importa GR na janela principal
    def open_rg(self):
        path, _ = QFileDialog.getOpenFileName(self)
        rg_string = ""
        if path:
            file = open(path, 'r')
            rg_string = file.read()
            file.close()
        self.rg = parse_rg(rg_string)
        self.update_rg_text()

    # Parse sem salvar na GR principal
    def parse_rg(self, str):
        try:
            rg = parse_rg(str)
        except (SyntaxError) as e:
            self.show_error(e)
            return
        return rg

    def save_regex(self):
        regex = Regex(self.regex_input.text())

        path, _ = QFileDialog.getSaveFileName(self)
        if path:
            file = open(path, 'w')
            file.write(regex.regex_str)
            file.close()
        else:
            return

    def open_regex(self):
        path, _ = QFileDialog.getOpenFileName(self)
        string = ""
        if path:
            file = open(path, 'r')
            string = file.read()
            try:
                regex = Regex(string)
                self.regex_input.setText(regex.regex_str)
            except SyntaxError as e:
                self.show_error(e)
                return
            file.close()



        
