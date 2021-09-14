import json
from datetime import datetime
from typing import Tuple
from PyQt5.QtCore import QPointF, QRectF
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsTextItem

pose_defs = [
	"nose",
	"leftEye",
	"rightEye",
	"leftEar",
	"rightEar",
	"leftShoulder",
	"rightShoulder",
	"leftElbow",
	"rightElbow",
	"leftWrist",
	"rightWrist",
	"lefthip",
	"rightHip",
	"leftKnee",
	"rightKnee",
	"leftAnkle",
	"rightAnkle",
]

class PosePoint():
	def __init__(self, idx, x=0.0, y=0.0, w=0.0, h=0.0, text=""):
		self.focusedPoint = None
		self.TEXT_OFFSET_X = 0//-15
		self.TEXT_OFFSET_Y = 0

		self.idx = idx
		self.s = 25

		self.raw_x = x
		self.raw_y = y
		self.w = w
		self.h = h

		self.elipse = QRectF(
			x * w,
			y * h,
			self.s,
			self.s
		)

		self.text = QGraphicsTextItem()
		self.text.setPlainText(text)

		self.text.setPos(
			self.elipse.x() + self.TEXT_OFFSET_X,
			self.elipse.y() + self.TEXT_OFFSET_Y
		)

		self.updatePoint = None
		self.text.setDefaultTextColor(QColor(255, 0, 0, 255))
		pass

	def clearFocus(self):
		self.focus = 0
	
	def move(self, point):
		# print("moving text from %f, %f to %f, %f" % (
		# 	self.text.x(),
		# 	self.text.y(),
		# 	point.x(),
		# 	point.y()
		# ) )
		self.text.setPos(point)
		# trigger redraw!
		# print("moving elipse from %f, %f to %f, %f" % (
		# 	self.elipse.x(),
		# 	self.elipse.y(),
		# 	point.x(),
		# 	point.y()
		# ) )
		self.elipse.moveTo(point)
		if self.updatePoint is not None:
			self.updatePoint(self.idx,point.x() / self.w, point.y() / self.h)

	def registerUpdatePoint(self,up):
		self.updatePoint = up

	def setColor(self,color):
		self.text.setDefaultTextColor(color)
		# self.elipse

	def setImageDims(self, w, h):
		self.w = w
		self.h = h

		self.elipse.moveTo(
			self.raw_x * w,
			self.raw_y * h
		)

		self.text.setPos(
			self.raw_x * w + self.TEXT_OFFSET_X,
			self.raw_y * h + self.TEXT_OFFSET_Y
		)

class Pose():
	focusedPoint: PosePoint 
	def __init__(self, url: str, j: dict) -> None:
		self.url = url
		self.json = j
		self.poses = j["poses"]
		self.pose = self.poses[0]

	def getPose(self, idx):
		return self.pose[idx]

	def getPoseLabel(self, idx):
		if(idx > len(pose_defs)-1):
			return "UNDEFINED"

		return pose_defs[idx]

	def focusPoint(self,idx):
		if idx == 0 or self.focusedPoint is None:
			return

		self.focusedPoint = self.getPose(idx)

	def clearFocusedPoint(self):
		self.focusedPoint.setColor(QColor(255,0,0,255))

		self.focusedPoint = None
	
	def getUrl(self):
		return self.url

	def setPoints(self,points):
		self.points = points
		for p in self.points:
			p.registerUpdatePoint(self.updatePoint)

	def updatePoint(self, idx: int, x: float, y: float):
		if x == None or y == None:
			return

		self.pose[idx][0] = x
		self.pose[idx][1] = y

	def setPoint(self,idx,point):
		self.pose[idx][0] = point.x()
		self.pose[idx][1] = point.y()
		pass

	def save(self):
		now = datetime.now()
		timestamp = now.strftime("%H_%M_%S")
		url = "pose_%s.json" % timestamp

		j = open(url, "w")
		json.dump(self.json, j)
		print("wrote file %s" % url)


def loadJson(url=""):
	if url == "":
		print("No url provided")
		return None

	try:
		f = open(url, "r")
		j = json.load(f)
		p = Pose(url, j)
		return p
	except Exception as e:
		print("Exception occured", e)
		return None


def createJson():
	# pose = loadJson("./template.json")
	pose = loadJson("./yorke.json")

	return pose

