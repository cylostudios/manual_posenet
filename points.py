from PyQt5 import QtGui
from PyQt5.QtWidgets import  QWidget, QGridLayout, QLineEdit, QLabel

class Points(QWidget):
	def __init__(self):
		super().__init__()
		layout = QGridLayout()
		self.setLayout(layout)

		self.points = [{} for i in range(17)]

	def paintEvent(self, event):
		self.painter = QtGui.QPainter(self)
		pen = QtGui.QPen(QtGui.QColor(0,0,0,255))
		pen.setWidth(5)
		self.painter.setPen(pen)

		self.painter.setBrush(QtGui.QColor(0,0,0,255))
		self.painter.drawEllipse(300, 300, 70, 70)

		path = QtGui.QPainterPath
