import os
import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from Lib.SA import myWidgets, abc, pso
from Lib.myInterface.equation import AddEquation
from Lib.myInterface.design import myDesign

db = sqlite3.connect('C:\\Users\\Ahmet\\Desktop\\dkb\\venv\\Lib\\dbWidgets\\veritabani.db')

imlec =db.cursor()

komut1 = "SELECT * FROM ABC where ID=2"

imlec.execute(komut1)

veriler = imlec.fetchall()
print(veriler)
print(veriler[0][2])


# from denklem import AddEquation
if __name__ == "__main__":

    my_abc = abc.artificialBeeAlgorithm()
    # myWidgets.printInMyFormat2d(sorted(my_abc.getCandidateFoodSources()))
    myWidgets.printInMyFormat1d(my_abc.getResult())

    my_pso = pso.particleSwarmOptimization()
    # myWidgets.printInMyFormat2d8(sorted(my_pso.getParticles()))
    myWidgets.printInMyFormat1d(my_pso.getResult())

    app = QtWidgets.QApplication(sys.argv)
    myWindow = QtWidgets.QMainWindow()
    ui = myDesign()
    ui.setupUi(myWindow)
    myWindow.show()
    sys.exit(app.exec_())

my_abc = abc.artificialBeeAlgorithm()
# myWidgets.printInMyFormat2d(sorted(my_abc.getCandidateFoodSources()))
myWidgets.printInMyFormat1d(my_abc.getResult())

my_pso = pso.particleSwarmOptimization()
# myWidgets.printInMyFormat2d8(sorted(my_pso.getParticles()))
myWidgets.printInMyFormat1d(my_pso.getResult())

# myAlgorithm= abc.artificialBeeAlgorithm(ncfs=5,mi=5,dl=10,ll=0.0,ul=50.0,afv=0.95)
# myAlgorithm= abc.artificialBeeAlgorithm()
# myWidgets.printInMyFormat2d(sorted(myAlgorithm.getCandidateFoodSources()))
# myWidgets.printInMyFormat1d(myAlgorithm.getResult())
