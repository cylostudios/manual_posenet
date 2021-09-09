from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap 
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget
import sys
from PointsWidget import PointsWidget
from CommandsWidget import CommandWidget


class MainWidget(QMainWindow):
	def __init__(self):

		super().__init__()

		self.setWindowTitle("Drag and Drop")
		self.resize(720, 480)
		self.setAcceptDrops(True)

		self.central_widget = QWidget()               
		self.setCentralWidget(self.central_widget)    
		self.central_widget.showFullScreen()

		lay = QVBoxLayout(self.central_widget)

		self.label = QLabel(self)
		self.pointsWidget = PointsWidget([])
		self.commandWidget = CommandWidget()

		self.commandWidget.setImage.connect(self.setImage)
		self.commandWidget.setJson.connect(self.setJson)
		self.commandWidget.newJson.connect(self.setNewJson)

		lay.addWidget(self.commandWidget)
		lay.addWidget(self.pointsWidget)

		lay.setAlignment(self.commandWidget,Qt.AlignTop)

	def dragEnterEvent(self, event):
		if event.mimeData().hasUrls():
			event.accept()
		else:
			event.ignore()


	def dropEvent(self, event):
		files = [u.toLocalFile() for u in event.mimeData().urls()]
		for f in files:
			print(f)
			img = QPixmap(f)
			self.label.setPixmap(img)
			# self.resize(img.width(), img.height())
			self.show()

	def setImage(self,url,file):
		self.IMAGE_URL = url
		self.image = file
	
	def setJson(self,url,file):
		self.JSON_URL = url
		self.json = file
	
	def setNewJson(self,url,file=None):
		print("newjson")
		self.JSON_URL = url
		self.json = file
	

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui = MainWidget()
	ui.show()
	sys.exit(app.exec_())


