from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import sys
import os

class AboutDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("Mozarella Ashbadger")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap(os.path.join('icons', 'ma-icon-128.png')))
        layout.addWidget(logo)

        layout.addWidget( QLabel("Version 23.35.211.233434"))
        layout.addWidget( QLabel("Copyright 2021 Mozarella Inc."))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment( Qt.AlignHCenter )

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect( self.tab_open_doubleclick )
        self.tabs.currentChanged.connect( self.current_tab_changed )
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect( self.close_current_tab )
        
        self.setCentralWidget(self.tabs)
    
##        self.browser = QWebEngineView()
##        self.browser.setUrl(QUrl("http://www.google.com"))

##        self.browser.urlChanged.connect(self.update_urlbar)
##        self.browser.loadFinished.connect(self.update_title)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navtb = QToolBar("Navigation")
        navtb.setIconSize( QSize(16,16) )
        self.addToolBar(navtb)

        back_btn = QAction( QIcon(os.path.join('icons','arrow-180.png')), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        navtb.addAction(back_btn)

        next_btn = QAction( QIcon(os.path.join('icons','arrow-000.png')), "Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget.forward())
        navtb.addAction(next_btn)

        reload_btn = QAction( QIcon(os.path.join('icons','arrow-circle-315.png')),"Reload",self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

        home_btn = QAction(QIcon(os.path.join('icons','home.png')),"Home", self)
        home_btn.setStatusTip("Go Home")
        home_btn.triggered.connect( self.navigate_home )
        navtb.addAction(home_btn)

        navtb.addSeparator()

        self.httpsicon = QLabel()
        self.httpsicon.setPixmap( QPixmap(os.path.join('icons','lock-nossl.png')))
        navtb.addWidget(self.httpsicon)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect( self.navigate_to_url )
        navtb.addWidget(self.urlbar)

        stop_btn = QAction( QIcon(os.path.join('icons','cross-circle.png')), "Stop",self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

        file_menu = self.menuBar().addMenu("&File")

        """
        The slot method for opening a file uses the built-in
        `QFileDialog.getOpenFileName()` method to create a file-open dialog
        and get a name. We restrict the names by default to file matching
        `\*.htm` or `*.html`.

        We read the file into a variable `html` using standard python functions
        then use `.setHtml()` to load the HTMK into the browser.
        """

        open_file_action = QAction(QIcon(os.path.join('icons','disk--arrow.png')),"Open file...", self)
        open_file_action.setStatusTip("Open from file")
        open_file_action.triggered.connect( self.open_file )
        file_menu.addAction(open_file_action)

        save_file_action = QAction(QIcon(os.path.join('icons','disk--pencil.png')), "Save page as...", self)
        save_file_action.setStatusTip("Save current page to file")
        save_file_action.triggered.connect( self.save_file )
        file_menu.addAction(save_file_action)

        help_menu = self.menuBar().addMenu("&Help")

        about_action = QAction( QIcon(os.path.join('icons','question.png')),"About Mozarella Ashbadger", self)
        about_action.setStatusTip("Find out more about Mzarella Ashbadger")
        about_action.triggered.connect( self.about )
        help_menu.addAction(about_action)

        navigate_mozarella_action = QAction( QIcon(os.path.join('icons','lifebuoy.png')),"Mozarella Ashbadger Homepage", self)
        navigate_mozarella_action.setStatusTip("Go to Mozarella Ashbadger Homepage")
        navigate_mozarella_action.triggered.connect( self.navigate_mozarella )
        help_menu.addAction(navigate_mozarella_action)


        try:
            self.add_new_tab(QUrl('https://www.google.com'), "Homepage")
        except Exception as err:
            print(err.args)
        

        self.show()

        self.setWindowTitle("Mozarella Ashbadger")
        self.setWindowIcon(QIcon(os.path.join('images', 'ma-icon-64.png'))) 

    def tab_open_doubleclick(self, i):
        try:
            if i == -1: # No tab under the click
                self.add_new_tab()
        except Exception as err:
            print(err.args)

            
    def current_tab_changed(self, i):
        try:
            qurl = self.tabs.currentWidget().url()
            self.update_urlbar( qurl, self.tabs.currentWidget() )
            self.update_title(self.tabs.currentWidget())
        except Exception as err:
            print(err.args)

            
    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return

        self.tabs.removeTab(i)


    def add_new_tab(self, qurl=None, label="Blank"):

        
            
        if qurl is None:
            qurl = QUrl('http://www.google.com')

        try:
            print(qurl)
            browser = QWebEngineView()
            browser.setUrl( qurl )
            print(browser)
            i = self.tabs.addTab(browser, label)
            print(i)

            self.tabs.setCurrentIndex(i)
        except Exception as err:
            print(err.args)
        # More difficult! We only want to update the url when it's from the
        # correct tab

        browser.urlChanged.connect( lambda qurl, browser=browser:
                                    self.update_urlbar(qurl, browser))

        browser.loadFinished.connect( lambda _, i = i, browser = browser:
                                      self.tabs.setTabText(i, browser.page().title()))


    def navigate_home(self):
        try:
            print(self.tabs.currentWidget())
            self.tabs.currentWidget().setUrl( QUrl("http://www.google.com") )
        except Exception as err:
            print(err.args)

    def navigate_to_url(self):
        q = QUrl( self.urlbar.text() )
        if q.scheme() == "":
            q.setScheme("http")

        try:
            self.tabs.currentWidget().setUrl(q)
        except Exception as err:
            print(err.args)

    def update_urlbar(self, q, browser=None):

        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        if q.scheme() == 'https':
            # Secure padLock icon
            self.httpsicon.setPixmap( QPixmap(os.path.join('icons','lock-ssl.png')))

        else:
            # Unsecure padLock icon
            self.httpsicon.setPixmap( QPixmap(os.path.join('icons','lock-nossl.png')))

        self.urlbar.setText( q.toString() )
        self.urlbar.setCursorPosition(0)


    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            # IF this signal is not from the current tab, ignore
            return
        
        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle("%s - Mozarella Ashbadger" % title)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
                                                  "All file (*.*)")
        try:
            
            if filename:
                with open(filename, 'r') as f:
                    html = f.read()

                self.tabs.currentWidget().setHtml( html )
                self.urlbar.setText( filename )
        except Exception as err:
            print(err.args)
            pass

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
                                                  "All files (*.*)")
        def processHtml(html):
            print(html)
        
        try:
            
            if filename:
                html = self.tabs.currentWidget().page().toHtml(processHtml)
                print(html)
                with open(filename, 'w') as f:
                    f.write(html.encode('utf8'))
        except Exception as err:
            print(err.args)

        

    def print_page(self):
        dlg = QPrintPreviewDialog()
        dlg.paintRequested.connect(self.browser.print_)
        dlg.exec_()

    def navigate_mozarella(self):
        self.tabs.currentWidget().setUrl(QUrl("https://www.learnpyqt.com/courses/example-browser/"))

    def about(self):
        try:
            dlg = AboutDialog()
            dlg.exec_()
        except Exception as err:
            print(err.args)

        


app = QApplication(sys.argv)
window  = MainWindow()
app.exec_()
        
