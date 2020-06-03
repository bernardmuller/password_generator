#sha-2 hashing
from hashlib import sha256
import os

#------Terminal program------#
def Combine(passw, accounts):
    combined = []
    for idx in accounts:
        combined.append(idx[3:] + passw)
    print(combined)
    return combined


def To_unicode(comb_list):
    unicode = []
    temp = ''
    for idx in comb_list:
        temp = ''
        for i in range(len(idx)):
            temp += str(ord(idx[i]))
        unicode.append(temp)
    return unicode


def encrypt(list_):
    E = []
    temp = ''
    for i in list_:
        for j in i:
            temp += j
            encryption = sha256(temp.encode('utf-8')).hexdigest()
        E.append(encryption)
        temp = ''
    return E


def passwlength(encryption):
    os.system('cls')
    user_input = int(input('Password Length:'))
    L = []
    for idx in encryption:
        pass_len = idx[:user_input]
        L.append(pass_len)
    return L


def Accounts(pass_list, accounts):
    os.system('cls')
    acnts_dict = dict(zip(accounts,pass_list))
    print(acnts_dict)


def run():
    run = True
    while run:
        passw = input('Enter Password:')
        accounts =[]

        all_accounts = False
        while not all_accounts:
            os.system('cls')
            print(accounts)
            print('Type \"CONFIRM\" when done.')
            account = input('Enter Account Name:').upper()             
            if account != 'CONFIRM':                      
                accounts.append(account)
                all_accounts = False
            else:
                all_accounts = True
                run = False

        combined = Combine(passw, accounts)
        unicode = To_unicode(combined)
        E = encrypt(unicode)
        sha_passw = passwlength(E)
        #final = Accounts(sha_passw,accounts)     
                    
        run = False


def Encode(password,accounts):
    combined = Combine(password,accounts)
    unicode = To_unicode(combined)
    E = encrypt(unicode)    
    sha_passw = passwlength(E)
    return sha_passw

if __name__ == "__main__":
    run()
    # #app = QtWidgets.QApplication(sys.argv)
    # PasswordGenerator = QtWidgets.QMainWindow()
    # ui = Ui_PasswordGenerator()
    # ui.setupUi(PasswordGenerator)
    # PasswordGenerator.show()
    # sys.exit(app.exec_())

    
     