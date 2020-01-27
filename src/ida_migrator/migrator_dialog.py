import os

from ida_migrator import UI_DIR

from PyQt5 import uic
from PyQt5.QtCore import Qt


Ui_MigratorDialog, MigratorDialogBase = uic.loadUiType(
    os.path.join(UI_DIR, 'MigratorDialog.ui')
)

# Table columns
col_CheckBox = 0
col_Address  = 1
col_Name     = 2


class MigratorDialog(MigratorDialogBase):

    def __init__(self, *args, **kwargs):
        super(MigratorDialog, self).__init__(*args, **kwargs)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self._ui = Ui_MigratorDialog()
        self._ui.setupUi(self)

        self.tblFunctions = self._ui.tblFunctions

        self.connect_slots()
        self.adjust_table_layout()
        self.populate_function_names()

    def connect_slots(self):
        self._ui.btnStart.clicked.connect(self.on_start_clicked)

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

    # virtual
    def on_start_clicked(self):
        print("[IDA Migrator]: BASE - on_start_clicked")
