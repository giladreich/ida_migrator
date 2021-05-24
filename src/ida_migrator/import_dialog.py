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
        with open(self.file_path, "r") as f:
            parsed_json = json.loads(f.read())
            self.tblFunctions.setRowCount(parsed_json['functions_count'])
            index = 0
            for func in parsed_json['functions']:
                self.append_table_item(index, func['address'], func['name'])
                index += 1
        print('[IDA Migrator]: Finished loading functions.')

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

            idaapi.set_name(address, name.encode(), idaapi.SN_NOWARN)
            print("[IDA Migrator]: {} - Renamed {} to {}".format(address_str, curr_name, name))
            renamed_count += 1

        return renamed_count

    def on_start_clicked(self):
        count = self.rename_functions()
        print("[IDA Migrator]: {} functions has been renamed.".format(count))

        answer = QMessageBox.question(self, 'QUESTION',
                """Would you like to import type information as well? (structs, enums)
                \nYou'll need to provide the dumped IDC file.""",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if answer == QMessageBox.Yes:
            # idc.process_ui_action('Execute')
            dir_path = os.path.dirname(idc.get_idb_path())
            file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Import", dir_path, "IDC Script (*.idc)")
            if file_path:
                ida_expr.exec_idc_script(None, file_path.encode(), "main", None, 0)

        QMessageBox.information(self, "SUCCESS", "Successfully renamed {} functions.".format(count))
