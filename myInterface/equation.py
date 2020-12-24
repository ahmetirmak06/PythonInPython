from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import os


class AddEquation(object):
    toplam = 0

    def setupUi(self, DenklemEkle):
        DenklemEkle.setObjectName("DenklemEkle")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DenklemEkle.setWindowIcon(icon)
        DenklemEkle.resize(1000, 500)
        DenklemEkle.setMinimumSize(QtCore.QSize(1000, 500))
        DenklemEkle.setMaximumSize(QtCore.QSize(1000, 500))
        DenklemEkle.setBaseSize(QtCore.QSize(0, 0))
        DenklemEkle.setContextMenuPolicy(QtCore.Qt.NoContextMenu)

        self.centralwidget = QtWidgets.QWidget(DenklemEkle)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 150, 31, 51))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.txt_ksayi = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_ksayi.setGeometry(QtCore.QRect(70, 125, 71, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.txt_ksayi.setFont(font)
        self.txt_ksayi.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.txt_ksayi.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_ksayi.setMaxLength(2)
        self.txt_ksayi.setCursorPosition(0)
        self.txt_ksayi.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.txt_ksayi.setObjectName("txt_ksayi")
        self.txt_ksayi.setValidator(QIntValidator(0, 10))

        self.txt_sabit_deger = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sabit_deger.setGeometry(QtCore.QRect(370, 140, 61, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.txt_sabit_deger.setFont(font)
        self.txt_sabit_deger.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.txt_sabit_deger.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.txt_sabit_deger.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.txt_sabit_deger.setInputMask("")
        self.txt_sabit_deger.setText("")
        self.txt_sabit_deger.setMaxLength(2)
        self.txt_sabit_deger.setCursorPosition(0)
        self.txt_sabit_deger.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.txt_sabit_deger.setObjectName("txt_sabit_deger")
        self.txt_sabit_deger.setValidator(QIntValidator(0, 10))

        self.txt_us = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_us.setGeometry(QtCore.QRect(180, 120, 31, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.txt_us.setFont(font)
        self.txt_us.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.txt_us.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_us.setMaxLength(2)
        self.txt_us.setCursorPosition(0)
        self.txt_us.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.txt_us.setObjectName("txt_us")
        self.txt_us.setValidator(QIntValidator(0, 10))

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 160, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setMaxVisibleItems(2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect(320, 170, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox2.setFont(font)
        self.comboBox2.setMaxVisibleItems(2)
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")

        self.lbl_denklem = QtWidgets.QLabel(self.centralwidget)
        self.lbl_denklem.setGeometry(QtCore.QRect(10, 10, 971, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_denklem.setFont(font)
        self.lbl_denklem.setText("")
        self.lbl_denklem.setObjectName("lbl_denklem")

        self.btn_ekle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ekle.setGeometry(QtCore.QRect(90, 250, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_ekle.setFont(font)
        self.btn_ekle.setObjectName("btn_ekle")
        self.btn_ekle.clicked.connect(self.e_ekle)
        self.btn_ekle.setEnabled(True)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.btn_sil = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sil.setGeometry(QtCore.QRect(90, 310, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_sil.setFont(font)
        self.btn_sil.setObjectName("btn_sil")
        self.btn_sil.clicked.connect(self.e_sil)

        self.btn_kaydet = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kaydet.setGeometry(QtCore.QRect(90, 370, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_kaydet.setFont(font)
        self.btn_kaydet.setObjectName("btn_kaydet")
        self.btn_kaydet.clicked.connect(self.d_kaydet)

        self.btn_cikis = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cikis.setGeometry(QtCore.QRect(820, 430, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_cikis.setFont(font)
        self.btn_cikis.setObjectName("btn_cikis")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 180, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.btn_st_ekle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_st_ekle.setGeometry(QtCore.QRect(340, 250, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_st_ekle.setFont(font)
        self.btn_st_ekle.setObjectName("btn_st_ekle")
        self.btn_st_ekle.clicked.connect(self.st_ekle)

        DenklemEkle.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DenklemEkle)
        self.statusbar.setObjectName("statusbar")
        DenklemEkle.setStatusBar(self.statusbar)

        self.retranslateUi(DenklemEkle)
        self.btn_cikis.clicked.connect(DenklemEkle.close)
        QtCore.QMetaObject.connectSlotsByName(DenklemEkle)

    def d_kaydet(self):
        try:
            with open("denklem.txt", "w") as dosya:
                dosya.write(self.lbl_denklem.text())
        except:
            print(self.lbl_denklem.setText("Dosya Oluşturulamadı."))

    def e_ekle(self):
        self.yazi1 = " "
        self.yazi1 = self.comboBox.currentText() + self.txt_ksayi.text() + "x**" + self.txt_us.text()
        if len(self.txt_ksayi.text()) > 0 and len(self.txt_us.text()) > 0:
            self.lbl_denklem.setText(self.lbl_denklem.text() + self.yazi1)
            self.txt_ksayi.setText("")
            self.txt_us.setText("")

    def e_sil(self):
        self.lbl_denklem.setText("")
        self.btn_st_ekle.setEnabled(True)

    def st_ekle(self):
        self.yazi = " "
        self.yazi = self.comboBox2.currentText() + self.txt_sabit_deger.text()
        self.lbl_denklem.setText(self.lbl_denklem.text() + self.yazi)
        self.txt_sabit_deger.setText("")
        self.btn_st_ekle.setEnabled(False)

    def retranslateUi(self, DenklemEkle):
        _translate = QtCore.QCoreApplication.translate
        DenklemEkle.setWindowTitle(_translate("DenklemEkle", "Denklem Ekle"))
        self.label.setText(_translate("DenklemEkle", "X"))
        self.comboBox.setCurrentText(_translate("DenklemEkle", "+"))
        self.comboBox.setItemText(0, _translate("DenklemEkle", "+"))
        self.comboBox.setItemText(1, _translate("DenklemEkle", "-"))
        self.comboBox2.setCurrentText(_translate("DenklemEkle", "+"))
        self.comboBox2.setItemText(0, _translate("DenklemEkle", "+"))
        self.comboBox2.setItemText(1, _translate("DenklemEkle", "-"))
        self.btn_ekle.setText(_translate("DenklemEkle", "EKLE"))
        self.label_3.setText(_translate("DenklemEkle", "SABİT TERİM"))
        self.btn_sil.setText(_translate("DenklemEkle", "TEMİZLE"))
        self.btn_kaydet.setText(_translate("DenklemEkle", "DENKLEMİ  KAYDET"))
        self.btn_cikis.setText(_translate("DenklemEkle", "ÇIKIŞ"))
        self.btn_st_ekle.setText(_translate("DenklemEkle", "SABİT TERİM EKLE"))
        self.label_2.setText(
            _translate("DenklemEkle",
                       "--> Bu kutucuğu denklemin sabit terimini girmek için kullanınız \n      Sabit Değer Bir Kez Eklenebilir"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    DenklemEkle = QtWidgets.QMainWindow()
    ui = AddEquation()
    ui.setupUi(DenklemEkle)
    DenklemEkle.show()
    sys.exit(app.exec_())
