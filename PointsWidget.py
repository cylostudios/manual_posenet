from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QRectF, pyqtSignal
from PyQt5.QtWidgets import  QWidget, QGridLayout
import Posenet

class PointsWidget(QWidget):

	# jsonSet = pyqtSignal(str,Posenet.Pose)
	# imageSet = pyqtSignal(str,QtGui.QPixmap)

	def __init__(self,width = 900,height = 800):
		super().__init__()
		self._width = width
		self._height = height

		self.circleSize = 5

		self.setFixedWidth(width)
		self.setFixedHeight(height)

		layout = QGridLayout()
		self.setLayout(layout)
		self.pose = None
		self.image = None

	def setPose(self,url,pose: Posenet.Pose):
		self.pose = pose
		self.pose = url
		self.update()

	def setImage(self,url,image: QtGui.QImage):
		print("IMGGGGGG")
		self.image = image
		self.imageUrl = url
		if(self.image.height() > self.image.width()):
			# set to vertical size
			# self.image.
			pass

		if(self.image.height() > self.image.width()):
			# set to vertical size
			pass

		if(self.image.height() == self.image.width()):
			# set to scaled square
			pass

		self.update()

	def setPoints(self,points):
		self.points = points

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		painter.setBrush(QtGui.QColor(255,255,255,255))
		painter.drawRect(QtCore.QRect(0,0,self._width,self._height))

		print(self.pose,self.image)
		if(self.pose is None or self.image is None):
			print("NOIMGORJSON")
			print(self.pose,self.image)
			return

		painter.setBrush(QtGui.QColor(0,0,0,255))
		painter.drawRect(QtCore.QRect(0,0,self._width,self._height))

		# painter = QtGui.QPainter(self)
		pen = QtGui.QPen(QtGui.QColor(0,0,0,255))
		pen.setWidth(5)
		painter.setPen(pen)

		painter.setBrush(QtGui.QColor(255,255,255,255))
		painter.drawRect(QtCore.QRect(0,0,self._width,self._height))

		qrect = QtCore.QRectF(0.5 * self._width , 0.5 * self._height ,self.circleSize,self.circleSize)

		painter.setBrush(QtGui.QColor(0,0,0,255))

		painter.drawEllipse( qrect )

		painter.drawImage(0,0,self.image)
		# i = QtGui.QPixmap()
		# i.fromImage(self.image)
		# painter.drawPixmap(QRectF(0,0,self.width,self.height),self.image)

	def mousePressEvent(self, event):
		pass
		# if self.rect.contains(event.pos()):
		# 	self.drag_position = event.pos() - self.rect.topLeft()
		# 	super().mousePressEvent(event)

	def mouseMoveEvent(self, event):
		pass
		# if not self.drag_position.isNull():
		# 	self.rect.moveTopLeft(event.pos() - self.drag_position)
		# 	self.update()
		# 	super().mouseMoveEvent(event)

	def mouseReleaseEvent(self, event):
		pass
		# self.drag_position = QtCore.QPoint()
		# super().mouseReleaseEvent(event)

	def save(self):
		print("SAVE")
		self.pose.save()

	def reset(self):
		print("reset")
