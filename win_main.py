import sys
import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QListWidgetItem, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from source.function_encoding import encode_Lee
from source.function_dict import HEZdict as hz
from source.win_dict_HEZ import dict_HEZ

df = pd.read_csv('source/data/HEZ_211020.csv', encoding='utf-8')
df = df.fillna('(none)')

class MainApp(QMainWindow):
    def __init__(self, df):
        super().__init__()
        self.df = df
        self.initUI()

    def initUI(self):
        wg = dict_HEZ()
        self.setCentralWidget(wg)

        """
        0 <PyQt5.QtWidgets.QVBoxLayout object
        1 <PyQt5.QtWidgets.QLabel object
        2 <PyQt5.QtWidgets.QCheckBox object
        3 <PyQt5.QtWidgets.QLineEdit object
        4 <PyQt5.QtWidgets.QPushButton object
        5 <PyQt5.QtWidgets.QPushButton object
        6 <PyQt5.QtWidgets.QListWidget object
        7 <PyQt5.QtWidgets.QTextBrowser object
        8 <PyQt5.QtCore.QPropertyAnimation object
        9 <PyQt5.QtCore.QPropertyAnimation object
        """

        # Action
        findLine = self.centralWidget().children()[3]
        findBtn = self.centralWidget().children()[4]
        totalBtn = self.centralWidget().children()[5]

        findLine.returnPressed.connect(self.findWord)
        findBtn.clicked.connect(self.findWord)
        totalBtn.clicked.connect(self.viewEntireDict)

        dictList = self.centralWidget().children()[6]
        dictList.currentItemChanged.connect(self.viewContent_single)
        

        # 윈도우 #
        self.setWindowTitle("Hezhen Dictionary ver. 1.0.0")
        self.setWindowIcon(QIcon("icons.png"))
        self.resize(800, 800)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    # Slots #
    def findWord(self):
        self.centralWidget().children()[6].clear()

        findLine = self.centralWidget().children()[3]
        exactCheck = self.centralWidget().children()[2]
        word = encode_Lee(findLine.text())
        if word == "":
            msgBox = QMessageBox.critical(self, "Warning", "Enter the string!")
            return

        if exactCheck.isChecked() == True:
            exact = 0
        else:
            exact = 1

        wordList = hz(self.df)
        numList = wordList.findword_exact(word, str(0), exact_param=exact)
        if len(numList) == 0:
            msgBox = QMessageBox.critical(self, "Warning", "Cannot fount the string!")
        for i in numList:
            word = QListWidgetItem(self.df.loc[i, '전사(변환)'])
            self.centralWidget().children()[6].addItem(word)

    def viewEntireDict(self):
        self.centralWidget().children()[6].clear()

        for i in range(len(self.df['전사(변환)'])):
            word = QListWidgetItem(self.df.loc[i, '전사(변환)'])
            self.centralWidget().children()[6].addItem(word)

    def viewContent_single(self):
        if str(type(self.centralWidget().children()[6].currentItem())) == "<class 'NoneType'>":
            return
            
        word = self.centralWidget().children()[6].currentItem().text()
        wordList = hz(self.df)
        numList = wordList.findword_exact(word, str(0), exact_param=0)
        print(numList)

        listLen = len(self.centralWidget().children()[6])
        i_dx = self.centralWidget().children()[6].currentRow()
        print(i_dx)

        # =============== 요주의 구간 시작 ================= #

        if listLen == len(self.df['전사(변환)']): # entire 상태
            full_text = self.get_full_text(i_dx)
        else: # entire가 아닌 상태
            new_list = []
            j = 0
            while j < listLen:
                listWord = self.centralWidget().children()[6].item(j).text()
                new_list_ind = wordList.findword_exact(listWord, '0', 0)
                new_list = new_list + new_list_ind

                if len(new_list_ind) != 1:
                    j += len(new_list_ind)
                else:
                    j += 1

            print(new_list)
            full_text = self.get_full_text(new_list[i_dx])

        # ================ 요주의 구간 끝 ================== #
        
        self.centralWidget().children()[7].clear()
        self.centralWidget().children()[7].append(full_text)


    def get_full_text(self, i):
        text = "<h1>" + self.df.loc[i, '전사(변환)'] + "</h1>"
        index = "<i>Serial Num.: " + str(self.df.loc[i, '일련번호']) + "</i>"
        ref = "<i>Page: " + self.df.loc[i, '페이지'] + "</i>"
        trans = "Originally, <b>" + self.df.loc[i, '전사(원문)'] + "</b>"
        df_class = "<b> - Class</b>: " + self.df.loc[i, '부류']
        chi = "<b> - Chi</b>: " + self.df.loc[i, '한어']
        kor = "<b> - Kor</b>: " + self.df.loc[i, '한국어']
        note = "<b> - Note</b>: " + self.df.loc[i, '메모']

        full_text = text + index + "<br>" + ref + "<br><br>" + trans \
             + "<br><br>" + df_class + "<br>" + chi + "<br>" + kor + "<br>" + note

        return full_text
            

## 메인 ##
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainApp(df)
    sys.exit(app.exec_())