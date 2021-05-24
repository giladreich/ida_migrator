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
            total += len(list(idautils.Functions(seg, idc.get_segm_end(seg))))

        self.tblFunctions.setRowCount(total)
        index = 0
        for seg in idautils.Segments():
            for func in idautils.Functions(seg, idc.get_segm_end(seg)):
                address = POINTER_FMT.format(func)
                function = idc.get_func_name(func)
                self.append_table_item(index, address, function)
                index += 1
        print('[IDA Migrator]: Finished loading functions.')

    def process_pe_info(self):
        info = idaapi.get_inf_structure()

        bits = 0xFF
        if info.is_64bit():
            bits = 64
        elif info.is_32bit():
            bits = 32

        data = {
            'exe': idc.get_root_filename(),
            'arch': "x{}_bit".format(bits),
            'file_type': idaapi.get_file_type_name(),
            'base_addr': POINTER_FMT.format(idaapi.get_imagebase()),
            'db_path': idaapi.get_input_file_path()
        }

        return data

    def process_functions(self):
        names = list()
        rowCount = self.tblFunctions.rowCount()
        count_added = 0
        for row in range(rowCount):
            cbx = self.tblFunctions.item(row, col_CheckBox)
            if not cbx or cbx.checkState() != Qt.Checked:
                continue

            name = {
                'address': self.tblFunctions.item(row, col_Address).text(),
                'name': self.tblFunctions.item(row, col_Name).text()
            }
            count_added += 1
            names.append(name)

        return names, count_added

    def on_start_clicked(self):
        file, ext = os.path.splitext(idc.get_idb_path())
        selected_dir = QFileDialog.getExistingDirectory(self, "Select Path to Export Files", os.path.dirname(file))
        if not selected_dir:
            return

        if os.name == 'nt':
            selected_dir = selected_dir.replace('/', '\\')

        file_name = os.path.basename(file)

        datetime = time.strftime("%Y%m%d-%H%M%S")
        file_json = "{}_symbols_{}.json".format(file_name, datetime)
        file_path_json = os.path.join(selected_dir, file_json)
        print("[IDA Migrator]: Exporting to {}".format(file_json))
        functions, count = self.process_functions()
        payload = {
            'bpe_info': self.process_pe_info(),
            'functions_count': count,
            'functions': functions
        }
        with open(file_path_json, "w") as f:
            json.dump(payload, f, indent=4, sort_keys=True)

        # NOTE(Gilad): Alternative Solution:
        # Call idc.process_ui_action('ProduceHeader') to produce C header file and then
        # on import idc.process_ui_action('LoadHeaderFile'). Only issue might be with parsing errors.
        # Parsing .IDC file is less error prone in this scenario.
        file_types = "{}_types_{}.idc".format(file_name, datetime)
        file_path_types = os.path.join(selected_dir, file_types)
        if not idc.gen_file(idc.OFILE_IDC, file_types, 0, idc.BADADDR, idc.GENFLG_IDCTYPE):
            QMessageBox.error(self, "FAILED", "Failed to generate type information file.")
        os.rename(file_types, file_path_types)

        QMessageBox.information(self, "SUCCESS",
                                """Successfully dumped files under:\n{}\n{}
                                \nWhich can now be used to import into another idb instance."""
                                .format(file_path_json, file_path_types))
