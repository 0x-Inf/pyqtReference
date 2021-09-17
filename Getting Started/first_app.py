import sys
from PyQt5.QtWidgets import QApplication

# You need one (and ony one) QApplication instance per application
# Pass in sys.argv to allow command line arguments for your app
# If you know you wont't use command Line arguments QApplication([]) is fine

app = QApplication(sys.argv)

# start the event loop.
app.exec_()

# Your application won't reach here until you exit and the event loop has stopped
