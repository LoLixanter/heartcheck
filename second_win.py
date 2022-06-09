# напиши здесь код для второго экрана приложения# second_win.py 
из PyQt5.QtCore импорт Qt, QTimer, QTime, qlocalefrom 
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений 
из PyQt5.QtWidgets импорт ( 
 QApplication, QWidget,  
 QHBoxLayout, QVBoxLayout, QGridLayout,  
 QGroupBox, QRadioButton, 
 QPushButton, QLabel, QListWidget, QLineEdit) 
 
из instr импорт * 
из импорта final_win * 
 
класс Person(): 
 def __init__(self, name, age): 
 self.name = имя 
 self.age = возраст 
 
эксперимент класса (): 
 def __init__(self, person, test1, test2, test3): 
 self.person = человек 
 self.test1 = test1 
 self.test2 = test2 
 self.test3 = test3 
 
класс TestWin(QWidget): 
 def __init__(self): 
 ''' окно, в котором проводится опрос ''' 
 super().__init__() 
 
 # создаём и настраиваем графические эелементы: 
 self.initUI() 
 
 #устанавливает связи между элементами 
 self.connectes() 
 
 #устанавливает, как будет выглядеть окно (надпись, размер, место) 
        self.set_appear()
 
        # старт:
        self.show()
 
    def next_click(self):
        self.tw = TestWin()
        self.hide()
 
 def подключается (самостоятельно): 
 self.btn_next.clicked.connect(self.next_click) 
 
 ''' устанавливает, как будет выглядеть окно (надпись, размер, место) ''' 
 def set_appear(self): 
 self.setWindowTitle(txt_title) 
 self.resize(win_width, win_height) 
 self.move(win_x, win_y) 
 def initUI(self): 
 ''' создает графические элементы ''' 
 #self.опросник = allQuestions() 
 self.btn_next = QPushButton(txt_sendresults, self) 
 self.btn_test1 = QPushButton(txt_starttest1, self) 
 self.btn_test2 = QPushButton(txt_starttest2, self) 
 self.btn_test3 = QPushButton(txt_starttest3, self) 
 
 
 self.text_name = QLabel(txt_name) 
 self.text_age = QLabel(txt_age) 
 self.text_test1 = QLabel(txt_test1) 
 self.text_test2 = QLabel(txt_test2) 
 self.text_test3 = QLabel(txt_test3) 
 self.text_timer = QLabel(txt_timer) 
 self.text_timer.setFont(QFont("Times", 36, QFont.Bold)) 
 
 self.loc = QLocale(QLocale.Английский, QLocale.UnitedStates) # язык, страна 
 self.validator = QDoubleValidator() 
        self.validator.setLocale(self.loc)
 
        self.line_name = QLineEdit(txt_hintname)
 
        self.line_age = QLineEdit(txt_hintage)
        self.line_age.setValidator(self.validator) # возраст должен быть числом!
        self.line_age.setValidator(QIntValidator(7, 150))
 
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test1.setValidator(self.validator)
        self.line_test1.setValidator(QIntValidator(0, 150))
 
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test2.setValidator(self.validator)
        self.line_test2.setValidator(QIntValidator(0, 150))
 
        self.line_test3 = QLineEdit(txt_hinttest3)
        self.line_test3.setValidator(self.validator)
        self.line_test3.setValidator(QIntValidator(0, 150))
 
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
 self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter) 
 self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft) 
 self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)  
 self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft) 
 self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft) 
 self.l_line.addWidget(self.text_test1, alignment = Qt.AlignLeft) 
 self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft) 
 self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)  
 self.l_line.addWidget(self.text_test2, alignment = Qt.AlignLeft) 
 self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft)  
 self.l_line.addWidget(self.text_test3, alignment = Qt.AlignLeft) 
 self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft) 
 self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft) 
 self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)  
 self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)  
 self.h_line.addLayout(self.l_line)  
 self.h_line.addLayout(self.r_line)  
 self.setLayout(self.h_line) 
 
 def next_click(self): 
 self.hide() 
 self.prs = Person(self.line_name.text, int(self.line_age.text())) 
 self.exp = Эксперимент (self.prs, self.line_test1.text(), self.line_test2.text(), self.line_test2.text()) 
 self.fw = FinalWin(self.exp) 
 
 def timer_test1(self): 
 глобальное время 
 time = QTime(0, 0, 15) 
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
 
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
 
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
 
    def timer_bob(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        #одно приседание в 1.5 секунды
 self.timer.start (1500) 
 
 def timer3Event(self): 
 глобальное время 
 time = time.addSecs(-1) 
 self.text_timer.setText(time.toString("hh:mm:ss")) 
 if int(time.toString("hh:mm:ss")[6:8]) >= 45: 
 self.text_timer.setStyleSheet("цвет: rgb (0,255,0)") 
 elif int(time.toString("hh:mm:ss")[6:8]) <= 15: 
 self.text_timer.setStyleSheet("цвет: rgb (0,255,0)") 
 ещё: 
 self.text_timer.setStyleSheet("цвет: rgb (0,0,0)") 
 self.text_timer.setFont(QFont("Times", 36, QFont.Bold)) 
 если time.toString("hh:mm:ss") == "00:00:00": 
 self.timer.stop() 
 
 def timer_final(self): 
 глобальное время 
 time = QTime(0, 1, 0) 
 self.timer = QTimer() 
 self.timer.timeout.connect(self.timer3Event) 
 self.timer.start (1000) 
 
 def подключается (самостоятельно): 
 self.btn_next.clicked.connect(self.next_click) 
 self.btn_test1.clicked.connect(self.timer_test1) 
 self.btn_test2.clicked.connect(self.timer_bob) 
 self.btn_test3.clicked.connect(self.timer_final) 
 
 ''' устанавливает, как будет выглядеть окно (надпись, размер, место) ''' 
 def set_appear(self): 
 self.setWindowTitle(txt_title) 
 self.resize(win_width, win_height) 
 self.move(win_x, win_y)
