#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import os
from os import path
import sys
import urllib
from urllib import request
import webbrowser
import sqlite3

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "main.ui"))


class mainApp(QMainWindow, FORM_CLASS):

    def __init__(self, parent=None):
        super(mainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Button()

    def Handel_UI(self):
        self.setWindowTitle('Download Manegar')
        self.setFixedSize(540, 270)
        self.setWindowIcon(QIcon('icons/download.png'))

    def Handel_Button(self):
        self.pushButton.clicked.connect(self.Download)
        self.pushButton_2.clicked.connect(self.Handel_Browse)
        self.actionExiet.triggered.connect(self.close)
        self.action_FaceBook.triggered.connect(self.MyFaceBookProfile)
        self.action_Tiwetter.triggered.connect(self.MyTiwitterAcount)
        self.action_instagram.triggered.connect(self.MyInstagramAcount)
        self.action_Histroy.triggered.connect(self.Handel_table)

    def Handel_Browse(self):
        save_place = QFileDialog.getSaveFileName(self, caption='Save As', directory='.', filter=('All Files(*.*)'))
        text = str(save_place)
        name = (text[2:].split(',')[0].replace("'", ""))
        self.lineEdit_2.setText(name)

    def Handel_Progress(self, blockNum, blockSize, totalSize):
        r = blockNum * blockSize
        if totalSize > 0:
            p = r * 100 / totalSize
            self.progressBar.setValue(p)
            QApplication.processEvents()

    def Download(self):
        try:
            self.url = self.lineEdit.text()
            self.saveLocation = self.lineEdit_2.text()
            urllib.request.urlretrieve(self.url, self.saveLocation, self.Handel_Progress)

            try:
                self.db_connection(URL=self.url, SL=self.saveLocation, S='compeleted')
            except Exception as db_error:
                print(db_error)
                QMessageBox.warning(self, "Failed to add this procces to history", '{}'.format(db_error))

            QMessageBox.information(self, 'Download Completed', 'download completed')
            self.progressBar.setValue(0)
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')

        except Exception as download_error:
            print(download_error)
            QMessageBox.information(self, 'Erorr', 'download field')

            try:
                self.db_connection(URL=self.url, SL=self.saveLocation, S='Failed')

            except Exception as db_error_1:
                print(db_error_1)
                QMessageBox.warning(self, "Failed to add this procces to history", '{}'.format(db_error_1))

            self.progressBar.setValue(0)
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')

    def Handel_table(self):
        sql = "SELECT link, pass, stetus FROM history"
        self.con = sqlite3.connect('download.db')
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        self.get = self.cur.fetchall()
        self.con.close()

        self.table = QTableWidget()
        self.table.setGeometry(500, 200, 347, 368)
        self.table.setColumnCount(3)
        self.table.setStyleSheet("""QToolTip
{
    border: 0.1ex solid #eff0f1;
    background-color: #31363b;
    alternate-background-color: #3b4045;
    color: #eff0f1;
    padding: 0.5ex;
    opacity: 200;
}

QWidget
{
    color: #eff0f1;
    background-color: #31363b;
    selection-background-color:#3daee9;
    selection-color: #eff0f1;
    background-clip: border;
    border-image: none;
    border: 0px transparent black;
    outline: 0;
}

QWidget:item:hover
{
    background-color: #3daee9;
    color: #eff0f1;
}

QWidget:item:selected
{
    background-color: #3daee9;
}


QCheckBox
{
    spacing: 0.5ex;
    outline: none;
    color: #eff0f1;
    margin-bottom: 0.2ex;
    opacity: 200;
}

QCheckBox:disabled
{
    color: #76797c;
}

QGroupBox::indicator
{
    margin-left: 0.2ex;
}

QCheckBox::indicator:unchecked,
QCheckBox::indicator:unchecked:focus
{
    border-image: url(:/dark/checkbox_unchecked_disabled.svg);
}

QCheckBox::indicator:unchecked:hover,
QCheckBox::indicator:unchecked:pressed,
QGroupBox::indicator:unchecked:hover,
QGroupBox::indicator:unchecked:focus,
QGroupBox::indicator:unchecked:pressed
{
    border: none;
    border-image: url(:/dark/checkbox_unchecked.svg);
}

QCheckBox::indicator:checked
{
    border-image: url(:/dark/checkbox_checked.svg);
}

QCheckBox::indicator:checked:hover,
QCheckBox::indicator:checked:focus,
QCheckBox::indicator:checked:pressed,
QGroupBox::indicator:checked:hover,
QGroupBox::indicator:checked:focus,
QGroupBox::indicator:checked:pressed
{
    border: none;
    border-image: url(:/dark/checkbox_checked.svg);
}

QCheckBox::indicator:indeterminate
{
    border-image: url(:/dark/checkbox_indeterminate.svg);
}

QCheckBox::indicator:indeterminate:focus,
QCheckBox::indicator:indeterminate:hover,
QCheckBox::indicator:indeterminate:pressed
{
    border-image: url(:/dark/checkbox_indeterminate.svg);
}

QCheckBox::indicator:indeterminate:disabled
{
    border-image: url(:/dark/checkbox_indeterminate_disabled.svg);
}

QCheckBox::indicator:checked:disabled,
QGroupBox::indicator:checked:disabled
{
    border-image: url(:/dark/checkbox_checked_disabled.svg);
}

QCheckBox::indicator:unchecked:disabled,
QGroupBox::indicator:unchecked:disabled
{
    border-image: url(:/dark/checkbox_unchecked_disabled.svg);
}

QRadioButton
{
    spacing: 0.5ex;
    outline: none;
    color: #eff0f1;
    margin-bottom: 0.2ex;
}

QRadioButton:disabled
{
    color: #76797c;
}

QRadioButton::indicator:unchecked,
QRadioButton::indicator:unchecked:focus
{
    border-image: url(:/dark/radio_unchecked_disabled.svg);
}


QRadioButton::indicator:unchecked:hover,
QRadioButton::indicator:unchecked:pressed
{
    border: none;
    outline: none;
    border-image: url(:/dark/radio_unchecked.svg);
}


QRadioButton::indicator:checked
{
    border: none;
    outline: none;
    border-image: url(:/dark/radio_checked.svg);
}

QRadioButton::indicator:checked:hover,
QRadioButton::indicator:checked:focus,
QRadioButton::indicator:checked:pressed
{
    border: none;
    outline: none;
    border-image: url(:/dark/radio_checked.svg);
}

QRadioButton::indicator:checked:disabled
{
    outline: none;
    border-image: url(:/dark/radio_checked_disabled.svg);
}

QRadioButton::indicator:unchecked:disabled
{
    border-image: url(:/dark/radio_unchecked_disabled.svg);
}

QMenuBar
{
    background-color: #31363b;
    color: #eff0f1;
}

QMenuBar::item
{
    background: transparent;
}

QMenuBar::item:selected
{
    background: transparent;
    border: 0.1ex solid #76797c;
}

QMenuBar::item:pressed
{
    border: 0.1ex solid #76797c;
    background-color: #3daee9;
    color: #eff0f1;
    margin-bottom: -0.1ex;
    padding-bottom: 0.1ex;
}

QMenu
{
    border: 0.1ex solid #76797c;
    color: #eff0f1;
    margin: 0.2ex;
}

QMenu::icon
{
    margin: 0.5ex;
}

QMenu::item
{
    padding: 0.5ex 3ex 0.5ex 3ex;
    margin-left: 0.5ex;
    border: 0.1ex solid transparent; /* reserve space for selection border */
}

QMenu::item:selected
{
    color: #eff0f1;
}

QMenu::separator
{
    height: 0.2ex;
    background: lightblue;
    margin-left: 1ex;
    margin-right: 0.5ex;
}

/* non-exclusive indicator = check box style indicator
   (see QActionGroup::setExclusive) */
QMenu::indicator:non-exclusive:unchecked
{
    border-image: url(:/dark/checkbox_unchecked_disabled.svg);
}

QMenu::indicator:non-exclusive:unchecked:selected
{
    border-image: url(:/dark/checkbox_unchecked_disabled.svg);
}

QMenu::indicator:non-exclusive:checked
{
    border-image: url(:/dark/checkbox_checked.svg);
}

QMenu::indicator:non-exclusive:checked:selected
{
    border-image: url(:/dark/checkbox_checked.svg);
}

/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */
QMenu::indicator:exclusive:unchecked
{
    border-image: url(:/dark/radio_unchecked_disabled.svg);
}

QMenu::indicator:exclusive:unchecked:selected
{
    border-image: url(:/dark/radio_unchecked_disabled.svg);
}

QMenu::indicator:exclusive:checked
{
    border-image: url(:/dark/radio_checked.svg);
}

QMenu::indicator:exclusive:checked:selected
{
    border-image: url(:/dark/radio_checked.svg);
}

QMenu::right-arrow
{
    margin: 0.5ex;
    border-image: url(:/light/right_arrow.svg);
    width: 0.6ex;
    height: 0.9ex;
}


QWidget:disabled
{
    color: #454545;
    background-color: #31363b;
}

QAbstractItemView
{
    alternate-background-color: #31363b;
    color: #eff0f1;
    border: 0.1ex solid 3A3939;
    border-radius: 0.2ex;
}

QWidget:focus,
QMenuBar:focus
{
    border: 0.1ex solid #3daee9;
}

QTabWidget:focus,
QCheckBox:focus,
QRadioButton:focus,
QSlider:focus
{
    border: none;
}

QLineEdit
{
    background-color: #232629;
    padding: 0.5ex;
    border-style: solid;
    border: 0.1ex solid #76797c;
    border-radius: 0.2ex;
    color: #eff0f1;
}

QGroupBox
{
    border: 0.1ex solid #76797c;
    border-radius: 0.2ex;
    padding-top: 1ex;
    margin-top: 1ex;
}

QGroupBox::title
{
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding-left: 0.1ex;
    padding-right: 0.1ex;
    margin-top: -0.7ex;
}

QAbstractScrollArea
{
    border-radius: 0.2ex;
    border: 0.1ex solid #76797c;
    background-color: transparent;
}

QScrollBar:horizontal
{
    height: 1.5ex;
    margin: 0.3ex 1.5ex 0.3ex 1.5ex;
    border: 0.1ex transparent #2A2929;
    border-radius: 0.4ex;
    background-color: #2A2929;
}

QScrollBar::handle:horizontal
{
    background-color: #3daee9;
    min-width: 0.5ex;
    border-radius: 0.4ex;
}

QScrollBar::add-line:horizontal
{
    margin: 0px 0.3ex 0px 0.3ex;
    border-image: url(:/dark/right_arrow_disabled.svg);
    width: 1ex;
    height: 1ex;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal
{
    margin: 0ex 0.3ex 0ex 0.3ex;
    border-image: url(:/dark/left_arrow_disabled.svg);
    width: 1ex;
    height: 1ex;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal:hover,
QScrollBar::add-line:horizontal:on
{
    border-image: url(:/dark/right_arrow.svg);
    width: 1ex;
    height: 1ex;
    subcontrol-position: right;
    subcontrol-origin: margin;
}


QScrollBar::sub-line:horizontal:hover,
QScrollBar::sub-line:horizontal:on
{
    border-image: url(:/dark/left_arrow.svg);
    width: 1ex;
    height: 1ex;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:horizontal,
QScrollBar::down-arrow:horizontal
{
    background: none;
}


QScrollBar::add-page:horizontal,
QScrollBar::sub-page:horizontal
{
    background: none;
}

QScrollBar:vertical
{
    background-color: #2A2929;
    width: 1.5ex;
    margin: 1.5ex 0.3ex 1.5ex 0.3ex;
    border: 0.1ex transparent #2A2929;
    border-radius: 0.4ex;
}

QScrollBar::handle:vertical
{
    background-color: #3daee9;
    min-height: 0.5ex;
    border-radius: 0.4ex;
}

QScrollBar::sub-line:vertical
{
    margin: 0.3ex 0ex 0.3ex 0ex;
    border-image: url(:/dark/up_arrow_disabled.svg);
    height: 1ex;
    width: 1ex;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical
{
    margin: 0.3ex 0ex 0.3ex 0ex;
    border-image: url(:/dark/down_arrow_disabled.svg);
    height: 1ex;
    width: 1ex;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical:hover,
QScrollBar::sub-line:vertical:on
{

    border-image: url(:/dark/up_arrow.svg);
    height: 1ex;
    width: 1ex;
    subcontrol-position: top;
    subcontrol-origin: margin;
}


QScrollBar::add-line:vertical:hover,
QScrollBar::add-line:vertical:on
{
    border-image: url(:/dark/down_arrow.svg);
    height: 1ex;
    width: 1ex;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
{
    background: none;
}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
    background: none;
}

QTextEdit
{
    background-color: #232629;
    color: #eff0f1;
    border: 0.1ex solid #76797c;
}

QPlainTextEdit
{
    background-color: #232629;;
    color: #eff0f1;
    border-radius: 0.2ex;
    border: 0.1ex solid #76797c;
}

QHeaderView::section
{
    background-color: #76797c;
    color: #eff0f1;
    padding: 0.5ex;
    border: 0.1ex solid #76797c;
}

QSizeGrip
{
    border-image: url(:/dark/sizegrip.svg);
    width: 1.2ex;
    height: 1.2ex;
}

QMainWindow::separator
{
    background-color: #31363b;
    color: white;
    padding-left: 0.4ex;
    spacing: 0.2ex;
    border: 0.1ex dashed #76797c;
}

QMainWindow::separator:hover
{

    background-color: #787876;
    color: white;
    padding-left: 0.4ex;
    border: 0.1ex solid #76797c;
    spacing: 0.2ex;
}

QMenu::separator
{
    height: 0.1ex;
    background-color: #76797c;
    color: white;
    padding-left: 0.4ex;
    margin-left: 1ex;
    margin-right: 0.5ex;
}

QFrame[frameShape="2"],  /* QFrame::Panel == 0x0003 */
QFrame[frameShape="3"],  /* QFrame::WinPanel == 0x0003 */
QFrame[frameShape="4"],  /* QFrame::HLine == 0x0004 */
QFrame[frameShape="5"],  /* QFrame::VLine == 0x0005 */
QFrame[frameShape="6"]  /* QFrame::StyledPanel == 0x0006 */
{
    border-width: 0.1ex;
    padding: 0.1ex;
    border-style: solid;
    border-color: #31363b;
    background-color: #76797c;
    border-radius: 0.5ex;
}

QStackedWidget
{
    border: 0.1ex transparent black;
}

QToolBar
{
    border: 0.1ex transparent #393838;
    background: 0.1ex solid #31363b;
    font-weight: bold;
}

QToolBar::handle:horizontal
{
    border-image: url(:/dark/hmovetoolbar.svg);
    width = 1.6ex;
    height = 6.4ex;
}

QToolBar::handle:vertical
{
    border-image: url(:/dark/vmovetoolbar.svg);
    width = 5.4ex;
    height = 1ex;
}

QToolBar::separator:horizontal
{
    border-image: url(:/dark/hsepartoolbar.svg);
    width = 0.7ex;
    height = 6.3ex;
}

QToolBar::separator:vertical
{
    border-image: url(:/dark/vsepartoolbars.svg);
    width = 6.3ex;
    height = 0.7ex;
}

QPushButton
{
    color: #eff0f1;
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #3b4045, stop: 0.5 #31363b);
    border-width: 0.1ex;
    border-color: #76797c;
    border-style: solid;
    padding: 0.5ex;
    border-radius: 0.2ex;
    outline: none;
}

QPushButton:disabled
{
    background-color: #31363b;
    border-width: 0.1ex;
    border-color: #454545;
    border-style: solid;
    padding-top: 0.5ex;
    padding-bottom: 0.5ex;
    padding-left: 1ex;
    padding-right: 1ex;
    border-radius: 0.2ex;
    color: #454545;
}

QPushButton:focus
{
    color: white;
}

QPushButton:pressed
{
    background-color: #31363b;
    padding-top: -1.5ex;
    padding-bottom: -1.7ex;
}

QComboBox
{
    selection-background-color: #3daee9;
    border-style: solid;
    border: 0.1ex solid #76797c;
    border-radius: 0.2ex;
    padding: 0.5ex;
    min-width: 7.5ex;
}

QPushButton:checked
{
    background-color: #76797c;
    border-color: #6A6969;
}

QPushButton:hover
{
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #454a4f, stop: 0.5 #3b4045);
    border: 0.1ex solid #3daee9;
    color: #eff0f1;
}

QPushButton:checked:hover
{
    background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #808386, stop: 0.5 #76797c);
    border: 0.1ex solid #3daee9;
    color: #eff0f1;
}

QComboBox:hover,
QAbstractSpinBox:hover,
QLineEdit:hover,
QTextEdit:hover,
QPlainTextEdit:hover,
QAbstractView:hover,
QTreeView:hover
{
    border: 0.1ex solid #3daee9;
    color: #eff0f1;
}

QComboBox:hover:pressed,
QPushButton:hover:pressed,
QAbstractSpinBox:hover:pressed,
QLineEdit:hover:pressed,
QTextEdit:hover:pressed,
QPlainTextEdit:hover:pressed,
QAbstractView:hover:pressed,
QTreeView:hover:pressed
{
    background-color: #31363b;
}

QComboBox:on
{
    padding-top: 0.3ex;
    padding-left: 0.4ex;
    selection-background-color: #4a4a4a;
}

QComboBox QAbstractItemView
{
    background-color: #232629;
    border-radius: 0.2ex;
    border: 0.1ex solid #76797c;
    selection-background-color: #3daee9;
}

QComboBox::drop-down
{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 1.5ex;

    border-left-width: 0ex;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: 0.3ex;
    border-bottom-right-radius: 0.3ex;
}

QComboBox::down-arrow
{
    border-image: url(:/dark/down_arrow_disabled.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QComboBox::down-arrow:on,
QComboBox::down-arrow:hover,
QComboBox::down-arrow:focus
{
    border-image: url(:/dark/down_arrow.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QAbstractSpinBox
{
    padding: 0.5ex;
    border: 0.1ex solid #76797c;
    background-color: #232629;
    color: #eff0f1;
    border-radius: 0.2ex;
    min-width: 7.5ex;
}

QAbstractSpinBox:up-button
{
    background-color: transparent;
    subcontrol-origin: border;
    subcontrol-position: center right;
}

QAbstractSpinBox:down-button
{
    background-color: transparent;
    subcontrol-origin: border;
    subcontrol-position: center left;
}

QAbstractSpinBox::up-arrow,
QAbstractSpinBox::up-arrow:disabled,
QAbstractSpinBox::up-arrow:off
{
    border-image: url(:/dark/up_arrow_disabled.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QAbstractSpinBox::up-arrow:hover
{
    border-image: url(:/dark/up_arrow.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QAbstractSpinBox::down-arrow,
QAbstractSpinBox::down-arrow:disabled,
QAbstractSpinBox::down-arrow:off
{
    border-image: url(:/dark/down_arrow_disabled.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QAbstractSpinBox::down-arrow:hover
{
    border-image: url(:/dark/down_arrow.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QLabel
{
    border: 0ex solid black;
}

/* BORDERS */
QTabWidget::pane
{
    padding: 0.5ex;
    margin: 0.1ex;
}

QTabWidget::pane:top
{
    border: 0.1ex solid #76797c;
    top: -0.1ex;
}

QTabWidget::pane:bottom
{
    border: 0.1ex solid #76797c;
    bottom: -0.1ex;
}

QTabWidget::pane:left
{
    border: 0.1ex solid #76797c;
    right: -0.1ex;
}

QTabWidget::pane:right
{
    border: 0.1ex solid #76797c;
    left: -0.1ex;
}


QTabBar
{
    qproperty-drawBase: 0;
    left: 0.5ex; /* move to the right by 0.5ex */
    border-radius: 0.3ex;
}

QTabBar:focus
{
    border: 0ex transparent black;
}

QTabBar::close-button
{
    border-image: url(:/dark/close.svg);
    background: transparent;
}

QTabBar::close-button:hover
{
    border-image: url(:/dark/close-hover.svg);
    width: 1.2ex;
    height: 1.2ex;
    background: transparent;
}

QTabBar::close-button:pressed
{
    border-image: url(:/dark/close-pressed.svg);
    width: 1.2ex;
    height: 1.2ex;
    background: transparent;
}

/* TOP TABS */
QTabBar::tab:top
{
    color: #eff0f1;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #76797c;
    border-top: 0.1ex solid #76797c;
    background-color: #31363b;
    padding: 0.5ex;
    min-width: 50px;
    border-top-left-radius: 0.2ex;
    border-top-right-radius: 0.2ex;
}

QTabBar::tab:top:last,
QTabBar::tab:top:only-one
{
    color: #eff0f1;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #76797c;
    border-right: 0.1ex solid #76797c;
    border-top: 0.1ex solid #76797c;
    background-color: #31363b;
    padding: 0.5ex;
    min-width: 50px;
    border-top-left-radius: 0.2ex;
    border-top-right-radius: 0.2ex;
}

QTabBar::tab:top:!selected
{
    color: #eff0f1;
    background-color: #54575B;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #76797c;
    border-top-left-radius: 0.2ex;
    border-top-right-radius: 0.2ex;
}

QTabBar::tab:top:first:!selected
{
    color: #eff0f1;
    background-color: #54575B;
    border: 0.1ex transparent black;
    border-top-left-radius: 0.2ex;
    border-top-right-radius: 0.2ex;
}

QTabBar::tab:top:!selected:hover
{
    background-color: rgba(61, 173, 232, 0.2);
    border: 0.1ex rgba(61, 173, 232, 0.2);
    border-left: 0.1ex solid #76797c;
}

QTabBar::tab:top:!selected:first:hover
{
    background-color: rgba(61, 173, 232, 0.2);
    border: 0.1ex rgba(61, 173, 232, 0.2);
}

/* BOTTOM TABS */

QTabBar::tab:bottom
{
    color: #eff0f1;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #76797c;
    border-bottom: 0.1ex solid #76797c;
    background-color: #31363b;
    padding: 0.5ex;
    border-bottom-left-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
    min-width: 50px;
}

QTabBar::tab:bottom:last,
QTabBar::tab:bottom:only-one
{
    color: #eff0f1;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #76797c;
    border-right: 0.1ex solid #76797c;
    border-bottom: 0.1ex solid #76797c;
    background-color: #31363b;
    padding: 0.5ex;
    border-bottom-left-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
    min-width: 50px;
}

QTabBar::tab:bottom:!selected
{
    color: #eff0f1;
    background-color: #54575B;
    border: 0.1ex transparent black;
    border-left: 0.1ex solid #76797c;
    border-bottom-left-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
}

QTabBar::tab:bottom:first:!selected
{
    color: #eff0f1;
    background-color: #54575B;
    border: 0.1ex transparent black;
    border-top-left-radius: 0.2ex;
    border-top-right-radius: 0.2ex;
}

QTabBar::tab:bottom:!selected:hover
{
    background-color: rgba(61, 173, 232, 0.2);
    border: 0.1ex rgba(61, 173, 232, 0.2);
    border-left: 0.1ex solid #76797c;
}

QTabBar::tab:bottom:!selected:first:hover
{
    background-color: rgba(61, 173, 232, 0.2);
    border: 0.1ex rgba(61, 173, 232, 0.2);
}

/* LEFT TABS */
QTabBar::tab:left
{
    color: #eff0f1;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #76797c;
    border-right: 0.1ex solid #76797c;
    background-color: #31363b;
    padding: 0.5ex;
    border-top-right-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
    min-height: 50px;
}

QTabBar::tab:left:last,
QTabBar::tab:left:only-one
{
    color: #eff0f1;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #76797c;
    border-bottom: 0.1ex solid #76797c;
    border-right: 0.1ex solid #76797c;
    background-color: #31363b;
    padding: 0.5ex;
    border-top-right-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
    min-height: 50px;
}

QTabBar::tab:left:!selected
{
    color: #eff0f1;
    background-color: #54575B;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #76797c;
    border-top-right-radius: 0.2ex;
    border-bottom-right-radius: 0.2ex;
}

QTabBar::tab:left:!selected:hover
{
    background-color: rgba(61, 173, 232, 0.2);
    border: 0.1ex rgba(61, 173, 232, 0.2);
    border-top: 0.1ex solid #76797c;
}

QTabBar::tab:left:!selected:first:hover
{
    background-color: rgba(61, 173, 232, 0.2);
    border: 0.1ex rgba(61, 173, 232, 0.2);
}

/* RIGHT TABS */
QTabBar::tab:right
{
    color: #eff0f1;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #76797c;
    border-left: 0.1ex solid #76797c;
    background-color: #31363b;
    padding: 0.5ex;
    border-top-left-radius: 0.2ex;
    border-bottom-left-radius: 0.2ex;
    min-height: 50px;
}

QTabBar::tab:right:last,
QTabBar::tab:right:only-one
{
    color: #eff0f1;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #76797c;
    border-bottom: 0.1ex solid #76797c;
    border-left: 0.1ex solid #76797c;
    background-color: #31363b;
    padding: 0.5ex;
    border-top-left-radius: 0.2ex;
    border-bottom-left-radius: 0.2ex;
    min-height: 50px;
}

QTabBar::tab:right:!selected
{
    color: #eff0f1;
    background-color: #54575B;
    border: 0.1ex transparent black;
    border-top: 0.1ex solid #76797c;
    border-top-left-radius: 0.2ex;
    border-bottom-left-radius: 0.2ex;
}

QTabBar::tab:right:!selected:hover
{
    background-color: rgba(61, 173, 232, 0.2);
    border: 0.1ex rgba(61, 173, 232, 0.2);
    border-top: 0.1ex solid #76797c;
}

QTabBar::tab:right:!selected:first:hover
{
    background-color: rgba(61, 173, 232, 0.2);
    border: 0.1ex rgba(61, 173, 232, 0.2);
}

QTabBar QToolButton::right-arrow:enabled
{
    border-image: url(:/dark/right_arrow.svg);
}

QTabBar QToolButton::left-arrow:enabled
{
    border-image: url(:/dark/left_arrow.svg);
}

QTabBar QToolButton::right-arrow:disabled
{
    border-image: url(:/dark/right_arrow_disabled.svg);
}

QTabBar QToolButton::left-arrow:disabled
{
    border-image: url(:/dark/left_arrow_disabled.svg);
}

QDockWidget
{
    background: #31363b;
    border: 0.1ex solid #403F3F;
    titlebar-close-icon: url(:/dark/transparent.svg);
    titlebar-normal-icon: url(:/dark/transparent.svg);
}

QDockWidget::close-button,
QDockWidget::float-button
{
    border: 0.1ex solid transparent;
    border-radius: 0.2ex;
    background: transparent;
}

QDockWidget::float-button
{
    border-image: url(:/dark/undock.svg);
}

QDockWidget::float-button:hover
{
    border-image: url(:/dark/undock-hover.svg) ;
}

QDockWidget::close-button
{
    border-image: url(:/dark/close.svg) ;
}

QDockWidget::close-button:hover
{
    border-image: url(:/dark/close-hover.svg) ;
}

QDockWidget::close-button:pressed
{
    border-image: url(:/dark/close-pressed.svg) ;
}

QTreeView,
QListView
{
    border: 0.1ex solid #76797c;
    background-color: #232629;
}

QTreeView::branch:has-siblings:!adjoins-item
{
    border-image: url(:/dark/stylesheet-vline.svg) 0;
}

QTreeView::branch:has-siblings:adjoins-item
{
    border-image: url(:/dark/stylesheet-branch-more.svg) 0;
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item
{
    border-image: url(:/dark/stylesheet-branch-end.svg) 0;
}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings
{
    border-image: url(:/dark/stylesheet-branch-end-closed.svg) 0;
    image: url(:/dark/branch_closed.svg);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings
{
    border-image: url(:/dark/stylesheet-branch-end-open.svg) 0;
    image: url(:/dark/branch_open.svg);
}

/*
QTreeView::branch:has-siblings:!adjoins-item {
        background: cyan;
}

QTreeView::branch:has-siblings:adjoins-item {
        background: red;
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {
        background: blue;
}

QTreeView::branch:closed:has-children:has-siblings {
        background: pink;
}

QTreeView::branch:has-children:!has-siblings:closed {
        background: gray;
}

QTreeView::branch:open:has-children:has-siblings {
        background: magenta;
}

QTreeView::branch:open:has-children:!has-siblings {
        background: green;
}
*/

QTableView::item,
QListView::item,
QTreeView::item
{
    padding: 0.3ex;
}

QTableView::item:!selected:hover,
QListView::item:!selected:hover,
QTreeView::item:!selected:hover
{
    background-color: rgba(61, 173, 232, 0.2);
    outline: 0;
    color: #eff0f1;
    padding: 0.3ex;
}


QSlider::groove:horizontal
{
    border: 0.1ex solid #31363b;
    height: 0.4ex;
    background: #565a5e;
    margin: 0ex;
    border-radius: 0.2ex;
}

QSlider::handle:horizontal
{
    background: #232629;
    border: 0.1ex solid #626568;
    width: 1.6ex;
    height: 1.6ex;
    margin: -0.8ex 0;
    border-radius: 0.9ex;
}

QSlider::groove:vertical
{
    border: 0.1ex solid #31363b;
    width: 0.4ex;
    background: #565a5e;
    margin: 0ex;
    border-radius: 0.3ex;
}

QSlider::handle:vertical
{
    background: #232629;
    border: 0.1ex solid #626568;
    width: 1.6ex;
    height: 1.6ex;
    margin: 0 -0.8ex;
    border-radius: 0.9ex;
}

QSlider::handle:horizontal:hover,
QSlider::handle:horizontal:focus,
QSlider::handle:vertical:hover,
QSlider::handle:vertical:focus
{
    border: 0.1ex solid #3daee9;
}

QSlider::sub-page:horizontal,
QSlider::add-page:vertical
{
    background: #3daee9;
    border-radius: 0.3ex;
}

QSlider::add-page:horizontal,
QSlider::sub-page:vertical
{
    background: #626568;
    border-radius: 0.3ex;
}

QToolButton
{
    background-color: transparent;
    border: 0.1ex solid #76797c;
    border-radius: 0.2ex;
    margin: 0.3ex;
    padding: 0.5ex;
}

QToolButton[popupMode="1"]  /* only for MenuButtonPopup */
{
    padding-right: 2ex; /* make way for the popup button */
}

QToolButton[popupMode="2"]  /* only for InstantPopup */
{
    padding-right: 1ex; /* make way for the popup button */
}

QToolButton::menu-indicator
{
    border-image: none;
    image: url(:/dark/down_arrow.svg);
    top: -0.7ex;
    left: -0.2ex;
}

QToolButton::menu-arrow
{
    border-image: none;
    image: url(:/dark/down_arrow.svg);
}

QToolButton:hover,
QToolButton::menu-button:hover
{
    background-color: transparent;
    border: 0.1ex solid #3daee9;
}

QToolButton:checked,
QToolButton:pressed,
QToolButton::menu-button:pressed
{
    background-color: #3daee9;
    border: 0.1ex solid #3daee9;
    padding: 0.5ex;
}

QToolButton::menu-button
{
    border: 0.1ex solid #76797c;
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
    /* 1ex width + 0.4ex for border + no text = 2ex allocated above */
    width: 1ex;
    padding: 0.5ex;
    outline: none;
}

QToolButton::menu-arrow:open
{
    border: 0.1ex solid #76797c;
}

QPushButton::menu-indicator
{
    subcontrol-origin: padding;
    subcontrol-position: bottom right;
    left: 0.8ex;
}

QTableView
{
    border: 0.1ex solid #76797c;
    gridline-color: #31363b;
    background-color: #232629;
}


QTableView,
QHeaderView
{
    border-radius: 0px;
}

QTableView::item:pressed,
QListView::item:pressed,
QTreeView::item:pressed
{
    background: #3daee9;
    color: #eff0f1;
}

QTableView::item:selected:active,
QTreeView::item:selected:active,
QListView::item:selected:active
{
    background: #3daee9;
    color: #eff0f1;
}

QListView::item:selected:hover,
QTreeView::item:selected:hover
{
    background-color: #47b8f3;
    color: #eff0f1;
}

QHeaderView
{
    background-color: #31363b;
    border: 0.1ex transparent;
    border-radius: 0px;
    margin: 0px;
    padding: 0px;

}

QHeaderView::section
{
    background-color: #31363b;
    color: #eff0f1;
    padding: 0.5ex;
    border: 0.1ex solid #76797c;
    border-radius: 0px;
    text-align: center;
}

QHeaderView::section::vertical::first,
QHeaderView::section::vertical::only-one
{
    border-top: 0.1ex solid #76797c;
}

QHeaderView::section::vertical
{
    border-top: transparent;
}

QHeaderView::section::horizontal::first,
QHeaderView::section::horizontal::only-one
{
    border-left: 0.1ex solid #76797c;
}

QHeaderView::section::horizontal
{
    border-left: transparent;
}


QHeaderView::section:checked
{
    color: white;
    background-color: #334e5e;
}

 /* style the sort indicator */
QHeaderView::down-arrow
{
    image: url(:/dark/down_arrow.svg);
}

QHeaderView::up-arrow
{
    image: url(:/dark/up_arrow.svg);
}

QTableCornerButton::section
{
    background-color: #31363b;
    border: 0.1ex transparent #76797c;
    border-radius: 0px;
}

QToolBox
{
    padding: 0.5ex;
    border: 0.1ex transparent black;
}

QToolBox:selected
{
    background-color: #31363b;
    border-color: #3daee9;
}

QToolBox:hover
{
    border-color: #3daee9;
}

QStatusBar::item
{
    border: 0px transparent dark;
}

QFrame[height="3"],
QFrame[width="3"]
{
    background-color: #76797c;
}

QSplitter::handle
{
    border: 0.1ex dashed #76797c;
}

QSplitter::handle:hover
{
    background-color: #787876;
    border: 0.1ex solid #76797c;
}

QSplitter::handle:horizontal
{
    width: 0.1ex;
}

QSplitter::handle:vertical
{
    height: 0.1ex;
}

QProgressBar:horizontal
{
    background-color: #626568;
    border: 0.1ex solid #31363b;
    border-radius: 0.3ex;
    height: 0.5ex;
    text-align: right;
    margin-top: 0.5ex;
    margin-bottom: 0.5ex;
    margin-right: 5ex;
    padding: 0px;
}

QProgressBar::chunk:horizontal
{
    background-color: #3daee9;
    border: 0.1ex transparent;
    border-radius: 0.3ex;
}

QSpinBox,
QDoubleSpinBox
{
    padding-right: 1.5ex;
}

QSpinBox::up-button,
QDoubleSpinBox::up-button
{
    subcontrol-origin: content;
    subcontrol-position: right top;

    width: 1.6ex;
    border-width: 0.1ex;
}

QSpinBox::up-arrow,
QDoubleSpinBox::up-arrow
{
    border-image: url(:/dark/up_arrow.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QSpinBox::up-arrow:hover,
QSpinBox::up-arrow:pressed,
QDoubleSpinBox::up-arrow:hover,
QDoubleSpinBox::up-arrow:pressed
{
    border-image: url(:/dark/up_arrow-hover.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QSpinBox::up-arrow:disabled,
QSpinBox::up-arrow:off,
QDoubleSpinBox::up-arrow:disabled,
QDoubleSpinBox::up-arrow:off
{
   border-image: url(:/dark/up_arrow_disabled.svg);
}

QSpinBox::down-button,
QDoubleSpinBox::down-button
{
    subcontrol-origin: content;
    subcontrol-position: right bottom;

    width: 1.6ex;
    border-width: 0.1ex;
}

QSpinBox::down-arrow,
QDoubleSpinBox::down-arrow
{
    border-image: url(:/dark/down_arrow.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QSpinBox::down-arrow:hover,
QSpinBox::down-arrow:pressed,
QDoubleSpinBox::down-arrow:hover,
QDoubleSpinBox::down-arrow:pressed
{
    border-image: url(:/dark/down_arrow-hover.svg);
    width: 0.9ex;
    height: 0.6ex;
}

QSpinBox::down-arrow:disabled,
QSpinBox::down-arrow:off,
QDoubleSpinBox::down-arrow:disabled,
QDoubleSpinBox::down-arrow:off
{
   border-image: url(:/dark/down_arrow_disabled.svg);
}""")
        self.table.setWindowTitle("Histoy")
        self.table.setWindowIcon(QIcon("icons/history.png"))

        self.table.setAlternatingRowColors(True)
        for row_Num, row_Data in enumerate(self.get):
            self.table.insertRow(row_Num)
            for cul_Num, data in enumerate(row_Data):
                self.table.setItem(row_Num, cul_Num, QTableWidgetItem(str(data)))
        self.table.show()

    def db_connection(self, URL, SL, S):
        self.con = sqlite3.connect('download.db')
        self.cur = self.con.cursor()
        self.cur.execute(
            "INSERT INTO history ('link', 'pass', 'stetus') VALUES ('{}', '{}', '{}'); ".format(URL, SL, S))
        self.con.commit()
        print('d')
        self.con.close()

    def Handel_Exit(self):
        self.window.close()

    def MyFaceBookProfile(self):
        webbrowser.open('https://www.facebook.com/marwanmo7amed8', new=2)

    def MyTiwitterAcount(self):
        webbrowser.open('https://twitter.com/Marwan_Mo7amed_', new=2)

    def MyInstagramAcount(self):
        webbrowser.open('https://www.instagram.com/marwan_mohamed_0_0', new=2)


def main():
    app = QApplication(sys.argv)
    window = mainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
