from imageai.Detection import ObjectDetection
from PyQt5 import QtCore, QtGui, QtWidgets
from colorthief import ColorThief
import resource_rc
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PIL import Image
from PyQt5.QtCore import QThread, pyqtSignal
from collections import Counter
import sys
import cv2
import time
import csv
import numpy
import webbrowser
import datetime



class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1170, 1043)
        MainWindow.setStyleSheet("")
        MainWindow.setFixedSize(1170, 1043)
        self.Widget = QtWidgets.QWidget(MainWindow)
        self.Widget.setStyleSheet("QWidget#Widget{background-color:qlineargradient(spread:pad, x1:0.065, y1:0.119, x2:0.955, y2:0.9375, stop:0 rgba(245, 227, 230, 255), stop:1 rgba(189, 216, 254, 255))}\n"
"")
        self.Widget.setObjectName("Widget")
        self.label = QtWidgets.QLabel(self.Widget)
        self.label.setGeometry(QtCore.QRect(20, 0, 461, 61))
        self.label.setStyleSheet("font: 75 24pt \"Comic Sans MS\";\n"
"color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Widget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 301, 31))
        self.label_2.setStyleSheet("font: 75 12pt \"Comic Sans MS\";\n"
"color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.Widget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 100, 481, 31))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
" border: 2px solid gray;\n"
" border-radius: 10px;\n"
" padding-left: 10px;\n"
" padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(189, 216, 254)\n"
"}\n"
"\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.Widget)
        self.pushButton.setGeometry(QtCore.QRect(520, 100, 111, 35))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"color:#fff;\n"
"font: 75 8pt \"Comic Sans MS\";\n"
"background-color:qlineargradient(spread:pad, x1:0.06, y1:0.119318, x2:1, y2:1, stop:0 rgba(189, 216, 254, 255), stop:1 rgba(225, 134, 180, 255))\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.Widget)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 481, 361))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Widget)
        self.label_4.setGeometry(QtCore.QRect(30, 540, 301, 31))
        self.label_4.setStyleSheet("font: 75 12pt \"Comic Sans MS\";\n"
"color:rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 580, 111, 35))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"color:#fff;\n"
"font: 75 8pt \"Comic Sans MS\";\n"
"background-color:qlineargradient(spread:pad, x1:0.06, y1:0.119318, x2:1, y2:1, stop:0 rgba(189, 216, 254, 255), stop:1 rgba(225, 134, 180, 255))\n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.Widget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 580, 111, 35))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"color:#fff;\n"
"font: 75 8pt \"Comic Sans MS\";\n"
"background-color:qlineargradient(spread:pad, x1:0.06, y1:0.119318, x2:1, y2:1, stop:0 rgba(189, 216, 254, 255), stop:1 rgba(225, 134, 180, 255))\n"
"\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.Widget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 630, 550, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.label_5 = QtWidgets.QLabel(self.Widget)
        self.label_5.setGeometry(QtCore.QRect(680, 60, 301, 31))
        self.label_5.setStyleSheet("font: 75 12pt \"Comic Sans MS\";\n"
"color:rgb(255, 255, 255)")
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.Widget)
        self.pushButton_4.setGeometry(QtCore.QRect(680, 100, 111, 35))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"color:#fff;\n"
"font: 75 8pt \"Comic Sans MS\";\n"
"background-color:qlineargradient(spread:pad, x1:0.06, y1:0.119318, x2:1, y2:1, stop:0 rgba(189, 216, 254, 255), stop:1 rgba(225, 134, 180, 255))\n"
"\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(self.Widget)
        self.label_6.setGeometry(QtCore.QRect(680, 150, 301, 31))
        self.label_6.setStyleSheet("font: 75 12pt \"Comic Sans MS\";\n"
"color:rgb(255, 255, 255)")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.Widget)
        self.label_7.setGeometry(QtCore.QRect(680, 190, 261, 31))
        self.label_7.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.Widget)
        self.label_8.setGeometry(QtCore.QRect(680, 230, 301, 31))
        self.label_8.setStyleSheet("font: 75 12pt \"Comic Sans MS\";\n"
"color:rgb(255, 255, 255)")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.Widget)
        self.label_9.setGeometry(QtCore.QRect(680, 270, 101, 31))
        self.label_9.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Widget)
        self.label_10.setGeometry(QtCore.QRect(790, 270, 101, 31))
        self.label_10.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Widget)
        self.label_11.setGeometry(QtCore.QRect(900, 270, 101, 31))
        self.label_11.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Widget)
        self.label_12.setGeometry(QtCore.QRect(680, 320, 301, 31))
        self.label_12.setStyleSheet("font: 75 12pt \"Comic Sans MS\";\n"
"color:rgb(255, 255, 255)")
        self.label_12.setObjectName("label_12")
        self.pushButton_5 = QtWidgets.QPushButton(self.Widget)
        self.pushButton_5.setGeometry(QtCore.QRect(680, 360, 111, 35))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"color:#fff;\n"
