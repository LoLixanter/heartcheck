# напиши здесь код основного приложения и первого экрана# my_app.py 
из PyQt5.QtCore импорт Qt, QTimer, QTime, qlocalefrom 
из PyQt5.QtGui импорт QDoubleValidator, QIntValidator, QFont 
из PyQt5.QtWidgets импорт ( 
 QApplication, QWidget,  
 QHBoxLayout, QVBoxLayout, QGridLayout,  
 QGroupBox, QRadioButton, 
 QPushButton, QLabel, QListWidget, QLineEdit) 
 
из instr импорт * 
from second_win import *
 
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
 
    def initUI(self):
        ''' создает графические элементы '''
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
 
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft) 
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)          
        self.setLayout(self.layout_line)
 
    def next_click(self):
        self.tw = TestWin()
        self.hide()
 
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
 
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
 
app = QApplication([])
mw = MainWin()
app.exec_()
