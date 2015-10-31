#-*- coding: utf-8 -*-
import utils
import signals
import config
import error
from ui.Ui_CreateTcpServerForm import Ui_CreateTcpServerForm
from PyQt4 import QtGui
from PyQt4 import QtCore

class CreateTcpServerDialog(QtGui.QDialog):
	
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_CreateTcpServerForm()
        self.ui.setupUi(self)
        self.initIpList()
        self.setModal(True)
        self.setupSignals()
    
    def initIpList(self):
        self.ui.ipCmbBox.addItems(config.DEFAULT_SERVER_IP_LIST + utils.getLocalIpList())
        
    def setupSignals(self):
        self.ui.okBtn.clicked.connect(self.onOkBtnClicked)
        self.ui.cancelBtn.clicked.connect(self.close)
        
    def onOkBtnClicked(self):
        strPort = utils.qstr2str(self.ui.portCmbBox.currentText())
        if not strPort.isdigit():
            return
            
        port = int(strPort)
        if not utils.isPortOk(port):
            return
        
        self.emit(signals.SIG_CREATE_TCP_SERVER, utils.qstr2str(self.ui.ipCmbBox.currentText()), port)
        self.close()
	
    def show_(self):
        if self.ui.portCmbBox.currentText() == "":
            self.ui.portCmbBox.setEditText(`utils.randomPort()`)
        
        self.ui.portCmbBox.setFocus()
        self.show()