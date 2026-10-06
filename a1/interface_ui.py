from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        
        # Label - Sensor de temperatura
        self.Sensor = QLabel(Form)
        self.Sensor.setObjectName(u"Sensor")
        self.Sensor.setGeometry(110, 30, 151, 16)
        self.Sensor.setText(u"Sensor de temperatura")
        
        # Progress Bar
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(120, 60, 118, 23)
        self.progressBar.setValue(24)

        # Set window title
        Form.setWindowTitle(u"Form")

        QMetaObject.connectSlotsByName(Form)
    # setupUi


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
