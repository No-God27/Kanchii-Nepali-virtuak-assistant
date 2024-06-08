# kanchhi3.py

import speech_recognition as sr
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from main_VA import main

class Ui_HomePage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_HomePage, self).__init__(parent)
        self.setupUi(self)
        self.listen_lock = threading.Lock()

    def setupUi(self, widget):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.is_listening = False

        self.BackGround = QtWidgets.QLabel(widget)
        self.BackGround.setEnabled(True)
        self.BackGround.setGeometry(QtCore.QRect(-40, -40, 2400, 1440))
        self.BackGround.setText("")
        self.BackGround.setPixmap(QtGui.QPixmap("images/Green Bgk.png"))
        self.BackGround.setScaledContents(True)
        self.BackGround.setObjectName("BackGround")

        self.Background2 = QtWidgets.QLabel(widget)
        self.Background2.setGeometry(QtCore.QRect(-170, 340, 2400, 1440))
        self.Background2.setText("")
        self.Background2.setPixmap(QtGui.QPixmap("images/Sky Blue.png"))
        self.Background2.setScaledContents(True)
        self.Background2.setObjectName("Background2")

        self.Background3 = QtWidgets.QLabel(widget)
        self.Background3.setGeometry(QtCore.QRect(-30, 600, 2400, 1440))
        self.Background3.setText("")
        self.Background3.setPixmap(QtGui.QPixmap("images/White.png"))
        self.Background3.setScaledContents(True)
        self.Background3.setObjectName("Background3")

        self.Kanchikt = QtWidgets.QLabel(widget)
        self.Kanchikt.setGeometry(QtCore.QRect(550, 30, 300, 420))
        self.Kanchikt.setText("")
        self.Kanchikt.setPixmap(QtGui.QPixmap("images/Newari kt.png"))
        self.Kanchikt.setScaledContents(True)
        self.Kanchikt.setObjectName("Kanchikt")

        self.Kanchitext = QtWidgets.QLabel(widget)
        self.Kanchitext.setGeometry(QtCore.QRect(880, 45, 450, 250))
        self.Kanchitext.setText("")
        self.Kanchitext.setPixmap(QtGui.QPixmap("images/Kanchi.png"))
        self.Kanchitext.setScaledContents(True)
        self.Kanchitext.setObjectName("Kanchitext")

        self.SwagatamLabel = QtWidgets.QLabel(widget)
        self.SwagatamLabel.setGeometry(QtCore.QRect(800, 330, 400, 80))
        font = QtGui.QFont()
        font.setFamily("Preeti")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.SwagatamLabel.setFont(font)
        self.SwagatamLabel.setObjectName("SwagatamLabel")

        self.BolnaSuruButton = QtWidgets.QPushButton(widget)
        self.BolnaSuruButton.setEnabled(True)
        self.BolnaSuruButton.setGeometry(QtCore.QRect(150, 450, 240, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.BolnaSuruButton.setFont(font)
        self.BolnaSuruButton.setAutoFillBackground(False)
        self.BolnaSuruButton.setStyleSheet("color: white; background-color:#228B22; border-style:outset;border-radius:15px;")
        self.BolnaSuruButton.setObjectName("BolnaSuruButton")

        self.BolnaBandaButton = QtWidgets.QPushButton(widget)
        self.BolnaBandaButton.setGeometry(QtCore.QRect(450, 450, 240, 80))
        font = QtGui.QFont()
        font.setFamily("Preeti")
        font.setPointSize(16)
        self.BolnaBandaButton.setFont(font)
        self.BolnaBandaButton.setAutoFillBackground(False)
        self.BolnaBandaButton.setStyleSheet("color: white; background-color:#d32f2f; border-style:outset;border-radius:15px;")
        self.BolnaBandaButton.setObjectName("BolnaBandaButton")

        self.SuruGarnaLabel = QtWidgets.QLabel(widget)
        self.SuruGarnaLabel.setGeometry(QtCore.QRect(250, 500, 370, 150))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.SuruGarnaLabel.setFont(font)
        self.SuruGarnaLabel.setObjectName("SuruGarnaLabel")

        self.SunekaKuraharuLabel = QtWidgets.QLabel(widget)
        self.SunekaKuraharuLabel.setGeometry(QtCore.QRect(100, 630, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SunekaKuraharuLabel.setFont(font)
        self.SunekaKuraharuLabel.setObjectName("SunekaKuraharuLabel")

        self.OutputTextboxLabel = QtWidgets.QLabel(widget)
        self.OutputTextboxLabel.setGeometry(QtCore.QRect(190, 700, 770, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.OutputTextboxLabel.setFont(font)
        self.OutputTextboxLabel.setText("")
        self.OutputTextboxLabel.setObjectName("OutputTextboxLabel")

        self.ResponseTextboxLabel = QtWidgets.QLabel(widget)
        self.ResponseTextboxLabel.setGeometry(QtCore.QRect(190, 770, 100, 150))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PratikriyaKuraharuLabel = QtWidgets.QLabel(widget)
        self.PratikriyaKuraharuLabel.setGeometry(QtCore.QRect(100, 730, 160, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PratikriyaKuraharuLabel.setFont(font)
        self.PratikriyaKuraharuLabel.setObjectName("PratikriyaKuraharuLabel")
        self.ResponseTextboxLabel.setFont(font)
        self.ResponseTextboxLabel.setText("")
        self.ResponseTextboxLabel.setObjectName("ResponseTextboxLabel")

        self.BolnaSuruButton.clicked.connect(self.start_listening)
        self.BolnaBandaButton.clicked.connect(self.stop_listening)

        self.retranslateUi(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        self.SwagatamLabel.setText(_translate("MainWindow", "तपाइलाई स्वागत छ ।"))
        self.BolnaSuruButton.setStatusTip(_translate("MainWindow", "बोल्न सुरु has been pressed"))
        self.BolnaSuruButton.setText(_translate("MainWindow", "बोल्न सुरु"))
        self.BolnaBandaButton.setStatusTip(_translate("MainWindow", "बोल्न बन्द has been pressed"))
        self.BolnaBandaButton.setText(_translate("MainWindow", "बोल्न बन्द"))
        self.SuruGarnaLabel.setText(_translate("MainWindow", "सुरु गर्नाको लागी \" बोल्न सुरु \" थिच्नुहोस् ।"))
        self.SunekaKuraharuLabel.setText(_translate("MainWindow", "सुनेको कुराहरु:"))
        self.PratikriyaKuraharuLabel.setText(_translate("MainWindow", "प्रतिक्रिया:"))

    def start_listening(self):
        if not self.is_listening:
            self.is_listening = True
            self.listening_thread = threading.Thread(target=self.listen)
            self.listening_thread.start()

    def stop_listening(self):
        if self.is_listening:
            self.is_listening = False

    def listen(self):
        with self.listen_lock:  # Ensure only one thread can access the microphone at a time
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                while self.is_listening:
                    try:
                        audio = self.recognizer.listen(source, timeout=5)
                        text = self.recognizer.recognize_google(audio, language='ne-NP')
                        self.update_output_textbox(text)
                        final_result = main(text)
                        print(final_result)
                        self.update_response_textbox(final_result)
                    except sr.UnknownValueError:
                        self.update_response_textbox("Could not understand audio")
                    except sr.RequestError as e:
                        self.update_response_textbox(f"Could not request results; {e}")
                    except sr.WaitTimeoutError:
                        continue

    def update_output_textbox(self, text):
        self.OutputTextboxLabel.setText(text)
        self.OutputTextboxLabel.adjustSize()

    def update_response_textbox(self, text):
        self.ResponseTextboxLabel.setText(text)
        self.ResponseTextboxLabel.adjustSize()

def setup_home_page(widget):
    ui = Ui_HomePage()
    ui.setupUi(widget)
