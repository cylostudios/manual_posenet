from typing import List
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QEvent, QPointF, QRect, QRectF, pyqtSignal, Qt
from PyQt5.QtWidgets import  QGraphicsEllipseItem, QGraphicsScene, QGraphicsTextItem, QGraphicsView, QLabel, QWidget, QGridLayout
import Posenet

class PointsWidget(QGraphicsView):

	def __init__(self,width = 900,height = 800):
		super().__init__()
		self._width = width
		self._height = height

		# self.setStyleSheet("background-color: red;")


		self.setFixedWidth(width)
		self.setFixedHeight(height)

		self._scene = QGraphicsScene()
		self.setScene(self._scene)

		self.scene()
		self.points = []

		self.pose = None
		self.image = None

		#used for dragging
		self.currentItem = None

		# cycle functionality setup
		self.togglePoints = False
		self.currentTogglePoint = None


		self.drawScene()


	def setPose(self,url,pose: Posenet.Pose):
		self.pose = pose
		self.poseUrl = url
		self.points: List[Posenet.PosePoint] = []
		
		w = self.image.width() if self.image else 800
		h = self.image.height() if self.image else 800 

		for idx in range(len(self.pose.pose)):
			_point = self.pose.getPose(idx)
			point = Posenet.PosePoint(
				idx,
				_point[0],
				_point[1],
				w,
				h,
				self.pose.getPoseLabel(idx)
			)

			self.points.append(point)

		self.pose.setPoints(self.points)
		self.update()
		self.drawScene()

	def setImage(self,url,image: QtGui.QImage):
		self.image = image
		self.imageUrl = url

		# self.setFixedWidth(self.image.width())
		# self.setFixedHeight(self.image.height())

		if(self.image.height() > self.image.width()):
			# set to vertical size
			self.image = self.image.scaled(self.width(),self.height(),Qt.KeepAspectRatio)
			# self.image = self		# layout = QGridLayout()
		# self.setLayout(layout).image.scaled(self.width(),self.height())
			pass

		if(self.image.height() < self.image.width()):
			# set to horizontal size
			# self.image = self.image.scaled(100,100)
			self.image = self.image.scaled(self.width(),self.height(),Qt.KeepAspectRatio)
			# self.image = self.image.scaled(self.width(),self.height())
			pass

		if(self.image.height() == self.image.width()):
			# set to scaled square
			# self.image = self.image.scaled(100,100)
			self.image = self.image.scaled(self.width(),self.height(),Qt.KeepAspectRatio)
			# self.image = self.image.scaled(self.width(),self.height())
			pass

		self.update()

		if self.points is not None:
			for p in self.points: p.setImageDims(self.image.width(),self.image.height())

		self.drawScene()

	def setPoints(self,points):
		# self.points = points
		pass


	def drawScene(self):
		if(self.pose is None or self.image is None):
			self.setStyleSheet("background-color: white;")
			return

		# self.setStyleSheet("background-color: white;")
		img = QtGui.QPixmap().fromImage(self.image)
		print(img.rect())
		self.scene().addPixmap(img)

		self.scene().addEllipse(QRectF(0,0,25,25),QtGui.QColor(0,0,255,255))

		# self.scene().setForegroundBrush(QtGui.QColor(255, 0, 0, 255))

		for p in range(len(self.points)):
			if p > 4:
				print(self.pose.getPoseLabel(p) ,self.points[p].elipse)
				self.scene().addEllipse(self.points[p].elipse, QtGui.QColor(255,0,0,255))
				self.scene().addItem(self.points[p].text)


	def mousePressEvent(self, event: QtGui.QMouseEvent):
		pos = event.pos()
		i = 0
		print(pos)
		for p in self.points:
			i+=1
			if p.elipse.contains(pos):
				print("COMNE")
				self.currentItem = p
				break

	def mouseMoveEvent(self, event: QtGui.QMouseEvent):
		if( self.currentItem is not None):
			ep = event.pos()
			self.currentItem.move(ep)	
			# self.drawScene()

	def mouseReleaseEvent(self, event):
		self.currentItem = None

	def save(self):
		self.pose.save()

	def reset(self):
		self.pose = None
		self.poseUrl = "" 
		self.image = None
		self.imageUrl = "" 
		print("reset")
		self.update()
		self.scene().clear()
		self.drawScene()

	def getNextPoint(self):
		print("getting next point")
		if self.currentTogglePoint is None:
			# idx 5 is the left shoulder
			self.currentTogglePoint = (5,self.points[5])
			self.currentTogglePoint[1].focus()
			self.update()
			return

		lastPoint = self.currentTogglePoint
		lastPoint[1].removeFocus()
		newIdx = (lastPoint[0] + 1) % len(self.points)

		# only activate body points
		if newIdx <= 4:
			newIdx = 5

		self.currentTogglePoint = ( 
			newIdx,
			self.points[newIdx]
		)
		self.currentTogglePoint[1].focus()
		self.update()
		

	def moveCurrentPoint(self):
		if self.currentTogglePoint is not None:
			print("moving point")
			self.currentTogglePoint[1].move(QPointF(0,0))
			self.update()

	def keyPressEvent(self,event):
		t = 84
		o = 79 
		n = 78
		if event.key() == t:
			# enable / disable individual selection 
			self.togglePoints = not self.togglePoints
			print("toggle = " , self.togglePoints)
			return

		if event.key() == o:
			# move current selection to 0,0 
			self.moveCurrentPoint()
			return

		if event.key() == n:
			# cycle through points 
			self.getNextPoint()
			return