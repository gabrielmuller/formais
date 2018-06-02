# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.selected_automaton = QtWidgets.QVBoxLayout()
        self.selected_automaton.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.selected_automaton.setSpacing(6)
        self.selected_automaton.setObjectName("selected_automaton")
        self.fa_label = QtWidgets.QLabel(self.centralwidget)
        self.fa_label.setMinimumSize(QtCore.QSize(0, 0))
        self.fa_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fa_label.setFont(font)
        self.fa_label.setObjectName("fa_label")
        self.selected_automaton.addWidget(self.fa_label)
        self.transition_table = QtWidgets.QTableWidget(self.centralwidget)
        self.transition_table.setMaximumSize(QtCore.QSize(16777215, 999999))
        self.transition_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.transition_table.setObjectName("transition_table")
        self.transition_table.setColumnCount(0)
        self.transition_table.setRowCount(0)
        self.transition_table.horizontalHeader().setDefaultSectionSize(40)
        self.transition_table.horizontalHeader().setMinimumSectionSize(38)
        self.selected_automaton.addWidget(self.transition_table)
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 40))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.determinize_button = QtWidgets.QPushButton(self.horizontalWidget)
        self.determinize_button.setEnabled(True)
        self.determinize_button.setMinimumSize(QtCore.QSize(0, 30))
        self.determinize_button.setObjectName("determinize_button")
        self.horizontalLayout.addWidget(self.determinize_button)
        self.minimize_button = QtWidgets.QPushButton(self.horizontalWidget)
        self.minimize_button.setMinimumSize(QtCore.QSize(0, 30))
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout.addWidget(self.minimize_button)
        self.selected_automaton.addWidget(self.horizontalWidget)
        self.horizontalWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.test_button = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.test_button.setMinimumSize(QtCore.QSize(0, 30))
        self.test_button.setObjectName("test_button")
        self.horizontalLayout_3.addWidget(self.test_button)
        self.word_input = QtWidgets.QLineEdit(self.horizontalWidget_2)
        self.word_input.setMinimumSize(QtCore.QSize(0, 30))
        self.word_input.setObjectName("word_input")
        self.horizontalLayout_3.addWidget(self.word_input)
        self.selected_automaton.addWidget(self.horizontalWidget_2)
        self.horizontalLayout_5.addLayout(self.selected_automaton)
        self.input_section = QtWidgets.QVBoxLayout()
        self.input_section.setObjectName("input_section")
        self.input_section_header = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_section_header.setFont(font)
        self.input_section_header.setObjectName("input_section_header")
        self.input_section.addWidget(self.input_section_header)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.regex_label = QtWidgets.QLabel(self.centralwidget)
        self.regex_label.setObjectName("regex_label")
        self.horizontalLayout_4.addWidget(self.regex_label)
        self.regex_input = QtWidgets.QLineEdit(self.centralwidget)
        self.regex_input.setObjectName("regex_input")
        self.horizontalLayout_4.addWidget(self.regex_input)
        self.regex_to_fa_button = QtWidgets.QPushButton(self.centralwidget)
        self.regex_to_fa_button.setObjectName("regex_to_fa_button")
        self.horizontalLayout_4.addWidget(self.regex_to_fa_button)
        self.input_section.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.rg_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rg_label.sizePolicy().hasHeightForWidth())
        self.rg_label.setSizePolicy(sizePolicy)
        self.rg_label.setObjectName("rg_label")
        self.horizontalLayout_7.addWidget(self.rg_label)
        self.rg_to_fa_button = QtWidgets.QPushButton(self.centralwidget)
        self.rg_to_fa_button.setObjectName("rg_to_fa_button")
        self.horizontalLayout_7.addWidget(self.rg_to_fa_button)
        self.input_section.addLayout(self.horizontalLayout_7)
        self.rg_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.rg_text.setObjectName("rg_text")
        self.input_section.addWidget(self.rg_text)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.input_section.addWidget(self.line)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.input_section.addWidget(self.pushButton_3)
        self.horizontalLayout_5.addLayout(self.input_section)
        self.automaton_list = QtWidgets.QVBoxLayout()
        self.automaton_list.setContentsMargins(0, -1, -1, -1)
        self.automaton_list.setObjectName("automaton_list")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.automaton_list.addWidget(self.label)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.automaton_list.addWidget(self.listView)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setObjectName("open_button")
        self.horizontalLayout_6.addWidget(self.open_button)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_6.addWidget(self.save_button)
        self.automaton_list.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5.addLayout(self.automaton_list)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1030, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.menuFile.addAction(self.actionSalvar)
        self.menuFile.addAction(self.actionAbrir)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Linguagens Regulares"))
        self.fa_label.setText(_translate("MainWindow", "<html><head/><body><p>Autômato Selecionado</p></body></html>"))
        self.determinize_button.setText(_translate("MainWindow", "Determinizar"))
        self.minimize_button.setText(_translate("MainWindow", "Minimizar"))
        self.test_button.setText(_translate("MainWindow", "Testar Sentença"))
        self.input_section_header.setText(_translate("MainWindow", "<html><head/><body><p>Criar Nova Linguagem</p></body></html>"))
        self.regex_label.setText(_translate("MainWindow", "Expressão Regular"))
        self.regex_to_fa_button.setText(_translate("MainWindow", "Converter para AF"))
        self.rg_label.setText(_translate("MainWindow", "Gramática"))
        self.rg_to_fa_button.setText(_translate("MainWindow", "Converter para AF"))
        self.pushButton_3.setText(_translate("MainWindow", "Criar autômato por operações..."))
        self.label.setText(_translate("MainWindow", "Autômatos Criados"))
        self.open_button.setText(_translate("MainWindow", "Abrir..."))
        self.save_button.setText(_translate("MainWindow", "Salvar..."))
        self.menuFile.setTitle(_translate("MainWindow", "Arquivo"))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar AF"))
        self.actionAbrir.setText(_translate("MainWindow", "Importar AF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