"font: 75 8pt \"Comic Sans MS\";\n"
"background-color:qlineargradient(spread:pad, x1:0.06, y1:0.119318, x2:1, y2:1, stop:0 rgba(189, 216, 254, 255), stop:1 rgba(225, 134, 180, 255))\n"
"\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.Widget)
        self.pushButton_6.setGeometry(QtCore.QRect(810, 360, 111, 35))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"color:#fff;\n"
"font: 75 8pt \"Comic Sans MS\";\n"
"background-color:qlineargradient(spread:pad, x1:0.06, y1:0.119318, x2:1, y2:1, stop:0 rgba(189, 216, 254, 255), stop:1 rgba(225, 134, 180, 255))\n"
"\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_13 = QtWidgets.QLabel(self.Widget)
        self.label_13.setGeometry(QtCore.QRect(680, 410, 261, 191))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.Widget)
        self.label_14.setGeometry(QtCore.QRect(680, 620, 141, 31))
        self.label_14.setStyleSheet("font: 75 12pt \"Comic Sans MS\";\n"
"color:rgb(255, 255, 255)")
        self.label_14.setObjectName("label_14")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(680, 710, 91, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
" border: 2px solid gray;\n"
" border-radius: 10px;\n"
" padding-left: 10px;\n"
" padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(189, 216, 254)\n"
"}\n"
"\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(780, 710, 91, 31))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
" border: 2px solid gray;\n"
" border-radius: 10px;\n"
" padding-left: 10px;\n"
" padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(189, 216, 254)\n"
"}\n"
"\n"
"")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.Widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(880, 710, 91, 31))
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
" border: 2px solid gray;\n"
" border-radius: 10px;\n"
" padding-left: 10px;\n"
" padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(189, 216, 254)\n"
"}\n"
"\n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.Widget)
        self.pushButton_7.setGeometry(QtCore.QRect(680, 660, 111, 35))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"color:#fff;\n"
"font: 75 8pt \"Comic Sans MS\";\n"
"background-color:qlineargradient(spread:pad, x1:0.06, y1:0.119318, x2:1, y2:1, stop:0 rgba(189, 216, 254, 255), stop:1 rgba(225, 134, 180, 255))\n"
"\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_15 = QtWidgets.QLabel(self.Widget)
        self.label_15.setGeometry(QtCore.QRect(680, 760, 181, 31))
        self.label_15.setStyleSheet("font: 75 12pt \"Comic Sans MS\";\n"
"color:rgb(255, 255, 255)")
        self.label_15.setObjectName("label_15")
        self.pushButton_8 = QtWidgets.QPushButton(self.Widget)
        self.pushButton_8.setGeometry(QtCore.QRect(680, 800, 131, 35))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"color:#fff;\n"
"font: 75 8pt \"Comic Sans MS\";\n"
"background-color:qlineargradient(spread:pad, x1:0.06, y1:0.119318, x2:1, y2:1, stop:0 rgba(189, 216, 254, 255), stop:1 rgba(225, 134, 180, 255))\n"
"\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_16 = QtWidgets.QLabel(self.Widget)
        self.label_16.setGeometry(QtCore.QRect(680, 850, 201, 31))
        self.label_16.setStyleSheet("font: 75 12pt \"Comic Sans MS\";\n"
"color:rgb(255, 255, 255)")
        self.label_16.setObjectName("label_16")
        self.pushButton_9 = QtWidgets.QPushButton(self.Widget)
        self.pushButton_9.setGeometry(QtCore.QRect(680, 890, 131, 35))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"color:#fff;\n"
"font: 75 8pt \"Comic Sans MS\";\n"
"background-color:qlineargradient(spread:pad, x1:0.06, y1:0.119318, x2:1, y2:1, stop:0 rgba(189, 216, 254, 255), stop:1 rgba(225, 134, 180, 255))\n"
"\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.Widget)
        self.pushButton_10.setGeometry(QtCore.QRect(680, 960, 171, 35))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"color:#fff;\n"
