from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QLineEdit, QFormLayout, QVBoxLayout,
    QHBoxLayout, QApplication, QMessageBox
)
from PyQt5.QtCore import pyqtSlot, QSize, Qt
from PyQt5.QtGui import QIcon
from src.probability import solve, Pair
from src.init_pkg import init_packages
import ctypes


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()

    def setup_ui(self) -> None:
        self.setWindowIcon(QIcon("icons/title_icon.png"))
        self.setWindowTitle("Задание №7")
        self.setFixedSize(QSize(350, 430))
        
        form = QFormLayout()
        main_layout = QVBoxLayout()

        self.n1 = QLineEdit()
        self.n1.setStyleSheet('''border: 2px solid black; border-radius: 10px; height: 30px; font-size: 20px;''')
        self.n1.setAlignment(Qt.AlignCenter)
        n1_lbl = QLabel("n<sub>1</sub> : ")
        n1_lbl.setStyleSheet("font-size: 20px;")

        self.n2 = QLineEdit()
        self.n2.setStyleSheet("border: 2px solid black; border-radius: 10px; height: 30px; font-size: 20px;")
        self.n2.setAlignment(Qt.AlignCenter)
        n2_lbl = QLabel("n<sub>2</sub> : ")
        n2_lbl.setStyleSheet("font-size: 20px;")

        self.n3 = QLineEdit()
        self.n3.setStyleSheet("border: 2px solid black; border-radius: 10px; height: 30px; font-size: 20px;")
        self.n3.setAlignment(Qt.AlignCenter)
        n3_lbl = QLabel("n<sub>3</sub> : ")
        n3_lbl.setStyleSheet("font-size: 20px;")

        self.m = QLineEdit()
        self.m.setStyleSheet("border: 2px solid black; border-radius: 10px; height: 30px; font-size: 20px;")
        self.m.setAlignment(Qt.AlignCenter)
        m_lbl = QLabel("m : ")
        m_lbl.setStyleSheet("font-size: 20px;")
        
        a = QHBoxLayout()
        b = QHBoxLayout()
        c = QHBoxLayout()
        d = QHBoxLayout()

        self.a1 = QLineEdit()
        self.a1.setStyleSheet("border: 2px solid black; border-radius: 10px; height: 30px; font-size: 20px;")
        self.a1.setAlignment(Qt.AlignCenter)
        self.a2 = QLineEdit()
        self.a2.setStyleSheet("border: 2px solid black; border-radius: 10px; height: 30px; font-size: 20px;")
        self.a2.setAlignment(Qt.AlignCenter)
        
        a_left_bracket = QLabel("(")
        a_left_bracket.setStyleSheet("font-size: 35px;")
        a_right_bracket = QLabel(")")
        a_right_bracket.setStyleSheet("font-size: 35px;")

        a_lbl = QLabel("a : ")
        a_lbl.setStyleSheet("font-size: 20px;")
        a.addWidget(a_left_bracket)
        a.addWidget(self.a1)
        a.addWidget(self.a2)
        a.addWidget(a_right_bracket)

        self.b1 = QLineEdit()
        self.b1.setStyleSheet("border: 2px solid black; border-radius: 10px; height: 30px; font-size: 20px;")
        self.b1.setAlignment(Qt.AlignCenter)
        self.b2 = QLineEdit()
        self.b2.setStyleSheet("border: 2px solid black; border-radius: 10px; height: 30px; font-size: 20px;")
        self.b2.setAlignment(Qt.AlignCenter)

        b_left_bracket = QLabel("(")
        b_left_bracket.setStyleSheet("font-size: 35px;")
        b_right_bracket = QLabel(")")
        b_right_bracket.setStyleSheet("font-size: 35px;")

        b_lbl = QLabel("b : ")
        b_lbl.setStyleSheet("font-size: 20px;")
        b.addWidget(b_left_bracket)
        b.addWidget(self.b1)
        b.addWidget(self.b2)
        b.addWidget(b_right_bracket)

        self.c1 = QLineEdit()
        self.c1.setStyleSheet("border: 2px solid black; border-radius: 10px; height: 30px; font-size: 20px;")
        self.c1.setAlignment(Qt.AlignCenter)
        self.c2 = QLineEdit()
        self.c2.setStyleSheet("border: 2px solid black; border-radius: 10px; height: 30px; font-size: 20px;")
        self.c2.setAlignment(Qt.AlignCenter)

        c_left_bracket = QLabel("(")
        c_left_bracket.setStyleSheet("font-size: 35px;")
        c_right_bracket = QLabel(")")
        c_right_bracket.setStyleSheet("font-size: 35px;")

        c_lbl = QLabel("c : ")
        c_lbl.setStyleSheet("font-size: 20px;")
        c.addWidget(c_left_bracket)
        c.addWidget(self.c1)
        c.addWidget(self.c2)
        c.addWidget(c_right_bracket)

        self.d1 = QLineEdit()
        self.d1.setStyleSheet("border: 2px solid black; border-radius: 10px; height: 30px; font-size: 20px;")
        self.d1.setAlignment(Qt.AlignCenter)
        self.d2 = QLineEdit()
        self.d2.setStyleSheet("border: 2px solid black; border-radius: 10px; height: 30px; font-size: 20px;")
        self.d2.setAlignment(Qt.AlignCenter)

        d_left_bracket = QLabel("(")
        d_left_bracket.setStyleSheet("font-size: 35px;")
        d_right_bracket = QLabel(")")
        d_right_bracket.setStyleSheet("font-size: 35px;")

        d_lbl = QLabel("d : ")
        d_lbl.setStyleSheet("font-size: 20px;")
        d.addWidget(d_left_bracket)
        d.addWidget(self.d1)
        d.addWidget(self.d2)
        d.addWidget(d_right_bracket)

        form.addRow(n1_lbl, self.n1)
        form.addRow(n2_lbl, self.n2)
        form.addRow(n3_lbl, self.n3)
        form.addRow(m_lbl, self.m)
        form.addRow(a_lbl, a)
        form.addRow(b_lbl, b)
        form.addRow(c_lbl, c)
        form.addRow(d_lbl, d)

        button = QPushButton("Решить")
        button.clicked.connect(self.solve_click)
        button.setStyleSheet('''
            QPushButton {
                color: white;
                font-weight: bold;
                font-size: 25px;
                text-align: center;
                background-color: #ff073a;
                border-radius: 10px;
            }
            
            QPushButton:hover {
                background-color: #4169e1;
            }
            ''')
        
        main_layout.addLayout(form)
        main_layout.addWidget(button)

        self.setLayout(main_layout)

    @pyqtSlot()
    def solve_click(self) -> None:
        try:
            n1: int = int(self.n1.text())
            n2: int = int(self.n2.text())
            n3: int = int(self.n3.text())
            m: int = int(self.m.text())
            a: Pair = (int(self.a1.text()), int(self.a2.text()))
            b: Pair = (int(self.b1.text()), int(self.b2.text()))
            c: Pair = (int(self.c1.text()), int(self.c2.text()))
            d: Pair = (int(self.d1.text()), int(self.d2.text()))
            solve(n1, n2, n3, m, a, b, c, d)
            msg = QMessageBox(self)
            msg.setWindowTitle("Решено!")
            msg.setText("Результаты вычислений посмотрите в консоли!")
            msg.setStyleSheet("font-size: 18px; height: bold;")
            msg.show()
        except ValueError:
            msg = QMessageBox(self)
            msg.setWindowTitle("Внимание!")
            msg.setText("Все поля должны быть заполнены!")
            msg.setStyleSheet("font-size: 18px; height: bold;")
            msg.show()


# запускающая функция
def run() -> None:
    myappid = u'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    init_packages()
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
