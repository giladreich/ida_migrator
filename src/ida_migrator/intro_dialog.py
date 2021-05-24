import os
import json

import idc

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog

from ida_migrator import UI_DIR
from ida_migrator.utility import log_info
from ida_migrator.export_dialog import ExportDialog
from ida_migrator.import_dialog import ImportDialog


Ui_IntroDialog, IntroDialogBase = uic.loadUiType(
    os.path.join(UI_DIR, 'IntroDialog.ui')
)

class IntroDialog(IntroDialogBase):

    def __init__(self, *args, **kwargs):
        super(IntroDialog, self).__init__(*args, **kwargs)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        self._export_dialog = None
        self._import_dialog = None

        self._ui = Ui_IntroDialog()
        self._ui.setupUi(self)
        self._ui.btnExport.clicked.connect(self.on_export_clicked)
        self._ui.btnImport.clicked.connect(self.on_import_clicked)

    def on_export_clicked(self):
        self._export_dialog = ExportDialog(self)
        self._export_dialog.show()

    def on_import_clicked(self):
        dir_path = os.path.dirname(idc.get_idb_path())
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select File to Import',
                                                   dir_path, 'Dump file (*.json)')
        if not file_path:
            return

        self._import_dialog = ImportDialog(file_path, self)
        self._import_dialog.show()
