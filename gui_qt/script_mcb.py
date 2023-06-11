from PySide6.QtCore import QThread


class Mcb:
    def __init__(self, mainwindow):
        self.parent = mainwindow

        # buttons mcb
        self.parent.action_script_mcb.triggered.connect(lambda: self.parent.change_tab(self.parent.tab_mcb))
        self.parent.mcb_go_button.clicked.connect(self.script_mcb)
        self.parent.mcb_help_button.clicked.connect(lambda: self.parent.show_help('mcb'))


    def script_mcb(self):
        script = 'mcb.py'

        if self.parent.mcb_load_radio.isChecked():
            keyword = self.parent.mcb_load_kw.text()
            args = [keyword]
        elif self.parent.mcb_save_radio.isChecked():
            keyword = self.parent.mcb_save_kw.text()
            args = ['save', keyword]
        elif self.parent.mcb_del_radio.isChecked():
            keyword = self.parent.mcb_delete_kw.text()
            args = ['del', keyword]
        elif self.parent.mcb_list_radio.isChecked():
            args = ['list']
        else:
            self.parent.output_box.append("ERROR!! Please select one option.")
            return
      
        self.parent.run_script(script, args)

        if args == ['list']:
            QThread.sleep(1)  # wait for the process to finish
            self.parent.output_box.append("\n")
            self.parent.output_box.paste()
