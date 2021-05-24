from ida_migrator import PLUGIN_NAME

# log_info("Message: {} - {}", "Hello", 123)
def log_info(fmt, *args):
    print("[{}]: {}".format(PLUGIN_NAME, fmt.format(*args)))
