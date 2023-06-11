class Alarm:
    def __init__(self, mainwindow):
        self.parent = mainwindow

        # buttons alarm
        self.parent.action_script_alarm.triggered.connect(lambda: self.parent.change_tab(self.tab_alarm))
        self.parent.alarm_go_button.clicked.connect(self.script_alarm)
        self.parent.alarm_help_button.clicked.connect(lambda: self.parent.show_help('alarm'))


    def script_alarm(self):
        script = 'alarm.py'

        msg = self.parent.alarm_message.text()

        if self.parent.alarm_wait_radio.isChecked():
            time = self.parent.alarm_wait_text.text().split()
            args = ['--wait', *time]
        elif self.parent.alarm_at_radio.isChecked():
            time = self.parent.alarm_at_text.text().split()
            args = ['--at', *time]
        else:
            self.parent.output_box.append("ERROR!! Please select one option.")
            return
        
        if msg:
            args.append('--message')
            args.append(msg)
        
        self.parent.run_script(script, args)
