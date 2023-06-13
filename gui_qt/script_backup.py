class Backup:
    def __init__(self, mainwindow):
        self.parent = mainwindow

        # buttons backup_to_zip
        self.parent.action_script_backup.triggered.connect(lambda: self.parent.change_tab(self.parent.tab_backup))
        self.parent.backup_go_button.clicked.connect(self.script_backup)
        self.parent.backup_help_button.clicked.connect(lambda: self.parent.show_help('backup_to_zip'))
        self.parent.backup_path_button.clicked.connect(lambda: self.parent.open_path(self.parent.backup_path))
        self.parent.backup_destination_button.clicked.connect(lambda: self.parent.open_path(self.parent.backup_destination))


    def script_backup(self):
        script = 'backup_to_zip'
        path = self.parent.backup_path.text()
        destination = self.parent.backup_destination.text()
        args = ["-d", destination, path]
        if self.parent.backup_compress_check.isChecked():
            args.insert(0, "-c")
        
        self.parent.run_script(script, args)
