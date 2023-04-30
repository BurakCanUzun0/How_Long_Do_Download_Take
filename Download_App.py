import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("How Long Do Download Take ? (Gb-MB/s)")
        self.deger = QtWidgets.QLabel()
        self.deger.setText("I'm ready to calculate :)")

        self.yazı_alanı1 = QtWidgets.QLineEdit() #Üzerine yazı yazabildiğimiz yazı alanını oluşturuyoruz.
        self.yazı_alanı2 = QtWidgets.QLineEdit()
        self.hesapla = QtWidgets.QPushButton("Calculate the time")
        self.setGeometry(750,450,400,250)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazı_alanı1)
        v_box.addWidget(self.yazı_alanı2)
        v_box.addWidget(self.hesapla)
        v_box.addWidget(self.deger)
        v_box.addStretch()

        self.setLayout(v_box)
        self.hesapla.clicked.connect(self.click)
        self.show()
    def click(self):
        yazı1 = self.yazı_alanı1.text()
        yazı2 = self.yazı_alanı2.text()
        try:
            yazı1 = float(yazı1)
            yazı2 = float(yazı2)
            saat = int(yazı1*1024/yazı2/3600)
            dakika = round(((yazı1*1024/yazı2/60)%60))
            self.deger.setText("Your download will take {} hour and {} minutes.".format(saat,dakika))


        except:
            self.deger.setText('Please, fill the blanks. Also you have to use "." (dot mark) for the fractional value.')



app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())