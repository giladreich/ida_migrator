import os
import idaapi


class IdaMigratorPlugin(idaapi.plugin_t):

    flags = idaapi.PLUGIN_FIX
    comment = "Migrating from one idb instance to another."
    help = "help"
    wanted_name = "IDA Migrator Plugin"
    wanted_hotkey = "Ctrl-Shift-D"

    def __init__(self, *args, **kwargs):
        print("[IDA Migrator]: Successfully loaded IDA Migrator plugin.")
        idaapi.plugin_t.__init__(self)

    def init(self):
        if not idaapi.init_hexrays_plugin():
            return idaapi.PLUGIN_SKIP

        return idaapi.PLUGIN_KEEP

    def run(self, arg):
        print("[IDA Migrator]: run")

    def term(self):
        print("[IDA Migrator]: term")
