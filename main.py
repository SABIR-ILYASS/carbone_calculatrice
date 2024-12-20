from PySide2.QtGui import QFont, QIcon
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout
from PySide2.QtCore import Qt
import sys
import os

# Répertoire local
PATH = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')

class CarboneCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # Paramètres de la fenêtre
        self.setWindowTitle("carbone calculator")
        self.setFixedSize(600, 400)
        # On peut ajouter une icône si on le souhaite, en décommentant si une image existe
        # self.setWindowIcon(QIcon(PATH + "/Images/icon.png")) 

        # Widget central
        self.centralWidget = QWidget(self)
        self.centralWidget.setFixedSize(600, 400)
        self.centralWidget.setStyleSheet("background-color: #212129;")
        self.setCentralWidget(self.centralWidget)

        # Titre
        self.titleLabel = QLabel("carbone calculator", self.centralWidget)
        font = QFont()
        font.setPointSize(30)
        font.setFamily("Gabriola")
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setStyleSheet("color: #12A2D7;")

        # Zone de saisie de texte
        self.text_input = QLineEdit(self.centralWidget)
        self.text_input.setStyleSheet(
            "QLineEdit {"
            "   background-color: #282B2E;"
            "   border-style: solid;"
            "   border-width: 1px;"
            "   border-color: #12A2D7;"
            "   border-radius: 5px;"
            "   color: #FFFFFF;"
            "   font-size: 20px;"
            "   font-family: Gabriola;"
            "   padding: 5px;"
            "}"
            "QLineEdit:hover {"
            "   border-color: #3E5EAB;"
            "}"
        )

        # Zone d'affichage d'un chiffre
        self.number_display = QLabel("0", self.centralWidget)
        display_font = QFont()
        display_font.setPointSize(50)
        display_font.setFamily("Gabriola")
        display_font.setBold(True)
        self.number_display.setFont(display_font)
        self.number_display.setAlignment(Qt.AlignCenter)
        self.number_display.setStyleSheet("color: #12A2D7;")

        # Mise en page verticale
        layout = QVBoxLayout()
        layout.addWidget(self.titleLabel)
        layout.addStretch(1)
        layout.addWidget(self.text_input)
        layout.addStretch(1)
        layout.addWidget(self.number_display)
        layout.addStretch(1)

        self.centralWidget.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CarboneCalculator()
    window.show()
    sys.exit(app.exec_())
