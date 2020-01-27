from ida_migrator.plugin import IdaMigratorPlugin

def PLUGIN_ENTRY(*args, **kwargs):
    return IdaMigratorPlugin(*args, **kwargs)
