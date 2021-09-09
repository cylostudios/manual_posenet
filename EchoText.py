from PyQt5.QtWidgets import  QWidget, QGridLayout, QLineEdit, QLabel

class EchoText(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
  
        self.textbox = QLineEdit()
        self.echo_label = QLabel('')
  
        self.textbox.textChanged.connect(self.textbox_text_changed)
  
        layout.addWidget(self.textbox, 0, 0)
        layout.addWidget(self.echo_label, 1, 0)
  
    def textbox_text_changed(self):
        self.echo_label.setText(self.textbox.text())