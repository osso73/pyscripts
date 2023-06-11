class Grep:
    def __init__(self, mainwindow):
        self.parent = mainwindow

        # buttons grep
        self.parent.action_script_grep.triggered.connect(lambda: self.parent.change_tab(self.tab_grep))
        self.parent.grep_go_button.clicked.connect(self.script_grep)
        self.parent.grep_help_button.clicked.connect(lambda: self.parent.show_help('grep'))
        self.parent.grep_folder_button.clicked.connect(lambda: self.parent.open_path(self.parent.grep_files))


    def script_grep(self):
        script = 'grep.py'

        files = self.parent.grep_files.text()
        pattern = self.parent.grep_pattern.text()
        args = [files, pattern]
        self.parent.run_script(script, args)

