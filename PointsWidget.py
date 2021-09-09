from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import  QWidget, QGridLayout, QLineEdit, QLabel

class PointsWidget(QWidget):
	def __init__(self,points):
		super().__init__()
		layout = QGridLayout()
		self.setLayout(layout)

		# self.points = [QtCore.QRect(300 ,300,70,70) for i in range(17)]
		self.points = points

	def paintEvent(self, event):
		return
		# self.painter = QtGui.QPainter(self)
		# pen = QtGui.QPen(QtGui.QColor(0,0,0,255))
		# pen.setWidth(5)
		# self.painter.setPen(pen)

		# self.painter.setBrush(QtGui.QColor(0,0,0,255))
		# c = self.points[0]
		# self.painter.drawEllipse( c )

	def mousePressEvent(self, event):
		print("mouse")
		# if self.rect.contains(event.pos()):
		# 	self.drag_position = event.pos() - self.rect.topLeft()
		# 	super().mousePressEvent(event)

	def mouseMoveEvent(self, event):
		if not self.drag_position.isNull():
			self.rect.moveTopLeft(event.pos() - self.drag_position)
			self.update()
			super().mouseMoveEvent(event)

	def mouseReleaseEvent(self, event):
		self.drag_position = QtCore.QPoint()
		super().mouseReleaseEvent(event)
