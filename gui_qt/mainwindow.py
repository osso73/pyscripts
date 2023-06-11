from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PySide6.QtCore import QProcess
from PySide6.QtCore import QThread
from script_tree_info import TreeInfo
from script_clp import Clp
from script_backup import Backup
from script_alarm import Alarm
from script_grep import Grep
from script_mcb import Mcb

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.set_general_actions()
        self.set_scripts_buttons()
    

    def set_general_actions(self):
        # general actions
        self.action_quit.triggered.connect(self.app.quit)
        self.action_about.triggered.connect(self.about)
        self.action_aboutQt.triggered.connect(self.app.aboutQt)
        self.action_zoom_in.triggered.connect(self.output_box.zoomIn)
        self.action_zoom_out.triggered.connect(self.output_box.zoomOut)
        self.action_clear.triggered.connect(self.output_box.clear)
        self.action_copy.triggered.connect(self.output_box.copy)


    def set_scripts_buttons(self):
        TreeInfo(self)
        Clp(self)
        Backup(self)
        Alarm(self)
        Grep(self)
        Mcb(self)


    def about(self):
        msg = """This is a GUI interface to run
command line scripts.

Author: osso
        """
        QMessageBox.information(self, "About", msg)


    def change_tab(self, tab):
        self.tab_widget.setCurrentWidget(tab)
        
    
    def run_script(self, script, args):
        args = [f'scripts/{script}', *args]

        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.setProgram('.venv/Scripts/python.exe')
        self.process.setArguments(args)
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.finished.connect(self.process_finished)
        cmd = " ".join(args)
        msg = f'Executing process: "{cmd}" ...'
        self.output_box.append(msg)
        self.process.start()


    def handle_stdout(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.output_box.append(output)


    def process_finished(self):
        self.output_box.append("Process finished!")
    

    def show_help(self, script):
        self.output_box.clear()
        self.run_script(script+'.py', ['--help'])
    

    def open_path(self, line_edit):
        path = QFileDialog.getExistingDirectory(self, "Open directory", "")
        if path:
            line_edit.setText(path)
