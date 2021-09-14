from PyQt5.QtCore import QDir, pyqtSignal
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QLabel, QPushButton, QWidget
import Posenet

class CommandWidget(QWidget):
	setImage = pyqtSignal(str,QImage)
	setJson = pyqtSignal(str,Posenet.Pose)
	newJson = pyqtSignal(str,Posenet.Pose)
	saveSignal = pyqtSignal()
	resetSignal = pyqtSignal()

	def __init__(self) -> None:
		super().__init__()
		layout = QHBoxLayout()
		self.setLayout(layout)

		#buttons
		# add image
		self.addImageBtn = QPushButton("add image")
		self.addImageBtn.clicked.connect(self.openImage)
		# add json
		self.addJsonBtn = QPushButton("add json")
		self.addJsonBtn.clicked.connect(self.openJson)
		# new json
		self.addNewJsonBtn = QPushButton("create new json")
		self.addNewJsonBtn.clicked.connect(self.createJson)
		# save
		self.saveBtn = QPushButton("save")
		self.saveBtn.clicked.connect(self.save)
		# reset
		self.resetBtn = QPushButton("reset")
		self.resetBtn.clicked.connect(self.reset)

		#labels
		self.jsonAdded = QPushButton("json added")
		self.imgAdded = QPushButton("image added")
		self.jsonAdded.setDisabled(True)
		self.imgAdded.setDisabled(True)

		#add to layout
		layout.addWidget(self.addImageBtn)
		layout.addWidget(self.imgAdded)
		self.imgAdded.hide()
		layout.addWidget(self.addJsonBtn)
		layout.addWidget(self.addNewJsonBtn)
		layout.addWidget(self.jsonAdded)
		self.jsonAdded.hide()
		layout.addWidget(self.saveBtn)
		self.saveBtn.hide()
		layout.addWidget(self.resetBtn)
		self.resetBtn.hide()

		self.show()

	def openImage(self, filename=None):
		# if not filename:
		# 	filename, _ = QFileDialog.getOpenFileName(self, 'Select Photo', QDir.currentPath(), 'Images (*.png *.jpg)')
		# if not filename:
		# 	return
		
		filename = "./yorke.jpg"

		# image = QPixmap(filename)
		image = QImage()
		f = filename
		image.load(f)

		# hide button
		self.addImageBtn.hide()
		self.imgAdded.show()

		self.setImage.emit(filename,image)
		self.enableSR()

	def openJson(self,filename=None):
		if not filename:
			filename, _ = QFileDialog.getOpenFileName(self, 'Select json', QDir.currentPath(), 'Json (*.json)')
		if not filename:
			return
		
		# parse json here
		pose = Posenet.loadJson(filename)
		if pose is None:
			print("ERROR CREATING POSE")
			return 

		# hide button
		self.addNewJsonBtn.hide()
		self.addJsonBtn.hide()
		self.jsonAdded.show()

		self.setJson.emit(filename, pose)
		self.enableSR()
	
	def createJson(self,event):
		# create new json object
		pose = Posenet.createJson()

		if pose is None:
			return

		# hide button
		self.addNewJsonBtn.hide()
		self.addJsonBtn.hide()
		self.jsonAdded.show()

		self.newJson.emit(pose.url,pose)
		self.enableSR()
	
	def save(self):
		self.saveSignal.emit()

	def reset(self):
		self.resetSignal.emit()
		self.resetBtn.hide()
		self.saveBtn.hide()
		self.addNewJsonBtn.show()
		self.addImageBtn.show()
		self.addJsonBtn.show()

	def enableSR(self):
		if( self.addImageBtn.isHidden() and ( self.addJsonBtn.isHidden() or self.addNewJsonBtn.isHidden())):
			self.resetBtn.show()
			self.saveBtn.show()
			self.imgAdded.hide()
			self.jsonAdded.hide()