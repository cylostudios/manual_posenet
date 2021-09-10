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
		self.resize(900, 900)
		self.setAcceptDrops(True)

		self.central_widget = QWidget()               
		self.setCentralWidget(self.central_widget)    
		self.central_widget.showFullScreen()

		layout = QVBoxLayout(self.central_widget)
		# self.setLayout(layout)
		#create widgets
		self.label = QLabel(self)
		self.pointsWidget = PointsWidget()
		self.commandWidget = CommandWidget()

		#style widgets
		self.setStyleSheet("\
			background-color:green;\
		")
		self.pointsWidget.setStyleSheet("width: 800;height: 600;background-color:white;border: 10px solid black;")
		self.commandWidget.setStyleSheet("color: white; background-color:green; border: 1px solid black;")

		#connections
		self.commandWidget.setImage.connect(self.setImage)
		self.commandWidget.setJson.connect(self.setPose)
		self.commandWidget.newJson.connect(self.setPose)
		self.commandWidget.saveSignal.connect(self.pointsWidget.save)
		self.commandWidget.resetSignal.connect(self.pointsWidget.reset)

		# add to this
		layout.addWidget(self.commandWidget)
		layout.addWidget(self.pointsWidget)

		# alignment
		layout.setAlignment(self.commandWidget,Qt.AlignTop)
		layout.setAlignment(self.pointsWidget,Qt.AlignTop | Qt.AlignCenter)

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
		print("adding image - %s" % url)
		self.IMAGE_URL = url
		self.image = file
		# emit file
		self.pointsWidget.setImage(url,file)
	
	def setPose(self,url,file=None):
		print("adding pose - %s" % url)
		self.POSE_URL = url
		self.pose = file
		# emit file
		self.pointsWidget.setPose(url,file)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui = MainWidget()
	ui.show()
	sys.exit(app.exec_())


