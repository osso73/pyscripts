class TreeInfo:
    def __init__(self, mainwindow):
        self.parent = mainwindow

        # buttons tree_info
        self.parent.action_script_tree_info.triggered.connect(lambda: self.parent.change_tab(self.tab_tree_info))
        self.parent.tree_info_go_button.clicked.connect(self.script_tree_info)
        self.parent.tree_info_help_button.clicked.connect(lambda: self.parent.show_help('tree_info'))
        self.parent.tree_info_path_button.clicked.connect(lambda: self.parent.open_path(self.tree_info_path_text))


    def script_tree_info(self):
        script = 'tree_info'

        # parameters
        start_path = self.parent.tree_info_path_text.text()
        depth = f"-d{self.parent.tree_info_depth.text()}"
        args = [depth, start_path]

        self.parent.run_script(script, args)


