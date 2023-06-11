# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_v2.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QStatusBar, QTabWidget,
    QTextEdit, QToolBar, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(928, 684)
        self.action_quit = QAction(MainWindow)
        self.action_quit.setObjectName(u"action_quit")
        icon = QIcon()
        icon.addFile(u":/icons/quit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_quit.setIcon(icon)
        self.action_script_tree_info = QAction(MainWindow)
        self.action_script_tree_info.setObjectName(u"action_script_tree_info")
        icon1 = QIcon()
        icon1.addFile(u":/icons/script.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_script_tree_info.setIcon(icon1)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        icon2 = QIcon()
        icon2.addFile(u":/icons/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_about.setIcon(icon2)
        self.action_aboutQt = QAction(MainWindow)
        self.action_aboutQt.setObjectName(u"action_aboutQt")
        icon3 = QIcon()
        icon3.addFile(u":/icons/aboutQt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_aboutQt.setIcon(icon3)
        self.action_script_clp = QAction(MainWindow)
        self.action_script_clp.setObjectName(u"action_script_clp")
        self.action_script_clp.setIcon(icon1)
        self.action_zoom_in = QAction(MainWindow)
        self.action_zoom_in.setObjectName(u"action_zoom_in")
        icon4 = QIcon()
        icon4.addFile(u":/icons/zoom_in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_zoom_in.setIcon(icon4)
        self.action_zoom_out = QAction(MainWindow)
        self.action_zoom_out.setObjectName(u"action_zoom_out")
        icon5 = QIcon()
        icon5.addFile(u":/icons/zoom_out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_zoom_out.setIcon(icon5)
        self.action_clear = QAction(MainWindow)
        self.action_clear.setObjectName(u"action_clear")
        icon6 = QIcon()
        icon6.addFile(u":/icons/edit-clear.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_clear.setIcon(icon6)
        self.action_copy = QAction(MainWindow)
        self.action_copy.setObjectName(u"action_copy")
        icon7 = QIcon()
        icon7.addFile(u":/icons/edit-copy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_copy.setIcon(icon7)
        self.action_script_backup = QAction(MainWindow)
        self.action_script_backup.setObjectName(u"action_script_backup")
        self.action_script_backup.setIcon(icon1)
        self.action_script_alarm = QAction(MainWindow)
        self.action_script_alarm.setObjectName(u"action_script_alarm")
        self.action_script_alarm.setIcon(icon1)
        self.action_script_grep = QAction(MainWindow)
        self.action_script_grep.setObjectName(u"action_script_grep")
        self.action_script_grep.setIcon(icon1)
        self.action_script_mcb = QAction(MainWindow)
        self.action_script_mcb.setObjectName(u"action_script_mcb")
        self.action_script_mcb.setIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.output_box = QTextEdit(self.centralwidget)
        self.output_box.setObjectName(u"output_box")
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(12)
        self.output_box.setFont(font)
        self.output_box.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 127);")
        self.output_box.setReadOnly(True)

        self.gridLayout_3.addWidget(self.output_box, 3, 0, 1, 1)

        self.tab_widget = QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName(u"tab_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_widget.sizePolicy().hasHeightForWidth())
        self.tab_widget.setSizePolicy(sizePolicy)
        self.tab_tree_info = QWidget()
        self.tab_tree_info.setObjectName(u"tab_tree_info")
        self.verticalLayout_2 = QVBoxLayout(self.tab_tree_info)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tree_info_path_button = QPushButton(self.tab_tree_info)
        self.tree_info_path_button.setObjectName(u"tree_info_path_button")
        icon8 = QIcon()
        icon8.addFile(u":/icons/open_folder.svg", QSize(), QIcon.Normal, QIcon.On)
        self.tree_info_path_button.setIcon(icon8)

        self.gridLayout.addWidget(self.tree_info_path_button, 0, 3, 1, 1)

        self.label_2 = QLabel(self.tab_tree_info)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.tree_info_help_button = QPushButton(self.tab_tree_info)
        self.tree_info_help_button.setObjectName(u"tree_info_help_button")
        icon9 = QIcon()
        icon9.addFile(u":/icons/help-help.svg", QSize(), QIcon.Normal, QIcon.On)
        self.tree_info_help_button.setIcon(icon9)

        self.gridLayout.addWidget(self.tree_info_help_button, 0, 4, 1, 1)

        self.tree_info_depth = QSpinBox(self.tab_tree_info)
        self.tree_info_depth.setObjectName(u"tree_info_depth")
        self.tree_info_depth.setMinimum(0)
        self.tree_info_depth.setValue(0)

        self.gridLayout.addWidget(self.tree_info_depth, 1, 2, 1, 1)

        self.tree_info_path_text = QLineEdit(self.tab_tree_info)
        self.tree_info_path_text.setObjectName(u"tree_info_path_text")

        self.gridLayout.addWidget(self.tree_info_path_text, 0, 2, 1, 1)

        self.label = QLabel(self.tab_tree_info)
        self.label.setObjectName(u"label")
        self.label.setBaseSize(QSize(0, 0))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.tree_info_go_button = QPushButton(self.tab_tree_info)
        self.tree_info_go_button.setObjectName(u"tree_info_go_button")
        icon10 = QIcon()
        icon10.addFile(u":/icons/script.png", QSize(), QIcon.Normal, QIcon.On)
        self.tree_info_go_button.setIcon(icon10)

        self.gridLayout.addWidget(self.tree_info_go_button, 1, 4, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.tab_widget.addTab(self.tab_tree_info, "")
        self.tab_clp = QWidget()
        self.tab_clp.setObjectName(u"tab_clp")
        self.gridLayout_2 = QGridLayout(self.tab_clp)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.clp_comas_dots_radio = QRadioButton(self.tab_clp)
        self.clp_comas_dots_radio.setObjectName(u"clp_comas_dots_radio")

        self.gridLayout_2.addWidget(self.clp_comas_dots_radio, 3, 2, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.clp_replace_regex_radio = QRadioButton(self.tab_clp)
        self.clp_replace_regex_radio.setObjectName(u"clp_replace_regex_radio")

        self.horizontalLayout_4.addWidget(self.clp_replace_regex_radio)

        self.clp_replace_regex_original = QLineEdit(self.tab_clp)
        self.clp_replace_regex_original.setObjectName(u"clp_replace_regex_original")

        self.horizontalLayout_4.addWidget(self.clp_replace_regex_original)

        self.clp_replace_regex_new = QLineEdit(self.tab_clp)
        self.clp_replace_regex_new.setObjectName(u"clp_replace_regex_new")

        self.horizontalLayout_4.addWidget(self.clp_replace_regex_new)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 5, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.clp_replace_radio = QRadioButton(self.tab_clp)
        self.clp_replace_radio.setObjectName(u"clp_replace_radio")

        self.horizontalLayout_3.addWidget(self.clp_replace_radio)

        self.clp_replace_original = QLineEdit(self.tab_clp)
        self.clp_replace_original.setObjectName(u"clp_replace_original")

        self.horizontalLayout_3.addWidget(self.clp_replace_original)

        self.clp_replace_new = QLineEdit(self.tab_clp)
        self.clp_replace_new.setObjectName(u"clp_replace_new")

        self.horizontalLayout_3.addWidget(self.clp_replace_new)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 5, 1, 1)

        self.clp_date_radio = QRadioButton(self.tab_clp)
        self.clp_date_radio.setObjectName(u"clp_date_radio")

        self.gridLayout_2.addWidget(self.clp_date_radio, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.clp_bullets_radio = QRadioButton(self.tab_clp)
        self.clp_bullets_radio.setObjectName(u"clp_bullets_radio")

        self.horizontalLayout.addWidget(self.clp_bullets_radio)

        self.clp_bullets_text = QLineEdit(self.tab_clp)
        self.clp_bullets_text.setObjectName(u"clp_bullets_text")

        self.horizontalLayout.addWidget(self.clp_bullets_text)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 4, 1, 1)

        self.clp_list_radio = QRadioButton(self.tab_clp)
        self.clp_list_radio.setObjectName(u"clp_list_radio")

        self.gridLayout_2.addWidget(self.clp_list_radio, 3, 3, 1, 1)

        self.clp_md_toc_radio = QRadioButton(self.tab_clp)
        self.clp_md_toc_radio.setObjectName(u"clp_md_toc_radio")

        self.gridLayout_2.addWidget(self.clp_md_toc_radio, 0, 2, 1, 1)

        self.clp_capitalize_radio = QRadioButton(self.tab_clp)
        self.clp_capitalize_radio.setObjectName(u"clp_capitalize_radio")

        self.gridLayout_2.addWidget(self.clp_capitalize_radio, 0, 3, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.clp_extract_radio = QRadioButton(self.tab_clp)
        self.clp_extract_radio.setObjectName(u"clp_extract_radio")

        self.horizontalLayout_2.addWidget(self.clp_extract_radio)

        self.clp_extract_text = QLineEdit(self.tab_clp)
        self.clp_extract_text.setObjectName(u"clp_extract_text")

        self.horizontalLayout_2.addWidget(self.clp_extract_text)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 4, 1, 1)

        self.clp_to_regex_radio = QRadioButton(self.tab_clp)
        self.clp_to_regex_radio.setObjectName(u"clp_to_regex_radio")

        self.gridLayout_2.addWidget(self.clp_to_regex_radio, 3, 1, 1, 1)

        self.clp_go_button = QPushButton(self.tab_clp)
        self.clp_go_button.setObjectName(u"clp_go_button")
        self.clp_go_button.setIcon(icon10)

        self.gridLayout_2.addWidget(self.clp_go_button, 3, 6, 1, 1)

        self.clp_help_button = QPushButton(self.tab_clp)
        self.clp_help_button.setObjectName(u"clp_help_button")
        self.clp_help_button.setIcon(icon9)

        self.gridLayout_2.addWidget(self.clp_help_button, 0, 6, 1, 1)

        self.gridLayout_2.setColumnStretch(4, 1)
        self.gridLayout_2.setColumnStretch(5, 2)
        self.tab_widget.addTab(self.tab_clp, "")
        self.tab_backup = QWidget()
        self.tab_backup.setObjectName(u"tab_backup")
        self.gridLayout_4 = QGridLayout(self.tab_backup)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.backup_help_button = QPushButton(self.tab_backup)
        self.backup_help_button.setObjectName(u"backup_help_button")
        self.backup_help_button.setIcon(icon9)

        self.gridLayout_4.addWidget(self.backup_help_button, 0, 3, 1, 1)

        self.backup_go_button = QPushButton(self.tab_backup)
        self.backup_go_button.setObjectName(u"backup_go_button")
        self.backup_go_button.setIcon(icon10)

        self.gridLayout_4.addWidget(self.backup_go_button, 1, 3, 1, 1)

        self.backup_compress_check = QCheckBox(self.tab_backup)
        self.backup_compress_check.setObjectName(u"backup_compress_check")

        self.gridLayout_4.addWidget(self.backup_compress_check, 0, 2, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.tab_backup)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.backup_destination = QLineEdit(self.tab_backup)
        self.backup_destination.setObjectName(u"backup_destination")

        self.horizontalLayout_6.addWidget(self.backup_destination)

        self.backup_destination_button = QPushButton(self.tab_backup)
        self.backup_destination_button.setObjectName(u"backup_destination_button")
        self.backup_destination_button.setIcon(icon8)

        self.horizontalLayout_6.addWidget(self.backup_destination_button)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.tab_backup)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.backup_path = QLineEdit(self.tab_backup)
        self.backup_path.setObjectName(u"backup_path")

        self.horizontalLayout_5.addWidget(self.backup_path)

        self.backup_path_button = QPushButton(self.tab_backup)
        self.backup_path_button.setObjectName(u"backup_path_button")
        self.backup_path_button.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.backup_path_button)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.tab_widget.addTab(self.tab_backup, "")
        self.tab_alarm = QWidget()
        self.tab_alarm.setObjectName(u"tab_alarm")
        self.horizontalLayout_10 = QHBoxLayout(self.tab_alarm)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.alarm_message = QLineEdit(self.tab_alarm)
        self.alarm_message.setObjectName(u"alarm_message")

        self.horizontalLayout_19.addWidget(self.alarm_message)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.alarm_help_button = QPushButton(self.tab_alarm)
        self.alarm_help_button.setObjectName(u"alarm_help_button")
        self.alarm_help_button.setIcon(icon9)

        self.gridLayout_5.addWidget(self.alarm_help_button, 0, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.alarm_at_radio = QRadioButton(self.tab_alarm)
        self.alarm_at_radio.setObjectName(u"alarm_at_radio")

        self.horizontalLayout_8.addWidget(self.alarm_at_radio)

        self.alarm_at_text = QLineEdit(self.tab_alarm)
        self.alarm_at_text.setObjectName(u"alarm_at_text")

        self.horizontalLayout_8.addWidget(self.alarm_at_text)


        self.gridLayout_5.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.alarm_go_button = QPushButton(self.tab_alarm)
        self.alarm_go_button.setObjectName(u"alarm_go_button")
        self.alarm_go_button.setIcon(icon10)

        self.gridLayout_5.addWidget(self.alarm_go_button, 2, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.alarm_wait_radio = QRadioButton(self.tab_alarm)
        self.alarm_wait_radio.setObjectName(u"alarm_wait_radio")

        self.horizontalLayout_9.addWidget(self.alarm_wait_radio)

        self.alarm_wait_text = QLineEdit(self.tab_alarm)
        self.alarm_wait_text.setObjectName(u"alarm_wait_text")

        self.horizontalLayout_9.addWidget(self.alarm_wait_text)


        self.gridLayout_5.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)


        self.horizontalLayout_19.addLayout(self.gridLayout_5)

        self.horizontalLayout_19.setStretch(0, 1)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_19)

        self.tab_widget.addTab(self.tab_alarm, "")
        self.tab_grep = QWidget()
        self.tab_grep.setObjectName(u"tab_grep")
        self.gridLayout_6 = QGridLayout(self.tab_grep)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.tab_grep)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_11.addWidget(self.label_6)

        self.grep_files = QLineEdit(self.tab_grep)
        self.grep_files.setObjectName(u"grep_files")

        self.horizontalLayout_11.addWidget(self.grep_files)

        self.grep_folder_button = QPushButton(self.tab_grep)
        self.grep_folder_button.setObjectName(u"grep_folder_button")
        self.grep_folder_button.setIcon(icon8)

        self.horizontalLayout_11.addWidget(self.grep_folder_button)


        self.gridLayout_6.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_7 = QLabel(self.tab_grep)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_12.addWidget(self.label_7)

        self.grep_pattern = QLineEdit(self.tab_grep)
        self.grep_pattern.setObjectName(u"grep_pattern")

        self.horizontalLayout_12.addWidget(self.grep_pattern)


        self.gridLayout_6.addLayout(self.horizontalLayout_12, 2, 0, 1, 1)

        self.grep_go_button = QPushButton(self.tab_grep)
        self.grep_go_button.setObjectName(u"grep_go_button")
        self.grep_go_button.setIcon(icon10)

        self.gridLayout_6.addWidget(self.grep_go_button, 2, 2, 1, 1)

        self.grep_help_button = QPushButton(self.tab_grep)
        self.grep_help_button.setObjectName(u"grep_help_button")
        self.grep_help_button.setIcon(icon9)

        self.gridLayout_6.addWidget(self.grep_help_button, 1, 2, 1, 1)

        self.tab_widget.addTab(self.tab_grep, "")
        self.tab_mcb = QWidget()
        self.tab_mcb.setObjectName(u"tab_mcb")
        self.gridLayout_7 = QGridLayout(self.tab_mcb)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.mcb_help_button = QPushButton(self.tab_mcb)
        self.mcb_help_button.setObjectName(u"mcb_help_button")
        self.mcb_help_button.setIcon(icon9)

        self.gridLayout_7.addWidget(self.mcb_help_button, 0, 2, 1, 1)

        self.mcb_go_button = QPushButton(self.tab_mcb)
        self.mcb_go_button.setObjectName(u"mcb_go_button")
        self.mcb_go_button.setIcon(icon10)

        self.gridLayout_7.addWidget(self.mcb_go_button, 1, 2, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.mcb_del_radio = QRadioButton(self.tab_mcb)
        self.mcb_del_radio.setObjectName(u"mcb_del_radio")

        self.horizontalLayout_15.addWidget(self.mcb_del_radio)

        self.mcb_delete_kw = QLineEdit(self.tab_mcb)
        self.mcb_delete_kw.setObjectName(u"mcb_delete_kw")

        self.horizontalLayout_15.addWidget(self.mcb_delete_kw)


        self.gridLayout_7.addLayout(self.horizontalLayout_15, 0, 1, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.mcb_save_radio = QRadioButton(self.tab_mcb)
        self.mcb_save_radio.setObjectName(u"mcb_save_radio")

        self.horizontalLayout_16.addWidget(self.mcb_save_radio)

        self.mcb_save_kw = QLineEdit(self.tab_mcb)
        self.mcb_save_kw.setObjectName(u"mcb_save_kw")

        self.horizontalLayout_16.addWidget(self.mcb_save_kw)


        self.gridLayout_7.addLayout(self.horizontalLayout_16, 1, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.mcb_load_radio = QRadioButton(self.tab_mcb)
        self.mcb_load_radio.setObjectName(u"mcb_load_radio")

        self.horizontalLayout_13.addWidget(self.mcb_load_radio)

        self.mcb_load_kw = QLineEdit(self.tab_mcb)
        self.mcb_load_kw.setObjectName(u"mcb_load_kw")

        self.horizontalLayout_13.addWidget(self.mcb_load_kw)


        self.gridLayout_7.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)

        self.mcb_list_radio = QRadioButton(self.tab_mcb)
        self.mcb_list_radio.setObjectName(u"mcb_list_radio")

        self.gridLayout_7.addWidget(self.mcb_list_radio, 1, 1, 1, 1)

        self.tab_widget.addTab(self.tab_mcb, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_8 = QGridLayout(self.tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pdf_logging = QComboBox(self.tab)
        self.pdf_logging.setObjectName(u"pdf_logging")

        self.gridLayout_8.addWidget(self.pdf_logging, 4, 4, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pdf_outpu_file = QLineEdit(self.tab)
        self.pdf_outpu_file.setObjectName(u"pdf_outpu_file")

        self.horizontalLayout_18.addWidget(self.pdf_outpu_file)

        self.pdf_outpu_file_button = QPushButton(self.tab)
        self.pdf_outpu_file_button.setObjectName(u"pdf_outpu_file_button")
        self.pdf_outpu_file_button.setIcon(icon8)

        self.horizontalLayout_18.addWidget(self.pdf_outpu_file_button)


        self.gridLayout_8.addLayout(self.horizontalLayout_18, 1, 3, 3, 3)

        self.pdf_help_button = QPushButton(self.tab)
        self.pdf_help_button.setObjectName(u"pdf_help_button")
        self.pdf_help_button.setIcon(icon9)

        self.gridLayout_8.addWidget(self.pdf_help_button, 1, 7, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pdf_input_file = QLineEdit(self.tab)
        self.pdf_input_file.setObjectName(u"pdf_input_file")

        self.horizontalLayout_14.addWidget(self.pdf_input_file)

        self.pdf_input_file_button = QPushButton(self.tab)
        self.pdf_input_file_button.setObjectName(u"pdf_input_file_button")
        self.pdf_input_file_button.setIcon(icon8)

        self.horizontalLayout_14.addWidget(self.pdf_input_file_button)

        self.pdf_input_pages = QLineEdit(self.tab)
        self.pdf_input_pages.setObjectName(u"pdf_input_pages")

        self.horizontalLayout_14.addWidget(self.pdf_input_pages)


        self.gridLayout_8.addLayout(self.horizontalLayout_14, 1, 0, 3, 2)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pdf_encrypt_check = QCheckBox(self.tab)
        self.pdf_encrypt_check.setObjectName(u"pdf_encrypt_check")

        self.horizontalLayout_20.addWidget(self.pdf_encrypt_check)

        self.pdf_decrypt_check = QCheckBox(self.tab)
        self.pdf_decrypt_check.setObjectName(u"pdf_decrypt_check")

        self.horizontalLayout_20.addWidget(self.pdf_decrypt_check)

        self.pdf_password = QLineEdit(self.tab)
        self.pdf_password.setObjectName(u"pdf_password")

        self.horizontalLayout_20.addWidget(self.pdf_password)


        self.gridLayout_8.addLayout(self.horizontalLayout_20, 4, 2, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.pdf_additional_file = QLineEdit(self.tab)
        self.pdf_additional_file.setObjectName(u"pdf_additional_file")

        self.horizontalLayout_21.addWidget(self.pdf_additional_file)

        self.pdf_additional_file_button = QPushButton(self.tab)
        self.pdf_additional_file_button.setObjectName(u"pdf_additional_file_button")
        self.pdf_additional_file_button.setIcon(icon8)

        self.horizontalLayout_21.addWidget(self.pdf_additional_file_button)

        self.pdf_additional_pages = QLineEdit(self.tab)
        self.pdf_additional_pages.setObjectName(u"pdf_additional_pages")

        self.horizontalLayout_21.addWidget(self.pdf_additional_pages)


        self.gridLayout_8.addLayout(self.horizontalLayout_21, 4, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_17.addWidget(self.label_8)

        self.pdf_roation_degrees = QSpinBox(self.tab)
        self.pdf_roation_degrees.setObjectName(u"pdf_roation_degrees")
        self.pdf_roation_degrees.setMinimum(-360)
        self.pdf_roation_degrees.setMaximum(360)

        self.horizontalLayout_17.addWidget(self.pdf_roation_degrees)

        self.pdf_roation_pages = QLineEdit(self.tab)
        self.pdf_roation_pages.setObjectName(u"pdf_roation_pages")

        self.horizontalLayout_17.addWidget(self.pdf_roation_pages)


        self.gridLayout_8.addLayout(self.horizontalLayout_17, 1, 2, 3, 1)

        self.pdf_go_button = QPushButton(self.tab)
        self.pdf_go_button.setObjectName(u"pdf_go_button")
        self.pdf_go_button.setIcon(icon10)

        self.gridLayout_8.addWidget(self.pdf_go_button, 4, 7, 1, 1)

        self.tab_widget.addTab(self.tab, "")

        self.gridLayout_3.addWidget(self.tab_widget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 928, 22))
        self.menuScript = QMenu(self.menubar)
        self.menuScript.setObjectName(u"menuScript")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuScript.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuScript.addAction(self.action_script_tree_info)
        self.menuScript.addAction(self.action_script_clp)
        self.menuScript.addAction(self.action_script_backup)
        self.menuScript.addAction(self.action_script_alarm)
        self.menuScript.addAction(self.action_script_grep)
        self.menuScript.addAction(self.action_script_mcb)
        self.menuHelp.addAction(self.action_about)
        self.menuHelp.addAction(self.action_aboutQt)
        self.menuFile.addAction(self.action_quit)
        self.menuView.addAction(self.action_zoom_in)
        self.menuView.addAction(self.action_zoom_out)
        self.menuEdit.addAction(self.action_copy)
        self.menuEdit.addAction(self.action_clear)
        self.toolBar.addAction(self.action_quit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_copy)
        self.toolBar.addAction(self.action_clear)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_zoom_in)
        self.toolBar.addAction(self.action_zoom_out)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_about)
        self.toolBar.addAction(self.action_aboutQt)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        self.tab_widget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(tooltip)
        self.action_quit.setToolTip(QCoreApplication.translate("MainWindow", u"Quit", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.action_quit.setStatusTip(QCoreApplication.translate("MainWindow", u"Quit the program", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_quit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_script_tree_info.setText(QCoreApplication.translate("MainWindow", u"tree_info", None))
#if QT_CONFIG(tooltip)
        self.action_script_tree_info.setToolTip(QCoreApplication.translate("MainWindow", u"tree_info", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.action_script_tree_info.setStatusTip(QCoreApplication.translate("MainWindow", u"Show information about size, files and subfolders of selected folder", None))
#endif // QT_CONFIG(statustip)
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(tooltip)
        self.action_about.setToolTip(QCoreApplication.translate("MainWindow", u"About", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.action_about.setStatusTip(QCoreApplication.translate("MainWindow", u"Information about author and program", None))
#endif // QT_CONFIG(statustip)
        self.action_aboutQt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
#if QT_CONFIG(tooltip)
        self.action_aboutQt.setToolTip(QCoreApplication.translate("MainWindow", u"About Qt", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.action_aboutQt.setStatusTip(QCoreApplication.translate("MainWindow", u"Information about Qt version used", None))
#endif // QT_CONFIG(statustip)
        self.action_script_clp.setText(QCoreApplication.translate("MainWindow", u"clp", None))
#if QT_CONFIG(tooltip)
        self.action_script_clp.setToolTip(QCoreApplication.translate("MainWindow", u"clp", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.action_script_clp.setStatusTip(QCoreApplication.translate("MainWindow", u"Transform clipboard", None))
#endif // QT_CONFIG(statustip)
        self.action_zoom_in.setText(QCoreApplication.translate("MainWindow", u"Zoom in", None))
#if QT_CONFIG(statustip)
        self.action_zoom_in.setStatusTip(QCoreApplication.translate("MainWindow", u"Make the text larger", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_zoom_in.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl++", None))
#endif // QT_CONFIG(shortcut)
        self.action_zoom_out.setText(QCoreApplication.translate("MainWindow", u"Zoom out", None))
#if QT_CONFIG(statustip)
        self.action_zoom_out.setStatusTip(QCoreApplication.translate("MainWindow", u"Make the text smaller", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_zoom_out.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+-", None))
#endif // QT_CONFIG(shortcut)
        self.action_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
#if QT_CONFIG(statustip)
        self.action_clear.setStatusTip(QCoreApplication.translate("MainWindow", u"Clear all text from the output box", None))
#endif // QT_CONFIG(statustip)
        self.action_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
#if QT_CONFIG(statustip)
        self.action_copy.setStatusTip(QCoreApplication.translate("MainWindow", u"Copy selected text to clipboard", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_copy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.action_script_backup.setText(QCoreApplication.translate("MainWindow", u"backup_to_zip", None))
#if QT_CONFIG(statustip)
        self.action_script_backup.setStatusTip(QCoreApplication.translate("MainWindow", u"Backup a folder to a zip file, compressed or uncompressed.", None))
#endif // QT_CONFIG(statustip)
        self.action_script_alarm.setText(QCoreApplication.translate("MainWindow", u"alarm", None))
#if QT_CONFIG(statustip)
        self.action_script_alarm.setStatusTip(QCoreApplication.translate("MainWindow", u"Program an alarm with a message and sound", None))
#endif // QT_CONFIG(statustip)
        self.action_script_grep.setText(QCoreApplication.translate("MainWindow", u"grep", None))
#if QT_CONFIG(statustip)
        self.action_script_grep.setStatusTip(QCoreApplication.translate("MainWindow", u"Find a pattern within a group of files", None))
#endif // QT_CONFIG(statustip)
        self.action_script_mcb.setText(QCoreApplication.translate("MainWindow", u"mcb", None))
#if QT_CONFIG(statustip)
        self.action_script_mcb.setStatusTip(QCoreApplication.translate("MainWindow", u"Multiclipboard: puts text in clipboard, based on short key value", None))
#endif // QT_CONFIG(statustip)
        self.tree_info_path_button.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Depth:", None))
        self.tree_info_help_button.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.tree_info_path_text.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Path:", None))
        self.tree_info_go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_tree_info), QCoreApplication.translate("MainWindow", u"tree_info", None))
        self.clp_comas_dots_radio.setText(QCoreApplication.translate("MainWindow", u"comas-dots", None))
        self.clp_replace_regex_radio.setText(QCoreApplication.translate("MainWindow", u"replace-regex", None))
        self.clp_replace_regex_original.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Original text", None))
        self.clp_replace_regex_new.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Replacement text", None))
        self.clp_replace_radio.setText(QCoreApplication.translate("MainWindow", u"replace", None))
        self.clp_replace_original.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Original text", None))
        self.clp_replace_new.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Replacement text", None))
        self.clp_date_radio.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.clp_bullets_radio.setText(QCoreApplication.translate("MainWindow", u"bullets", None))
        self.clp_bullets_text.setText(QCoreApplication.translate("MainWindow", u"- ", None))
        self.clp_list_radio.setText(QCoreApplication.translate("MainWindow", u"list", None))
        self.clp_md_toc_radio.setText(QCoreApplication.translate("MainWindow", u"md-toc", None))
        self.clp_capitalize_radio.setText(QCoreApplication.translate("MainWindow", u"capitalize", None))
        self.clp_extract_radio.setText(QCoreApplication.translate("MainWindow", u"extract", None))
        self.clp_extract_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"regex pattern", None))
        self.clp_to_regex_radio.setText(QCoreApplication.translate("MainWindow", u"to-regex", None))
        self.clp_go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.clp_help_button.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_clp), QCoreApplication.translate("MainWindow", u"clp", None))
        self.backup_help_button.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.backup_go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.backup_compress_check.setText(QCoreApplication.translate("MainWindow", u"Compress", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Destination path", None))
        self.backup_destination.setText(QCoreApplication.translate("MainWindow", u"C:\\Cloud\\Backups", None))
        self.backup_destination_button.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Path to backup", None))
        self.backup_path_button.setText("")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_backup), QCoreApplication.translate("MainWindow", u"backup_to_zip", None))
        self.alarm_message.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Message to show", None))
        self.alarm_help_button.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.alarm_at_radio.setText(QCoreApplication.translate("MainWindow", u"At fixed time", None))
        self.alarm_go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.alarm_wait_radio.setText(QCoreApplication.translate("MainWindow", u"Wait", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_alarm), QCoreApplication.translate("MainWindow", u"alarm", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.grep_files.setPlaceholderText("")
        self.grep_folder_button.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Pattern", None))
        self.grep_go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.grep_help_button.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_grep), QCoreApplication.translate("MainWindow", u"grep", None))
        self.mcb_help_button.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.mcb_go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.mcb_del_radio.setText(QCoreApplication.translate("MainWindow", u"del", None))
        self.mcb_delete_kw.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter keyword", None))
        self.mcb_save_radio.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.mcb_save_kw.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter keyword", None))
        self.mcb_load_radio.setText(QCoreApplication.translate("MainWindow", u"load", None))
        self.mcb_load_kw.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter keyword", None))
        self.mcb_list_radio.setText(QCoreApplication.translate("MainWindow", u"list", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_mcb), QCoreApplication.translate("MainWindow", u"mcb", None))
        self.pdf_logging.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logging", None))
        self.pdf_outpu_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output file", None))
        self.pdf_outpu_file_button.setText("")
        self.pdf_help_button.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.pdf_input_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PDF file", None))
        self.pdf_input_file_button.setText("")
        self.pdf_input_pages.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pages", None))
        self.pdf_encrypt_check.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.pdf_decrypt_check.setText(QCoreApplication.translate("MainWindow", u"Dencrypt", None))
        self.pdf_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pdf_additional_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Additional PDF", None))
        self.pdf_additional_file_button.setText("")
        self.pdf_additional_pages.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pages", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.pdf_roation_pages.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pages", None))
        self.pdf_go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"pdf_pages", None))
#if QT_CONFIG(statustip)
        self.menuScript.setStatusTip(QCoreApplication.translate("MainWindow", u"Choose the script you want to run", None))
#endif // QT_CONFIG(statustip)
        self.menuScript.setTitle(QCoreApplication.translate("MainWindow", u"Script", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(statustip)
        self.menuFile.setStatusTip(QCoreApplication.translate("MainWindow", u"File options, like Quit the program", None))
#endif // QT_CONFIG(statustip)
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
#if QT_CONFIG(statustip)
        self.menuView.setStatusTip(QCoreApplication.translate("MainWindow", u"Zoom in and out", None))
#endif // QT_CONFIG(statustip)
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

