# напиши здесь код третьего экрана приложения#final_win.py 
из PyQt5.QtCore импорт Qt, QTimer, QTime, QLocale 
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений 
из PyQt5.QtWidgets импорт ( 
 QApplication, QWidget,  
 QHBoxLayout, QVBoxLayout, QGridLayout,  
 QGroupBox, QRadioButton, 
 QPushButton, QLabel, QListWidget, QLineEdit) 
 
из instr импорт * 
 
класс FinalWin(QWidget): 
 def __init__(self, exp): 
 ''' окно, в котором проводится опрос ''' 
 super().__init__() 
 
 #получаем данные об эксперименте 
 self.exp = exp 
 
 # создаём и настраиваем графические элелементы: 
 self.initUI() 
 
 #устанавливает связи между элементами 
 # self.connectes() 
 
 #устанавливает, как будет выглядеть окно (надпись, размер, место) 
 self.set_appear() 
 
 # старт: 
        self.show()
 
    def results(self):
        if self.exp.person.age < 7:
            self.index = 0
            return "нет данных для такого возраста"
        self.index = (4 * (int(self.exp.test1) + int(self.exp.test2) + int(self.exp.test3)) - 200) / 10
 если self.exp.person.age == 7 или self.exp.person.age == 8: 
 если self.index >= 21: 
 возврат txt_res1 
 elif self.index < 21 и self.index >= 17: 
 возврат txt_res2 
 elif self.index < 17 и self.index >= 12: 
 возврат txt_res3 
 elif self.index < 12 и self.index >= 6.5: 
 возврат txt_res4 
 ещё: 
 возврат txt_res5 
 если self.exp.person.age == 9 или self.exp.person.age == 10: 
 если self.index>= 19.5: 
 возврат txt_res1 
 elif self.index < 19.5 и self.index >= 15.5: 
 возврат txt_res2 
 elif self.index < 15.5 и self.index >= 10.5: 
 возврат txt_res3 
 elif self.index < 10.5 и self.index >= 5: 
 возврат txt_res4 
 ещё: 
 возврат txt_res5 
 если self.exp.person.age == 11 или self.exp.person.age == 12: 
 если self.index>= 18: 
 возврат txt_res1 
 elif self.index < 18 и self.index >= 14: 
 возврат txt_res2 
            elif self.index < 14 and self.index >= 9:
                return txt_res3
            elif self.index < 9 and self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.person.age == 13 or self.exp.person.age == 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 16.5 and self.index >= 12.5:
                return txt_res2
            elif self.index < 12.5 and self.index >= 7.5:
                return txt_res3
            elif self.index < 7.5 and self.index >= 2:
                return txt_res4
            else:
                return txt_res5
        if self.exp.person.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index >= 11:
                return txt_res2
            elif self.index < 11 and self.index >= 6:
                return txt_res3
            elif self.index < 6 and self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5
 
 def initUI(self): 
 ''' создает графические элементы ''' 
 self.workh_text = QLabel(txt_workheart + self.results()) 
 self.index_text = QLabel(txt_index + str(self.index)) 
 
 self.layout_line = QVBoxLayout() 
 self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter) 
 self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)  
 self.setLayout(self.layout_line) 
 
 ''' устанавливает, как будет выглядеть окно (надпись, размер, место) ''' 
 def set_appear(self): 
 self.setWindowTitle(txt_finalwin) 
 self.resize(win_width, win_height) 
