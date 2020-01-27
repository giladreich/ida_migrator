import os
import idaapi
from PyQt5.Qt import qApp
from PyQt5.QtCore import QObject
from ida_migrator.intro_dialog import IntroDialog


class IdaMigratorPlugin(QObject, idaapi.plugin_t):

    flags = idaapi.PLUGIN_FIX
    comment = "Migrating from one idb instance to another."
    help = "help"
    wanted_name = "IDA Migrator Plugin"
    wanted_hotkey = "Ctrl-Shift-D"

    def __init__(self, *args, **kwargs):
        print("[IDA Migrator]: Successfully loaded IDA Migrator plugin.")
        QObject.__init__(self, *args, **kwargs)
        idaapi.plugin_t.__init__(self)
        self._intro_dialog = None

    def init(self):
        if not idaapi.init_hexrays_plugin():
            return idaapi.PLUGIN_SKIP

        return idaapi.PLUGIN_KEEP

    def run(self, arg):
        self._intro_dialog = IntroDialog(qApp.activeWindow())
        self._intro_dialog.show()

    def term(self):
        print("[IDA Migrator]: term")
