from PyQt5 import QtWidgets, QtCore
from configuration.Appconfig import Appconfig
from configparser import ConfigParser
import os


# This Class creates NgSpice Window
class NgspiceWidget(QtWidgets.QWidget):

    def __init__(self, command, projPath):
        """
        - Creates constructor for NgspiceWidget class.
        - Checks whether OS is Linux or Windows and
          creates Ngspice window accordingly.
        """
        QtWidgets.QWidget.__init__(self)
        self.obj_appconfig = Appconfig()
        self.process = QtCore.QProcess(self)
        self.terminal = QtWidgets.QWidget(self)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.terminal)

        print("Argument to ngspice command : ", command)

        if os.name == 'nt':     # For Windows OS
            parser_nghdl = ConfigParser()
            parser_nghdl.read(
                os.path.join('library', 'config', '.nghdl', 'config.ini')
            )

            msys_home = parser_nghdl.get('COMPILER', 'MSYS_HOME')

            tempdir = os.getcwd()
            projPath = self.obj_appconfig.current_project["ProjectName"]
            os.chdir(projPath)
            self.command = 'cmd /c '+'"start /min ' + \
                msys_home + "/usr/bin/mintty.exe ngspice -p " + command + '"'
            self.process.start(self.command)
            os.chdir(tempdir)

        else:                   # For Linux OS
            # self.command = "cd " + projPath + \
            #     ";ngspice -r " + command.replace(".cir.out", ".raw") + \
            #     " " + command
            # Creating argument for process
            self.args = ['-b', '-r', command.replace(".cir.out", ".raw"), command]
            self.process.setWorkingDirectory(projPath)
            self.process.start('ngspice', self.args)
            self.process.readyReadStandardOutput.connect(lambda: self.readyReadAll())
            self.obj_appconfig.process_obj.append(self.process)
            print(self.obj_appconfig.proc_dict)
            (
                self.obj_appconfig.proc_dict
                [self.obj_appconfig.current_project['ProjectName']].append(
                    self.process.pid())
            )
            self.gawProcess = QtCore.QProcess(self)
            self.command = "gaw " + command.replace(".cir.out", ".raw")
            self.gawProcess.start('sh', ['-c', self.command])
            print(self.command)
    
    @QtCore.pyqtSlot()
    def readyReadAll(self):
        self.obj_appconfig.noteArea['Note'].append(
            str(self.process.readAllStandardOutput().data(), encoding='utf-8')
        )
