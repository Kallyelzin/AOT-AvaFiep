import sys
from PySide6.QtCore import Qt
from Pyside6.QtWidges import QApplication, QMainWindow, Qlabel

class JanelaPrincipal(MainWindow):
    def _init_(Self):
        super()._init_()
        self.setwindowTitle("Minha Primeira Janela")
        self.resize(400, 250)
                    
        rotulo = Qlabel("Olá, Pyside6!", parent-self)
        self.setCentralWidge(rotulo)
        rotulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

if _name_ == "_main_":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec())