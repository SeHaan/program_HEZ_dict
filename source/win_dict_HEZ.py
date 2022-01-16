"""
필요한 것
- 최상단 exact 여부 체크박스
- 최상단에 검색창 + 검색버튼?
- 그것보다 아래에 사전의 어휘 전체 리스트
- 우측 전체에 좌측에서 클릭 시 보이게 할 내용 공간
"""

from PyQt5.QtWidgets import QWidget, QCheckBox, QLineEdit,\
    QPushButton, QTextBrowser, QListWidget, QLabel, \
    QHBoxLayout, QVBoxLayout

class dict_HEZ(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # setting widgets
        exactLabel = QLabel('exact')
        exactCheck = QCheckBox()
        findLine = QLineEdit()
        findBtn = QPushButton(text='search')
        totalBtn = QPushButton(text='Entire Dict')
        dictList = QListWidget()
        contentBox = QTextBrowser()

        # Style
        font_init = exactLabel.font()
        font_init.setPointSize(15)
        font_init.setFamilies(['Times New Roman', 'Malgun Gothic'])

        exactLabel.setFont(font_init)
        findLine.setFont(font_init)
        findBtn.setFont(font_init)
        totalBtn.setFont(font_init)
        dictList.setFont(font_init)

        contentBox.setFont(font_init)
        contentBox.setStyleSheet("line-height:1;""padding:3px;")

        # setting hbox
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(exactLabel)
        hbox_1.addWidget(exactCheck)
        hbox_1.addWidget(findLine)
        hbox_1.addWidget(findBtn)
        hbox_1.addWidget(totalBtn)

        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(dictList)
        hbox_2.addWidget(contentBox)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)

        self.setLayout(vbox)