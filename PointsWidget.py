from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPointF, QRectF, pyqtSignal
from PyQt5.QtWidgets import  QWidget, QGridLayout
import Posenet

class PointsWidget(QWidget):

	# jsonSet = pyqtSignal(str,Posenet.Pose)
	# imageSet = pyqtSignal(str,QtGui.QPixmap)

	def __init__(self,width = 900,height = 800):
		super().__init__()
		self._width = width
		self._height = height

		self.circleSize = 25

		self.setFixedWidth(width)
		self.setFixedHeight(height)

		layout = QGridLayout()
		self.setLayout(layout)
		self.pose = None
		self.image = None

	def setPose(self,url,pose: Posenet.Pose):
		self.pose = pose
		self.poseUrl = url
		self.update()

	def setImage(self,url,image: QtGui.QImage):
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

		if(self.pose is None or self.image is None):
			return

		painter.setBrush(QtGui.QColor(0,0,0,255))
		painter.drawRect(QtCore.QRect(0,0,self._width,self._height))

		# painter = QtGui.QPainter(self)
		# pen = QtGui.QPen(QtGui.QColor(0,0,0,255))
		# pen.setWidth(5)
		# painter.setPen(pen)

		painter.setBrush(QtGui.QColor(255,255,255,255))
		painter.drawRect(QtCore.QRect(0,0,self._width,self._height))


		painter.setBrush(QtGui.QColor(0,0,0,255))

		painter.drawImage(0,0,self.image)

		for pidx in range(17):
			if pidx < 5:
				continue	

			pose = self.pose.getPose(pidx)
			point = QRectF( 
				pose[0] * self.image.width(),
				pose[1] * self.image.height(),
				self.circleSize,
				self.circleSize
			)
			painter.setBrush(QtGui.QColor(255,0,0,255))
			painter.drawEllipse(point)
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
		self.pose = None
		self.poseUrl = "" 
		self.image = None
		self.imageUrl = "" 
		print("reset")
		self.update()

