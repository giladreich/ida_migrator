from ida_migrator.migrator_dialog import *
from ida_migrator.utility import log_info


class ImportDialog(MigratorDialog):

    def __init__(self, file_path, *args, **kwargs):
        self.file_path = file_path
        super(ImportDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("Importer")
        self._ui.lblTitle.setText(self._ui.lblTitle.text().replace('XXXX', 'import'))
        self._ui.btnStart.setText("Start Import")

    def populate_function_names(self):
        log_info('Loading functions...')
        with open(self.file_path, "r") as f:
            parsed_json = json.loads(f.read())
            self.tblFunctions.setRowCount(parsed_json['functions_count'])
            index = 0
            for func in parsed_json['functions']:
                self.append_table_item(index, func['address'], func['name'])
                index += 1
        log_info('Finished loading functions.')

    def rename_functions(self):
        row_count = self.tblFunctions.rowCount()
        renamed_count = 0
        for row in range(row_count):
            cbx = self.tblFunctions.item(row, col_CheckBox)
            if not cbx or cbx.checkState() != Qt.Checked:
                continue

            address_str = self.tblFunctions.item(row, col_Address).text()
            address = int(address_str, 16)
            name = self.tblFunctions.item(row, col_Name).text()
            curr_name = idc.get_func_name(address)
            if not name or not curr_name or name == curr_name:
                continue

            if idaapi.set_name(address, str(name), idaapi.SN_NOWARN):
                log_info("{} - Renamed {} to {}", address_str, curr_name, name)
                renamed_count += 1
            else:
                log_info("Failed renaming: {}. Disable SN_NOWARN to see why.", address_str)

        return renamed_count

    def on_start_clicked(self):
        count = self.rename_functions()
        log_info("{} functions has been renamed.", count)

        answer = QMessageBox.question(self, 'QUESTION',
                """Would you like to import type information as well? (structs, enums)
                \nYou'll need to provide the dumped IDC file.""",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if answer == QMessageBox.Yes:
            # idc.process_ui_action('Execute')
            dir_path = os.path.dirname(idc.get_idb_path())
            file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Import", dir_path, "IDC Script (*.idc)")
            if file_path:
                ida_expr.exec_idc_script(None, str(file_path), "main", None, 0)

        QMessageBox.information(self, "SUCCESS", "Successfully renamed {} functions.".format(count))
