from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import time
import traceback, sys

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are

    finished
        No data

    error
        tuple(exctype, value, trcaback.format_exec() )
        
    result
        object data returned from processing, anything
    '''

    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(float)
    

class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up

    :param callback: The function callback to run in this worker thread. Supplied args and
                    kwargs will be passed through to the runner
    :type callback: function

    :param args: Arguments to make available to the run code
    :param kwargs: Keywords arguments to make available to the run code
    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress
        
    def run(self):
##        '''
##        Your code goes in this function
##        '''
##        print("Thread start")
##        time.sleep(5)
##        print("Thread complete")
        '''
        Initialize the runner function with passed self.args, self.kwargs
        '''
        
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(
                *self.args, **self.kwargs
            )
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result) # Return the result of the processing
        finally:
            self.signals.finished.emit() # Done

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        c = QPushButton("?")
        c.pressed.connect(self.change_message)

        layout.addWidget(self.l)
        layout.addWidget(b)
        layout.addWidget(c)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)
        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def progress_fn(self, n):
        print("%d%% done" % n)

    def change_message(self):
        self.message = "OH NO"

    def execute_this_fn(self, progress_callback):
        for n in range(0, 10):
            time.sleep(1)
            progress_callback.emit(n*100/9)
        return "Done."

    def print_output(self, s):
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE!")

    def oh_no(self):
        # PAss the function to execute
        worker = Worker(self.execute_this_fn) #Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)

##        for n in range(100):  
##            time.sleep(0.1)
##            self.l.setText(self.message)
##            QApplication.processEvents()

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)


app = QApplication([])
window = MainWindow()
app.exec_()
