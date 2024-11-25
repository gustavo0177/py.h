import sys

from PyQt6.QtWidgets import QApplication, QPushButton, QMessageBox, QMainWindow


class MainWindow(QMainWindow):
 
 def __init__(self):

    super().__init__()

    self.setWindowTitle("Botão com Mensagem")

    self.setGeometry(100, 100, 280, 80)
  
    button = QPushButton('Clique aqui', self)

    button.clicked.connect(self.show_message)

    button.resize(100, 30)

    button.move(90, 20)

    def show_message(self):

       QMessageBox.information(self, "Mensagem", "Você clicou no botão!")


def main():
 
app = QApplication(sys.argv)

window = MainWindow()

window.show()
sys.exit(app.exec())


if __name__ == "__main__":

 main()
