from ida_migrator.migrator_dialog import *


class ExportDialog(MigratorDialog):

    def __init__(self, *args, **kwargs):
        super(ExportDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("Exporter")
        self._ui.lblTitle.setText(self._ui.lblTitle.text().replace('XXXX', 'export'))
        self._ui.btnStart.setText("Start Export")

    def populate_function_names(self):
        print('[IDA Migrator]: Loading functions...')
        total = 0
        for seg in idautils.Segments():
            total += len(list(idautils.Functions(seg, idc.SegEnd(seg))))

        self.tblFunctions.setRowCount(total)
        index = 0
        for seg in idautils.Segments():
            for func in idautils.Functions(seg, idc.SegEnd(seg)):
                address = POINTER_FMT.format(func)
                function = idc.GetFunctionName(func)
                self.append_table_item(index, address, function)
                index += 1
        print('[IDA Migrator]: Finished loading functions.')



    def on_start_clicked(self):
        print('started export')
