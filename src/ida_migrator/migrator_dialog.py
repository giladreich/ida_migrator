import os

import idc
import idaapi
import idautils

from ida_migrator import UI_DIR

from PyQt5 import uic
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

Ui_MigratorDialog, MigratorDialogBase = uic.loadUiType(
    os.path.join(UI_DIR, 'MigratorDialog.ui')
)

POINTER_FMT = "0x{:016X}" if idaapi.get_inf_structure().is_64bit() else "0x{:08X}"

# Table columns
col_CheckBox = 0
col_Address  = 1
col_Name     = 2

# Search debounce/delay time
FILTER_DEBOUNCE_PERIOD = 500


class MigratorDialog(MigratorDialogBase):

    def __init__(self, *args, **kwargs):
        super(MigratorDialog, self).__init__(*args, **kwargs)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self._ui = Ui_MigratorDialog()
        self._ui.setupUi(self)

        self.filter_timer = QTimer()
        self.filter_timer.setSingleShot(True)
        self.filter_text = ""
        self.tblFunctions = self._ui.tblFunctions

        self.connect_slots()
        self.adjust_table_layout()
        self.populate_function_names()

    def connect_slots(self):
        self._ui.btnStart.clicked.connect(self.on_start_clicked)
        self._ui.tbxSearch.textChanged.connect(self.on_search_textchanged)
        self.filter_timer.timeout.connect(self.filter_items)

    def adjust_table_layout(self):
        checkbox_width = 22
        self.tblFunctions.setColumnWidth(col_CheckBox, checkbox_width)
        self.tblFunctions.horizontalHeader().setSectionResizeMode(col_CheckBox, QHeaderView.Fixed)
        self.tblFunctions.horizontalHeader().setStretchLastSection(True)
        # self.tblFunctions.setSelectionMode(QAbstractItemView.NoSelection)
        self.tblFunctions.setFocusPolicy(Qt.NoFocus)

    # virtual
    def populate_function_names(self):
        print("[IDA Migrator]: BASE - populate_function_names")

    def append_table_item(self, index, address, function):
        # cbx = QCheckBox(self)
        # cbx.setChecked(True)
        # cbx.setStyleSheet("margin-left:10%;")
        # self.tblFunctions.setCellWidget(index, col_CheckBox, cbx)
        cbx = QTableWidgetItem()
        cbx.setCheckState(Qt.Checked)
        cbx.setTextAlignment(Qt.AlignCenter)
        cbx.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable)
        self.tblFunctions.setItem(index, col_CheckBox, cbx)
        self.tblFunctions.setItem(index, col_Address, QTableWidgetItem(address))
        self.tblFunctions.setItem(index, col_Name, QTableWidgetItem(function))

    # virtual
    def on_start_clicked(self):
        print("[IDA Migrator]: BASE - on_start_clicked")

    def on_search_textchanged(self, text):
        self.filter_text = text
        self.filter_timer.start(FILTER_DEBOUNCE_PERIOD)

    # TODO(Gilad): Convert this to use Qt Model/View architecture (QAbstractItemView)
    def filter_items(self):
        filter = self.filter_text.lower()
        rowCount = self.tblFunctions.rowCount()
        colCount = self.tblFunctions.columnCount()
        for row in range(rowCount):
            match = False
            for col in range(1, colCount):
                item = self.tblFunctions.item(row, col)
                if item.text().lower().find(filter) != -1:
                    match = True
                    break
            self.tblFunctions.setRowHidden(row, not match)