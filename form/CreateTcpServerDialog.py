#-*- coding: utf-8 -*-
from ui.Ui_CreateTcpServerForm import Ui_CreateTcpServerForm
from PyQt4 import QtGui

class CreateTcpServerDialog(QtGui.QDialog):
	
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_CreateTcpServerForm()
        self.ui.setupUi(self)
		
        self.setModal(True)
        self.setupSignals()
    
    def setupSignals(self):
        self.ui.okBtn.clicked.connect(self.onOkBtnClicked)
        self.ui.cancelBtn.clicked.connect(self.close)
        
    def onOkBtnClicked(self):
        print 123
    
	