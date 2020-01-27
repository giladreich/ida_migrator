from ida_migrator.migrator_dialog import *


class ImportDialog(MigratorDialog):

    def __init__(self, file_path, *args, **kwargs):
        self.file_path = file_path
        super(ImportDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("Importer")
        self._ui.lblTitle.setText(self._ui.lblTitle.text().replace('XXXX', 'import'))
        self._ui.btnStart.setText("Start Import")

    def populate_function_names(self):
        print('[IDA Migrator]: Loading functions...')

    def on_start_clicked(self):
        print('started import')
