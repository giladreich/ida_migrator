from ida_migrator.migrator_dialog import *


class ExportDialog(MigratorDialog):

    def __init__(self, *args, **kwargs):
        super(ExportDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("Exporter")
        self._ui.lblTitle.setText(self._ui.lblTitle.text().replace('XXXX', 'export'))
        self._ui.btnStart.setText("Start Export")

    def populate_function_names(self):
        print('[IDA Migrator]: Loading functions...')

    def on_start_clicked(self):
        print('started export')
