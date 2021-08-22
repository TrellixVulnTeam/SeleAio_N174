
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import part2
from concurrent.futures import ThreadPoolExecutor

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.input_urls_pushButton = QtWidgets.QPushButton(self.tab)
        self.input_urls_pushButton.clicked.connect(self.get_text_file)
        self.input_urls_pushButton.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.input_urls_pushButton.setObjectName("input_urls_pushButton")
        self.start_pushButton = QtWidgets.QPushButton(self.tab)
        self.start_pushButton.clicked.connect(self.threadextract)
        self.start_pushButton.setGeometry(QtCore.QRect(190, 20, 93, 28))
        self.start_pushButton.setObjectName("start_pushButton")
        self.log_box = QtWidgets.QTextBrowser(self.tab)

        # self.console_log = open("test.txt").read()
        # self.log_box.setPlainText(self.console_log.)
        # self.log_box.a


        self.log_box.setGeometry(QtCore.QRect(20, 100, 361, 391))
        self.log_box.setObjectName("log_box")
        self.mail_box = QtWidgets.QTextBrowser(self.tab)
        self.mail_box.setGeometry(QtCore.QRect(440, 100, 331, 391))
        self.mail_box.setObjectName("mail_box")
        self.logs_label = QtWidgets.QLabel(self.tab)
        self.logs_label.setGeometry(QtCore.QRect(20, 70, 55, 16))
        self.logs_label.setObjectName("logs_label")
        self.mails_label = QtWidgets.QLabel(self.tab)
        self.mails_label.setGeometry(QtCore.QRect(440, 70, 55, 16))
        self.mails_label.setObjectName("mails_label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")


        self.send_text_radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.send_text_radioButton.setGeometry(QtCore.QRect(0, 310, 95, 20))
        self.send_text_radioButton.setObjectName("send_text_radioButton")
        self.send_text_radioButton.toggled.connect(self.click_send_text_radioButton)

        self.send_file_radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.send_file_radioButton.setGeometry(QtCore.QRect(0, 340, 95, 20))
        self.send_file_radioButton.setObjectName("send_file_radioButton")
        self.send_file_radioButton.toggled.connect(self.click_send_file_radioButton)

        self.send_text_file_radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.send_text_file_radioButton.setGeometry(QtCore.QRect(0, 370, 131, 20))
        self.send_text_file_radioButton.setObjectName("send_text_file_radioButton")
        self.send_text_file_radioButton.toggled.connect(self.click_send_text_file_radioButton)

        self.save_mails_checkBox = QtWidgets.QCheckBox(self.tab_2)
        self.save_mails_checkBox.setGeometry(QtCore.QRect(0, 400, 91, 20))
        self.save_mails_checkBox.setObjectName("save_mails_checkBox")
        self.save_mails_checkBox.stateChanged.connect(self.click_save_mail)


        self.select_file_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.select_file_pushButton.setGeometry(QtCore.QRect(0, 450, 93, 28))
        self.select_file_pushButton.setObjectName("select_file_pushButton")
        self.select_file_pushButton.clicked.connect(self.select_send_file)

        self.finish_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.finish_pushButton.setGeometry(QtCore.QRect(670, 470, 93, 28))
        self.finish_pushButton.setObjectName("finish_pushButton")
        self.gmail_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.gmail_lineEdit.setGeometry(QtCore.QRect(70, 30, 211, 22))
        self.gmail_lineEdit.setObjectName("gmail_lineEdit")
        self.gmail_lineEdit.textChanged.connect(self.sender)


        self.password_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.password_lineEdit.setGeometry(QtCore.QRect(70, 60, 211, 22))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.password_lineEdit.textChanged.connect(self.password)
        self.check_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.check_pushButton.setGeometry(QtCore.QRect(290, 40, 93, 28))
        self.check_pushButton.setObjectName("check_pushButton")
        self.check_pushButton.clicked.connect(self.label_change)

        self.gmail_label = QtWidgets.QLabel(self.tab_2)
        self.gmail_label.setGeometry(QtCore.QRect(20, 30, 41, 16))
        self.gmail_label.setObjectName("gmail_label")
        self.password_label = QtWidgets.QLabel(self.tab_2)
        self.password_label.setGeometry(QtCore.QRect(0, 60, 71, 16))
        self.password_label.setObjectName("password_label")
        self.gmail_checked_label = QtWidgets.QLabel(self.tab_2)
        self.gmail_checked_label.setGeometry(QtCore.QRect(310, 70, 55, 16))
        self.gmail_checked_label.setObjectName("gmail_checked_label")
        self.gmail_checked_label.setText(" ")
        self.mail_text_textEdit_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.mail_text_textEdit_2.setGeometry(QtCore.QRect(140, 300, 521, 201))
        self.mail_text_textEdit_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.mail_text_textEdit_2.setObjectName("mail_text_textEdit_2")
        self.mail_text_textEdit_2.textChanged.connect(self.mail_text)

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def label_change(self):
        if part2.t:
            self.gmail_checked_label.setText(t)
        else:
            self.gmail_checked_label.setText("OK")
    def sender(self, text):
        part2.sender_email =text
    def password(self, text):
        part2.password =text
    def mail_text(self, text):
        part2.text =text
    def save_mail(self):
        with open('mails.txt', 'w') as f:
            for i in part1.exmaili:
                f.write(i)


    def click_save_mail(self, state):
        if state == Qt.Checked:
            self.finish_pushButton.clicked.connect(self.save_mail)

    def click_send_text_radioButton(self):
        try:
            radiobtn =self.sender()
            if radiobtn.isChecked():
                # self.finish_pushButton.clicked.connect(part2.send_text)
                print("1")
        except Exception as err:
            print(err)
    def click_send_file_radioButton(self):
        radiobtn = self.sender()
        if radiobtn.isChecked():
            # self.finish_pushButton.clicked.connect(part2.send_file)
            print("2")
    def click_send_text_file_radioButton(self):
        radiobtn = self.sender()
        if radiobtn.isChecked():
            # self.finish_pushButton.clicked.connect(part2.send_text_file)
            print("3")
    def get_text_file(self):
        dialog =QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)

        if dialog.exec_():
            file_name= dialog.selectedFiles()
            if file_name[0].endswith('.txt'):
                with open(file_name[0], 'r') as f:
                    self.data= f.readlines()


                    f.close()
            else:
                pass
    def select_send_file(self):
        dialog =QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)

        if dialog.exec_():
            file_name= dialog.selectedFiles()

            with open(file_name[0], 'r') as f:
                self.attach_file= f
                part2.filename =self.attach_file


                f.close()

    def threadextract(self):
        with ThreadPoolExecutor() as executer1:
            executer1.map(part1.extractatag, self.data)
        with ThreadPoolExecutor() as executer2:
            executer2.map(part1.extractemail, part1.ltags)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.input_urls_pushButton.setText(_translate("MainWindow", "input urls"))
        self.start_pushButton.setText(_translate("MainWindow", "start"))
        self.logs_label.setText(_translate("MainWindow", "logs:"))
        self.mails_label.setText(_translate("MainWindow", "mails:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.save_mails_checkBox.setText(_translate("MainWindow", "save mails"))

        self.send_text_radioButton.setText(_translate("MainWindow", "send text"))
        self.send_file_radioButton.setText(_translate("MainWindow", "send file"))
        self.send_text_file_radioButton.setText(_translate("MainWindow", "send text and file"))
        self.select_file_pushButton.setText(_translate("MainWindow", "select file"))
        self.finish_pushButton.setText(_translate("MainWindow", "finish"))
        self.check_pushButton.setText(_translate("MainWindow", "check"))
        self.gmail_label.setText(_translate("MainWindow", "gmail:"))
        self.password_label.setText(_translate("MainWindow", "password:"))
        # self.gmail_checked_label.setText(_translate("MainWindow", "TextLabel"))
        self.mail_text_textEdit_2.setToolTip(_translate("MainWindow", "type here your Message"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
