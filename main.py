from PyQt5 import QtCore, QtGui, QtWidgets
from hashlib import sha256
#import backend
#import asyncio

class Ui_PasswordGenerator(object):
    password = ''
    list_accounts = []
    password_length = 15
    passwords = []


    def __init__(self):
        pass


    def setupUi(self, PasswordGenerator):
        PasswordGenerator.setObjectName("PasswordGenerator")
        PasswordGenerator.resize(444, 243)
        self.centralwidget = QtWidgets.QWidget(PasswordGenerator)
        self.centralwidget.setObjectName("centralwidget")

        ## Enter Password
        self.Pass_label = QtWidgets.QLabel(self.centralwidget)
        self.Pass_label.setGeometry(QtCore.QRect(10, 10, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Pass_label.setFont(font)
        self.Pass_label.setObjectName("Pass_label")
        self.AddButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton_1.setGeometry(QtCore.QRect(360, 10, 75, 23))
        self.AddButton_1.setObjectName("AddButton_1")
        self.AddButton_1.clicked.connect(self.passAddbtn)

        ## Enter Account
        self.Account_label = QtWidgets.QLabel(self.centralwidget)
        self.Account_label.setGeometry(QtCore.QRect(10, 40, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Account_label.setFont(font)
        self.Account_label.setObjectName("Account_label")
        self.AddButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton_2.setGeometry(QtCore.QRect(360, 40, 75, 23))
        self.AddButton_2.setObjectName("AddButton_2")
        self.AddButton_2.clicked.connect(self.accountAddbtn)

        ## Output Box
        self.Output_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.Output_textEdit.setGeometry(QtCore.QRect(80, 140, 301, 61))
        self.Output_textEdit.setObjectName("Output_textEdit")
        self.Length_label = QtWidgets.QLabel(self.centralwidget)
        self.Length_label.setGeometry(QtCore.QRect(10, 70, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)

        ## Enter Length
        self.Length_label.setFont(font)
        self.Length_label.setObjectName("Length_label")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(130, 70, 42, 22))
        self.spinBox.setMinimum(7)
        self.spinBox.setMaximum(15)
        self.spinBox.setObjectName("spinBox")

        ## Generate Button
        self.GenButton = QtWidgets.QPushButton(self.centralwidget)
        self.GenButton.setGeometry(QtCore.QRect(190, 110, 75, 23))
        self.GenButton.setObjectName("GenButton")

        self.GenButton.clicked.connect(self.btnGenerate)

        ## Password box
        self.Passw_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Passw_lineEdit.setGeometry(QtCore.QRect(130, 10, 221, 20))
        self.Passw_lineEdit.setObjectName("Passw_lineEdit")

        ## Account Box 
        self.Account_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Account_lineEdit.setGeometry(QtCore.QRect(130, 40, 221, 20))
        self.Account_lineEdit.setObjectName("Account_lineEdit")

        PasswordGenerator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PasswordGenerator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 444, 21))
        self.menubar.setObjectName("menubar")
        PasswordGenerator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PasswordGenerator)
        self.statusbar.setObjectName("statusbar")
        PasswordGenerator.setStatusBar(self.statusbar)

        self.retranslateUi(PasswordGenerator)
        QtCore.QMetaObject.connectSlotsByName(PasswordGenerator)
            
        
    def Display(self, pass_, accounts):
        temp = ''
        #self.Output_textEdit.clear()
        for i in range(len(accounts)):
            temp = accounts[i] + ' : ' + pass_[i] + ' \n'
        self.Output_textEdit.setText(temp) 

        
    def retranslateUi(self, PasswordGenerator):
        _translate = QtCore.QCoreApplication.translate
        PasswordGenerator.setWindowTitle(_translate("PasswordGenerator", "Password Generator"))
        self.Pass_label.setText(_translate("PasswordGenerator", "Enter Password:"))
        self.AddButton_1.setText(_translate("PasswordGenerator", "Add"))
        self.Account_label.setText(_translate("PasswordGenerator", "Enter Account:"))
        self.AddButton_2.setText(_translate("PasswordGenerator", "Add"))
        self.Length_label.setText(_translate("PasswordGenerator", "Enter Length:"))
        self.GenButton.setText(_translate("PasswordGenerator", "Generate"))


    def btnGenerate(self):
        self.passwords = self.Encode(self.password, self.list_accounts)      
        self.Display(self.passwords, self.list_accounts)
               

    def passAddbtn(self):
        self.password = self.Passw_lineEdit.text()
        self.Output_textEdit.setText('Password Added: ' + self.password)     
       
        
    def accountAddbtn(self):  
        self.list_accounts.append(self.Account_lineEdit.text())                          
        self.Output_textEdit.clear()        
        temp = ''
        for i in self.list_accounts:
            temp += "Account Added: " + i + '\n'        
        self.Output_textEdit.setText(temp)
        self.Account_lineEdit.clear()


    def Combine(self, passw, accounts):
        combined = []
        for idx in accounts:
            combined.append(idx[3:] + passw)
        #print(combined)
        return combined


    def To_unicode(self, comb_list):
        unicode = []
        temp = ''
        for idx in comb_list:
            temp = ''
            for i in range(len(idx)):
                temp += str(ord(idx[i]))
            unicode.append(temp)
        return unicode


    def encrypt(self, list_):
        E = []
        temp = ''
        for i in list_:
            for j in i:
                temp += j
                encryption = sha256(temp.encode('utf-8')).hexdigest()
            E.append(encryption)
            temp = ''
        return E


    def passwlength(self, encryption):
        #os.system('cls')
        #user_input = int(input('Password Length:'))
        L = []
        for idx in encryption:
            pass_len = idx[:self.password_length]
            L.append(pass_len)
        return L    


    def Encode(self, password,accounts):
        combined = self.Combine(password,accounts)
        unicode = self.To_unicode(combined)
        E = self.encrypt(unicode)    
        sha_passw = self.passwlength(E)
        return sha_passw


App = None
if __name__ == "__main__":
    import sys
    ## app = QtWidgets.QApplication(sys.argv)
    App = QtWidgets.QApplication.instance()
    if App is None:
        App = QtWidgets.QApplication(sys.argv)
    PasswordGenerator = QtWidgets.QMainWindow()
    ui = Ui_PasswordGenerator()
    ui.setupUi(PasswordGenerator)
    PasswordGenerator.show()
    sys.exit(App.exec_())


