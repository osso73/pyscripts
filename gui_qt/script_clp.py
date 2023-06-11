class Clp:
    def __init__(self, mainwindow):
        self.parent = mainwindow

        # buttons clp
        self.parent.action_script_clp.triggered.connect(lambda: self.parent.change_tab(self.tab_clp))
        self.parent.clp_go_button.clicked.connect(self.script_clp)
        self.parent.clp_help_button.clicked.connect(lambda: self.parent.show_help('clp'))


    def script_clp(self):
        script = 'clp.py'
        
        if self.parent.clp_date_radio.isChecked():
            args = ["date"]
        
        elif self.parent.clp_to_regex_radio.isChecked():
            args = ["to-regex"]
        
        elif self.parent.clp_md_toc_radio.isChecked():
            args = ["md-toc"]
        
        elif self.parent.clp_comas_dots_radio.isChecked():
            args = ["comas-dots"]
        
        elif self.parent.clp_capitalize_radio.isChecked():
            args = ["capitalize"]
        
        elif self.parent.clp_list_radio.isChecked():
            args = ["list"]
        
        elif self.parent.clp_bullets_radio.isChecked():
            bullet = self.clp_bullets_text.text()
            args = ["bullets", bullet]
        
        elif self.parent.clp_extract_radio.isChecked():
            text = self.clp_extract_text.text()
            args = ["extract", ""]
        
        elif self.parent.clp_replace_radio.isChecked():
            original = self.clp_replace_original.text()
            new = self.clp_replace_new.text()
            args = ["replace", original, new]
        
        elif self.parent.clp_replace_regex_radio.isChecked():
            original = self.clp_replace_regex_original.text()
            new = self.clp_replace_regex_new.text()
            args = ["replace-regex", original, new]
        
        else:
            return
        
        self.parent.run_script(script, args)
        
