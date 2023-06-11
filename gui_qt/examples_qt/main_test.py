from PySide6.QtCore import QProcess
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.setProgram('python')
        self.process.setArguments(['scripts/probabilidades.py', '-d2', '..'])
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.start()

    def handle_stdout(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.text_edit.append(output)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
