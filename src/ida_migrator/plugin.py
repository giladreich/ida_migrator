import os

import idaapi

from PyQt5.Qt import qApp
from PyQt5.QtCore import QObject

from ida_migrator import VERSION, PLUGIN_NAME
from ida_migrator.utility import log_info
from ida_migrator.intro_dialog import IntroDialog


class IdaMigratorPlugin(QObject, idaapi.plugin_t):

    flags = idaapi.PLUGIN_FIX
    comment = "Migrating from one database instance to another."
    help = "help"
    wanted_name = PLUGIN_NAME
    wanted_hotkey = "Ctrl-Shift-D"

    def __init__(self, *args, **kwargs):
        QObject.__init__(self, *args, **kwargs)
        idaapi.plugin_t.__init__(self)
        self._intro_dialog = None

    def init(self):
        if not idaapi.init_hexrays_plugin():
            return idaapi.PLUGIN_SKIP

        log_info("Successfully loaded plugin - v{}", VERSION)
        return idaapi.PLUGIN_KEEP

    def run(self, arg):
        self._intro_dialog = IntroDialog(qApp.activeWindow())
        self._intro_dialog.show()

    def term(self):
        pass
