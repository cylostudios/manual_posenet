from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget
import sys
from points import Points


class MainWidget(QMainWindow):
	def __init__(self):

		super().__init__()

		self.setWindowTitle("Drag and Drop")
		self.resize(720, 480)
		self.setAcceptDrops(True)

		self.central_widget = QWidget()               
		self.setCentralWidget(self.central_widget)    
		lay = QVBoxLayout(self.central_widget)

		self.label = QLabel(self)
		self.points = Points()
		self.central_widget.showFullScreen()
		lay.addWidget(self.points)
		# lay.addWidget(self.echoText)


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


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui = MainWidget()
	ui.show()
	sys.exit(app.exec_())


