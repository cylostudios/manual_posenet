import json
from datetime import datetime
from typing import Tuple

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


class Pose():
	def __init__(self, url: str, j: dict) -> None:
		self.url = url
		self.json = j 
		self.poses = j["poses"]
		self.pose = self.poses[0]

	def getPose(self, idx):
		return self.pose[idx]

	def getPoseLabel(self,idx):
		if(idx > len(pose_defs)-1):
			return "UNDEFINED"

		return pose_defs[idx]

	def getUrl(self):
		return self.url

	def updatePoint(self, idx: int, x: float, y: float):
		if x == None or y == None:
			return

		self.pose[idx][0] = x
		self.pose[idx][1] = y

	def save(self):
		now = datetime.now()
		timestamp = now.strftime("%H_%M_%S")
		url = "pose_%s.json" % timestamp

		j = open(url,"w")	
		json.dump(self.json,j)
		print("wrote file %s"%url)

def loadJson(url=""):
	if url == "":
		print("No url provided")
		return None

	try:
		f = open(url,"r")
		j = json.load(f)
		p = Pose(url,j)
		return p
	except Exception as e:
		print("Exception occured",e)
		return None

def createJson():
	pose = loadJson("./template.json")

	return pose
