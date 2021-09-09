from PyQt5 import QtCore
from PyQt5.QtCore import QDir, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QPushButton, QWidget

class CommandWidget(QWidget):
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
		self.addImageBtn.clicked.connect(self.openJson)
		# new json
		self.addNewJsonBtn = QPushButton("create new json")
		self.addNewJsonBtn.clicked.connect(self.createJson)

		#signals
		self.setImage = pyqtSignal(str,QPixmap)
		self.setJson = pyqtSignal(str)#json_obj)
		self.newJson = pyqtSignal()

		#add to layout
		layout.addWidget(self.addImageBtn)
		layout.addWidget(self.addJsonBtn)
		layout.addWidget(self.addNewJsonBtn)

	def openImage(self, filename=None):
		if not filename:
			filename, _ = QFileDialog.getOpenFileName(self, 'Select Photo', QDir.currentPath(), 'Images (*.png *.jpg)')
		if not filename:
			return
		
		image = QPixmap(filename)
		self.setImage.emit(filename,image)

	def openJson(self,filename=None):
		if not filename:
			filename, _ = QFileDialog.getOpenFileName(self, 'Select json', QDir.currentPath(), 'Json (*.json)')
		if not filename:
			return
		
		# parse json here
		
		self.setJson.emit(filename)
	
	def createJson(self,event):
		# create new json object
		self.newJson.emit()