"font: 75 8pt \"Comic Sans MS\";\n"
"background-color:qlineargradient(spread:pad, x1:0.06, y1:0.119318, x2:1, y2:1, stop:0 rgba(189, 216, 254, 255), stop:1 rgba(225, 134, 180, 255))\n"
"\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.Widget)
        self.pushButton_11.setGeometry(QtCore.QRect(870, 960, 111, 35))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"color:#fff;\n"
"font: 75 8pt \"Comic Sans MS\";\n"
"background-color:qlineargradient(spread:pad, x1:0.06, y1:0.119318, x2:1, y2:1, stop:0 rgba(189, 216, 254, 255), stop:1 rgba(225, 134, 180, 255))\n"
"\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        MainWindow.setCentralWidget(self.Widget)

        self.imageSpireImage = ""
        self.imageSpireImageResized = ""
        self.tableRowCount = 0
        self.imagePath = ""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ImageSpire By Aditya"))
        self.label.setText(_translate("MainWindow", "Welcome! to ImageSpire"))
        self.label_2.setText(_translate("MainWindow", "Please pick an image to continue"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Image file path"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Images/imagenotfound.jpg\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Pixel RGB Data"))
        self.pushButton_2.setText(_translate("MainWindow", "Generate"))
        self.pushButton_3.setText(_translate("MainWindow", "Export to CSV"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Position X"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Position Y"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Red"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Green"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Blue"))
        self.label_5.setText(_translate("MainWindow", "Color palettes"))
        self.pushButton_4.setText(_translate("MainWindow", "Generate"))
        self.label_6.setText(_translate("MainWindow", "Dominant color:"))
        self.label_8.setText(_translate("MainWindow", "Palettes:"))
        self.label_12.setText(_translate("MainWindow", "Gray scale image"))
        self.pushButton_5.setText(_translate("MainWindow", "Transform"))
        self.pushButton_6.setText(_translate("MainWindow", "Save Image"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Images/imagenotfoundalt.jpg\"/></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "H, S, B values"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Hue"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Saturation"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Brightness"))
        self.pushButton_7.setText(_translate("MainWindow", "Generate"))
        self.label_15.setText(_translate("MainWindow", "Object Detection:"))
        self.pushButton_8.setText(_translate("MainWindow", "Detect Objects "))
        self.label_16.setText(_translate("MainWindow", "Facial Recognization:"))
        self.pushButton_9.setText(_translate("MainWindow", "Recognize "))
        self.pushButton_10.setText(_translate("MainWindow", "Github Link"))
        self.pushButton_11.setText(_translate("MainWindow", "Quit"))

        self.pushButton.clicked.connect(self.openFileNameDialog)
        self.pushButton_2.clicked.connect(self.generateRGBData)
        self.pushButton_3.clicked.connect(self.exportRGBData)
        self.pushButton_4.clicked.connect(self.generateColorPalette)
        self.pushButton_5.clicked.connect(self.transFormToGrayScale)
        self.pushButton_6.clicked.connect(self.saveGrayScaleImage)
        self.pushButton_7.clicked.connect(self.getHSBValue)
        self.pushButton_8.clicked.connect(self.objectDetection)
        self.pushButton_9.clicked.connect(self.facialRecognization)
        self.pushButton_10.clicked.connect(self.openBrowser)
        self.pushButton_11.clicked.connect(self.closeWindow)
        
        
 

    def generateRGBData(self):
        
        (width, height) = self.imageSpireImageResized.size
        self.tableWidget.setRowCount(int(width * height))

        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setItem(0, 0, QTableWidgetItem(str(1)))

        self.worker = RGBDataThread(self.imageSpireImageResized)
        self.worker.start()
        self.worker.updateRowCount.connect(self.eventupdateRowCount)
        self.worker.updateX.connect(self.eventUpdateX)
        self.worker.updateY.connect(self.eventUpdateY)
        self.worker.updateR.connect(self.eventUpdateR)
        self.worker.updateG.connect(self.eventUpdateG)
        self.worker.updateB.connect(self.eventUpdateB)



    def eventupdateRowCount(self, value):
        self.tableRowCount = value


    def eventUpdateX(self, value):
        self.tableWidget.setItem(self.tableRowCount, 0, QTableWidgetItem(str(value)))

    def eventUpdateY(self, value):
        self.tableWidget.setItem(self.tableRowCount, 1, QTableWidgetItem(str(value)))

    def eventUpdateR(self, value):
        self.tableWidget.setItem(self.tableRowCount, 2, QTableWidgetItem(str(value)))

    def eventUpdateG(self, value):
        self.tableWidget.setItem(self.tableRowCount, 3, QTableWidgetItem(str(value)))

    def eventUpdateB(self, value):
        self.tableWidget.setItem(self.tableRowCount, 4, QTableWidgetItem(str(value)))


    def exportRGBData(self):
        rgbImage = self.imageSpireImageResized.convert('RGB')
        (width, height) = rgbImage.size
        pixelData = []
        for x in range(width):
                for y in range(height):
                        (r, g, b) = rgbImage.getpixel((x, y))
                        pixelData.append([x, y, r, g, b])
        with open("pixels.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Position X", "Position Y", "Red", "Green", "Blue"])
                writer.writerows(pixelData)
        self.eventWorkerFinished()


    def transFormToGrayScale(self):
        grayScaleimage = self.imageSpireImageResized.convert("L")
        resizedGrayScaleImage = grayScaleimage.resize((261, 191))
        resizedGrayScaleImage.save("resizeGrayImage.jpg")
        qpixmap = QPixmap("resizeGrayImage.jpg")
        self.label_13.setPixmap(qpixmap)

    def saveGrayScaleImage(self):
        grayScaleimage = self.imageSpireImage.convert("L")
        grayScaleimage.save("GrayImage.jpg")
        self.messageBox("Save Image", "GrayImage.jpg saved successfully.")



    def eventWorkerFinished(self):
        self.messageBox("Export", "RGBData.csv created successfully.")

        
    def messageBox(self, title, message):
        messageBoxWidget = QMessageBox()
        messageBoxWidget.setWindowTitle(title)
        messageBoxWidget.setIcon(QMessageBox.Information)
        messageBoxWidget.setText(message)
        messageBoxWidget.setStandardButtons(QMessageBox.Ok)
        messageBoxWidget.exec_()

                        
    def generateColorPalette(self):

        self.worker = ColorPaletteThread(self.imagePath)
        self.worker.start()
        self.worker.dominantColorSignal.connect(self.setDominantColor)
        self.worker.paletteSignal.connect(self.setpaletteColor)



    def setDominantColor(self, value):
        self.label_7.setStyleSheet("background-color:rgb("+ str(value[0]) + "," + str(value[1]) + "," + str(value[2]) +")")

    def setpaletteColor(self, value):
        value1 = value[0]
        value2 = value[1]
        value3 = value[2]
        self.label_9.setStyleSheet("background-color:rgb("+ str(value1[0]) + "," + str(value1[1]) + "," + str(value1[2]) +")")
        self.label_10.setStyleSheet("background-color:rgb("+ str(value2[0]) + "," + str(value2[1]) + "," + str(value2[2]) +")")
        self.label_11.setStyleSheet("background-color:rgb("+ str(value3[0]) + "," + str(value3[1]) + "," + str(value3[2]) +")")

    def getHSBValue(self):
        self.worker = HSBDataThread(self.imageSpireImageResized)
        self.worker.start()
        self.worker.updateHSB.connect(self.setHSBValues)


    def setHSBValues(self, value):
        self.lineEdit_2.setText(str(value[0]))
        self.lineEdit_3.setText(str(value[1]))
        self.lineEdit_4.setText(str(value[2]))

    def facialRecognization(self):
        self.worker = FacialRecognizationThread(self.imagePath)
        self.worker.start()

    def objectDetection(self):
        self.worker = ObjectDetectionThread(self.imagePath)
        self.worker.start()

    def openBrowser(self):
        webbrowser.open('https://github.com/adityaxp')

    def closeWindow(self):
        sys.exit(app.exec_())

    def openFileNameDialog(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "C:\\Users\\Aditya\\PythonGUIProjects\\PyQt5Projects\\ImageSpire\\Images", "All Files (*);;Python Files (*.py);; PNG Files (*.png)" )
        if fname:
                self.lineEdit.setText(fname[0])
                self.imagePath = fname[0]
                image = Image.open(fname[0])
                self.imageSpireImage = image
                resizedImage = image.resize((481, 361))
                self.imageSpireImageResized = resizedImage
                convertedImage = resizedImage.convert("RGBA")
                data = convertedImage.tobytes("raw","RGBA")
                qImage =  QtGui.QImage(data, convertedImage.size[0], convertedImage.size[1], QtGui.QImage.Format_RGBA8888)
                qpixmap = QtGui.QPixmap.fromImage(qImage)
                self.label_3.setPixmap(qpixmap)





class ColorPaletteThread(QThread):

        def __init__(self, imagePath):
                super(ColorPaletteThread,self).__init__()
                self.imagePath = imagePath

        
        dominantColorSignal = pyqtSignal(tuple)
        paletteSignal = pyqtSignal(list)

        def run(self):
                colorThief = ColorThief(self.imagePath)
                dominantColor = colorThief.get_color(quality=1)
                palette = colorThief.get_palette(color_count=2)
                print(dominantColor)
                print(palette)
                self.dominantColorSignal.emit(dominantColor)
                self.paletteSignal.emit(palette)
                self.quit()


class ObjectDetectionThread(QThread):
        def __init__(self, imagePath):
                super(ObjectDetectionThread,self).__init__()
                self.imagePath = imagePath

        def run(self):
                detector = ObjectDetection()

                detector.setModelTypeAsRetinaNet()
                detector.setModelTypeAsTinyYOLOv3()
                detector.setModelPath("tiny-yolov3.pt")
                detector.loadModel()
                detections = detector.detectObjectsFromImage(self.imagePath, output_image_path="DetectedObjects.jpg", minimum_percentage_probability=30)
                capture = cv2.imread("DetectedObjects.jpg")
                capture = cv2.resize(capture, (640, 480))
                cv2.imshow('Object Detection',capture)
                cv2.waitKey()
                self.quit()



        
class HSBDataThread(QThread):
        def __init__(self, imageSpireImageResized):
                super(HSBDataThread,self).__init__()
                self.imageSpireImageResized = imageSpireImageResized

        updateHSB = pyqtSignal(list)
        
        def run(self):
                hsb = self.imageSpireImageResized.convert("HSV")
                h, s, b = hsb.split()
                h_int = [i for i in h.getdata()]
                s_int = [i for i in s.getdata()]
                b_int = [i for i in b.getdata()]
                hueCount = Counter(h_int)
                saturationCount = Counter(s_int)
                brightnessCount = Counter(b_int)
                hue = hueCount.most_common(1)
                saturation = saturationCount.most_common(1)
                brightness= brightnessCount.most_common(1)
                HSBData = [hue[0][0], saturation[0][0], brightness[0][0]]
                self.updateHSB.emit(HSBData)


class RGBDataThread(QThread):

        def __init__(self, imageSpireImageResized):
                super(RGBDataThread,self).__init__()
                self.imageSpireImageResized = imageSpireImageResized

        updateX = pyqtSignal(int)
        updateY = pyqtSignal(int)
        updateR = pyqtSignal(int)
        updateG = pyqtSignal(int)
        updateB = pyqtSignal(int)
        updateRowCount = pyqtSignal(int)

        def run(self):
                rgb_image = self.imageSpireImageResized.convert('RGB')
                (width, height) = rgb_image.size
                rowCount = 0
                for x in range(width):
                        for y in range(height):
                                (r, g, b) = rgb_image.getpixel((x, y))
                               # print(f"Pixel at ({x}, {y}): R={r}, G={g}, B={b}")
                                self.updateX.emit(x)
                                self.updateY.emit(y)
                                self.updateR.emit(r)
                                self.updateG.emit(g)
                                self.updateB.emit(b)
                                rowCount = rowCount + 1
                                self.updateRowCount.emit(rowCount)
                                
                self.quit()

class FacialRecognizationThread(QThread):


        def __init__(self, imagePath):
                super(FacialRecognizationThread,self).__init__()
                self.imagePath = imagePath


        def run(self):
                capture = cv2.imread(self.imagePath)
                humanCascade = cv2.CascadeClassifier('haarcascade_face.xml')
                
                gray = cv2.cvtColor(capture, cv2.COLOR_BGR2GRAY)
                humans = humanCascade.detectMultiScale(gray, 1.9, 1)


                for (x,y,w,h) in humans:
                        cv2.rectangle(capture,(x,y),(x+w,y+h),(255,0,0),2)

                capture = cv2.resize(capture, (640, 480))
                cv2.imshow('Facial Recognization',capture)
                cv2.waitKey()
                self.quit()
                        
                        
                



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


