from PyQt5 import QtCore, QtGui, QtWidgets
import random
import csv
from datetime import datetime


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(873, 861)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 10, 671, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(931, 91))
        font = QtGui.QFont()
        font.setFamily("Outfit ExtraBold")
        font.setPointSize(38)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setStyleSheet("text-decoration: underline;\n"
                                 "font: 81 38pt \"Outfit ExtraBold\";")
        self.label.setLineWidth(4)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(300, 130, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Outfit Black")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 87 22pt \"Outfit Black\";\n"
                                   "text-decoration:underline;\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.SignalFrequency = QtWidgets.QLabel(Dialog)
        self.SignalFrequency.setGeometry(QtCore.QRect(20, 280, 221, 41))
        self.SignalFrequency.setStyleSheet("font: 81 18pt \"Outfit ExtraBold\";")
        self.SignalFrequency.setObjectName("SignalFrequency")
        self.n1 = QtWidgets.QSpinBox(Dialog)
        self.n1.setEnabled(True)
        self.n1.setGeometry(QtCore.QRect(450, 280, 151, 31))
        self.n1.setStyleSheet("font: 81 10pt \"Outfit ExtraBold\";")
        self.n1.setMaximum(99999999)
        self.n1.setObjectName("n1")
        self.SignalFrequency_2 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_2.setGeometry(QtCore.QRect(20, 350, 221, 41))
        self.SignalFrequency_2.setStyleSheet("font: 81 18pt \"Outfit ExtraBold\";")
        self.SignalFrequency_2.setObjectName("SignalFrequency_2")
        self.SignalFrequency_3 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_3.setGeometry(QtCore.QRect(20, 420, 381, 41))
        self.SignalFrequency_3.setStyleSheet("font: 81 18pt \"Outfit ExtraBold\";")
        self.SignalFrequency_3.setObjectName("SignalFrequency_3")
        self.SignalFrequency_5 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_5.setGeometry(QtCore.QRect(20, 490, 221, 41))
        self.SignalFrequency_5.setStyleSheet("font: 81 18pt \"Outfit ExtraBold\";")
        self.SignalFrequency_5.setObjectName("SignalFrequency_5")
        self.SignalFrequency_6 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_6.setGeometry(QtCore.QRect(20, 560, 351, 41))
        self.SignalFrequency_6.setStyleSheet("font: 81 18pt \"Outfit ExtraBold\";")
        self.SignalFrequency_6.setObjectName("SignalFrequency_6")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(450, 420, 121, 31))
        self.spinBox_2.setStyleSheet("font: 81 10pt \"Outfit ExtraBold\";")
        self.spinBox_2.setMaximum(360)
        self.spinBox_2.setObjectName("spinBox_2")
        self.SignalFrequency_8 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_8.setGeometry(QtCore.QRect(570, 430, 21, 16))
        self.SignalFrequency_8.setStyleSheet("font: 63 11pt \"Montserrat\";")
        self.SignalFrequency_8.setObjectName("SignalFrequency_8")
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(450, 490, 121, 31))
        self.spinBox_3.setStyleSheet("font: 81 10pt \"Outfit ExtraBold\";")
        self.spinBox_3.setMaximum(99999999)
        self.spinBox_3.setObjectName("spinBox_3")
        self.SignalFrequency_10 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_10.setGeometry(QtCore.QRect(570, 500, 31, 16))
        self.SignalFrequency_10.setStyleSheet("font: 81 13pt \"Outfit ExtraBold\";")
        self.SignalFrequency_10.setObjectName("SignalFrequency_10")
        self.nmax = QtWidgets.QSpinBox(Dialog)
        self.nmax.setGeometry(QtCore.QRect(450, 560, 121, 31))
        self.nmax.setStyleSheet("font: 81 10pt \"Outfit ExtraBold\";")
        self.nmax.setMaximum(99999999)
        self.nmax.setObjectName("nmax")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(790, 290, 71, 22))
        self.comboBox_3.setStyleSheet("font: 81 10pt \"Outfit ExtraBold\";")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 740, 321, 51))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("font: 81 15pt \"Outfit ExtraBold\";\n"
                                      "Background-color: #7DF9FF")
        self.pushButton.setObjectName("pushButton")
        self.n1_2 = QtWidgets.QSpinBox(Dialog)
        self.n1_2.setEnabled(True)
        self.n1_2.setGeometry(QtCore.QRect(650, 280, 131, 31))
        self.n1_2.setStyleSheet("font: 81 10pt \"Outfit ExtraBold\";")
        self.n1_2.setMaximum(99999999)
        self.n1_2.setObjectName("n1_2")
        self.SignalFrequency_12 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_12.setGeometry(QtCore.QRect(620, 280, 21, 20))
        self.SignalFrequency_12.setStyleSheet("font: 81 18pt \"Outfit ExtraBold\";")
        self.SignalFrequency_12.setObjectName("SignalFrequency_12")
        self.SignalFrequency_13 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_13.setGeometry(QtCore.QRect(610, 420, 21, 20))
        self.SignalFrequency_13.setStyleSheet("font: 81 18pt \"Outfit ExtraBold\";")
        self.SignalFrequency_13.setObjectName("SignalFrequency_13")
        self.spinBox_4 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_4.setGeometry(QtCore.QRect(650, 420, 121, 31))
        self.spinBox_4.setStyleSheet("font: 81 10pt \"Outfit ExtraBold\";")
        self.spinBox_4.setMaximum(360)
        self.spinBox_4.setObjectName("spinBox_4")
        self.SignalFrequency_11 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_11.setGeometry(QtCore.QRect(770, 430, 21, 16))
        self.SignalFrequency_11.setStyleSheet("font: 63 11pt \"Montserrat\";")
        self.SignalFrequency_11.setObjectName("SignalFrequency_11")
        self.SignalFrequency_14 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_14.setGeometry(QtCore.QRect(510, 260, 221, 16))
        self.SignalFrequency_14.setStyleSheet("font: 81 11pt \"Outfit ExtraBold\";")
        self.SignalFrequency_14.setObjectName("SignalFrequency_14")
        self.SignalFrequency_15 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_15.setGeometry(QtCore.QRect(690, 260, 221, 16))
        self.SignalFrequency_15.setStyleSheet("font: 81 11pt \"Outfit ExtraBold\";")
        self.SignalFrequency_15.setObjectName("SignalFrequency_15")
        self.SignalFrequency_16 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_16.setGeometry(QtCore.QRect(490, 400, 221, 16))
        self.SignalFrequency_16.setStyleSheet("font: 81 11pt \"Outfit ExtraBold\";")
        self.SignalFrequency_16.setObjectName("SignalFrequency_16")
        self.SignalFrequency_17 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_17.setGeometry(QtCore.QRect(680, 400, 221, 16))
        self.SignalFrequency_17.setStyleSheet("font: 81 11pt \"Outfit ExtraBold\";")
        self.SignalFrequency_17.setObjectName("SignalFrequency_17")
        self.SignalFrequency_9 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_9.setGeometry(QtCore.QRect(20, 630, 401, 41))
        self.SignalFrequency_9.setStyleSheet("font: 81 18pt \"Outfit ExtraBold\";")
        self.SignalFrequency_9.setObjectName("SignalFrequency_9")
        self.SignalFrequency_18 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_18.setGeometry(QtCore.QRect(450, 640, 221, 21))
        self.SignalFrequency_18.setStyleSheet("font: 81 18pt \"Outfit ExtraBold\";")
        self.SignalFrequency_18.setObjectName("SignalFrequency_18")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 740, 321, 51))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("font: 81 15pt \"Outfit ExtraBold\";\n"
                                         "Background-color: #7DF9FF")
        self.pushButton_2.setObjectName("pushButton_2")
        self.spinBox_5 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_5.setGeometry(QtCore.QRect(650, 490, 121, 31))
        self.spinBox_5.setStyleSheet("font: 81 10pt \"Outfit ExtraBold\";")
        self.spinBox_5.setMaximum(360)
        self.spinBox_5.setObjectName("spinBox_5")
        self.SignalFrequency_19 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_19.setGeometry(QtCore.QRect(610, 490, 21, 20))
        self.SignalFrequency_19.setStyleSheet("font: 81 18pt \"Outfit ExtraBold\";")
        self.SignalFrequency_19.setObjectName("SignalFrequency_19")
        self.SignalFrequency_20 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_20.setGeometry(QtCore.QRect(770, 500, 31, 16))
        self.SignalFrequency_20.setStyleSheet("font: 81 13pt \"Outfit ExtraBold\";")
        self.SignalFrequency_20.setObjectName("SignalFrequency_20")
        self.SignalFrequency_21 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_21.setGeometry(QtCore.QRect(490, 470, 221, 16))
        self.SignalFrequency_21.setStyleSheet("font: 81 11pt \"Outfit ExtraBold\";")
        self.SignalFrequency_21.setObjectName("SignalFrequency_21")
        self.SignalFrequency_22 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_22.setGeometry(QtCore.QRect(680, 470, 221, 16))
        self.SignalFrequency_22.setStyleSheet("font: 81 11pt \"Outfit ExtraBold\";")
        self.SignalFrequency_22.setObjectName("SignalFrequency_22")
        self.spinBox_6 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_6.setGeometry(QtCore.QRect(450, 350, 121, 31))
        self.spinBox_6.setStyleSheet("font: 81 10pt \"Outfit ExtraBold\";")
        self.spinBox_6.setMaximum(360)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_7.setGeometry(QtCore.QRect(650, 350, 121, 31))
        self.spinBox_7.setStyleSheet("font: 81 10pt \"Outfit ExtraBold\";")
        self.spinBox_7.setMaximum(360)
        self.spinBox_7.setObjectName("spinBox_7")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(780, 360, 41, 22))
        self.comboBox_4.setStyleSheet("font: 81 10pt \"Outfit ExtraBold\";")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.SignalFrequency_23 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_23.setGeometry(QtCore.QRect(490, 330, 221, 16))
        self.SignalFrequency_23.setStyleSheet("font: 81 11pt \"Outfit ExtraBold\";")
        self.SignalFrequency_23.setObjectName("SignalFrequency_23")
        self.SignalFrequency_24 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_24.setGeometry(QtCore.QRect(690, 330, 221, 16))
        self.SignalFrequency_24.setStyleSheet("font: 81 11pt \"Outfit ExtraBold\";")
        self.SignalFrequency_24.setObjectName("SignalFrequency_24")
        self.SignalFrequency_25 = QtWidgets.QLabel(Dialog)
        self.SignalFrequency_25.setGeometry(QtCore.QRect(600, 350, 21, 20))
        self.SignalFrequency_25.setStyleSheet("font: 81 18pt \"Outfit ExtraBold\";")
        self.SignalFrequency_25.setObjectName("SignalFrequency_25")

        self.pushButton.clicked.connect(self.generate_random_frequencies)
        self.pushButton_2.clicked.connect(self.save_to_csv)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Initialize data storage
        self.data = []

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "DATA"))
        self.label_3.setText(_translate("Dialog", "Enter Signal Details :"))
        self.SignalFrequency.setText(_translate("Dialog", "Signal Frequency :"))
        self.SignalFrequency_2.setText(_translate("Dialog", "Signal Duration :"))
        self.SignalFrequency_3.setText(_translate("Dialog", "Signal Angle of Arrival (AoA) :"))
        self.SignalFrequency_5.setText(_translate("Dialog", "Signal Strength :"))
        self.SignalFrequency_6.setText(_translate("Dialog", "Maximun No. of Signal :"))
        self.SignalFrequency_8.setText(_translate("Dialog", "θ"))
        self.SignalFrequency_10.setText(_translate("Dialog", "dB"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "Hz"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "MHz"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "GHz"))
        self.pushButton.setText(_translate("Dialog", "Generate Random Frequencies"))
        self.SignalFrequency_12.setText(_translate("Dialog", "-"))
        self.SignalFrequency_13.setText(_translate("Dialog", "-"))
        self.SignalFrequency_11.setText(_translate("Dialog", "θ"))
        self.SignalFrequency_14.setText(_translate("Dialog", "MIN"))
        self.SignalFrequency_15.setText(_translate("Dialog", "MAX"))
        self.SignalFrequency_16.setText(_translate("Dialog", "MIN"))
        self.SignalFrequency_17.setText(_translate("Dialog", "MAX"))
        self.SignalFrequency_9.setText(_translate("Dialog", "Taking current system timestamp"))
        self.SignalFrequency_18.setText(_translate("Dialog", "HH:MM:SS"))
        self.pushButton_2.setText(_translate("Dialog", "Open .csv file"))
        self.SignalFrequency_19.setText(_translate("Dialog", "-"))
        self.SignalFrequency_20.setText(_translate("Dialog", "dB"))
        self.SignalFrequency_21.setText(_translate("Dialog", "MIN"))
        self.SignalFrequency_22.setText(_translate("Dialog", "MAX"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "ns"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "ms"))
        self.SignalFrequency_23.setText(_translate("Dialog", "MIN"))
        self.SignalFrequency_24.setText(_translate("Dialog", "MAX"))
        self.SignalFrequency_25.setText(_translate("Dialog", "-"))

    def generate_random_frequencies(self):
        # Function to generate random frequencies based on user input

        # Fetching range inputs
        min_frequency = self.n1.value()
        max_frequency = self.n1_2.value()
        min_duration = self.spinBox_6.value()
        max_duration = self.spinBox_7.value()
        min_angle = 0
        max_angle = self.spinBox_4.value()
        min_strength = self.spinBox_3.value()
        max_strength = self.spinBox_5.value()
        max_signals = self.nmax.value()
        
        # Fetching units
        freq_unit = self.comboBox_3.currentText()
        duration_unit = self.comboBox_4.currentText()
        
        if max_frequency < min_frequency:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'Maximum frequency cannot be smaller than minimum frequency.')
            return
        if max_duration < min_duration:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'Maximum duration cannot be smaller than minimum duration.')
            return
        if max_angle < min_angle:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'Maximum angle cannot be smaller than minimum angle.')
            return
        if max_strength < min_strength:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'Maximum strengthS cannot be smaller than minimum strength.')
            return
        if max_signals <= 0:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'Maximum number of signals must be greater than zero.')
            return

        # Generating random data
        self.data = []
        
        for _ in range(max_signals):
            frequency = random.uniform(min_frequency, max_frequency)
            duration = random.uniform(min_duration, max_duration)
            angle = random.uniform(min_angle, max_angle)
            strength = random.uniform(min_strength, max_strength)
            current_time = datetime.now().strftime('%H:%M:%S.%f')[:-3]
            self.data.append((frequency, duration, angle, strength, current_time))

        # Display timestamp (example: update a QLabel)
        self.SignalFrequency_18.setText(f"Current timestamp: {current_time}")  
        QtWidgets.QMessageBox.information(None, 'Information', 'Random data generated successfully.')

        # Updating the UI or saving data as needed

        

    def save_to_csv(self):
    # Function to save generated data to a CSV file

    # Fetching data to save (using self.data)
        data_to_save = self.data
        
        if not data_to_save:
            QtWidgets.QMessageBox.warning(None, 'Warning', 'No data to save. Generate data first.')
            return
        
        freq_unit = self.comboBox_3.currentText()
        duration_unit = self.comboBox_4.currentText()

        # Saving data to CSV file
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File', '', 'CSV Files (*.csv)')
        if filename:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([f'Frequency ({freq_unit})', f'Duration ({duration_unit})', 'Angle', 'Strength', 'current_time'])
                writer.writerows(data_to_save)

            # Displaying a message or updating the UI after saving
            QtWidgets.QMessageBox.information(None, 'Information', 'CSV file saved successfully.')



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
