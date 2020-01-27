import os

from PyQt5 import uic

from ida_migrator import UI_DIR


Ui_IntroDialog, IntroDialogBase = uic.loadUiType(
    os.path.join(UI_DIR, 'IntroDialog.ui')
)

class IntroDialog(IntroDialogBase):

    def __init__(self, *args, **kwargs):
        super(IntroDialog, self).__init__(*args, **kwargs)

        self._ui = Ui_IntroDialog()
        self._ui.setupUi(self)
        self._ui.btnExport.clicked.connect(self.on_export_clicked)
        self._ui.btnImport.clicked.connect(self.on_import_clicked)

    def on_export_clicked(self):
        print('export')

    def on_import_clicked(self):
        print('import')
    
