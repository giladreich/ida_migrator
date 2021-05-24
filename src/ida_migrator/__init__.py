import os

VERSION = '1.0.0'
PLUGIN_NAME = "IDA Migrator"
PLUGIN_DIR = os.path.dirname(os.path.realpath(__file__))
IDA_DIR = os.path.abspath(os.path.join(PLUGIN_DIR, '..', '..'))
UI_DIR = os.path.join(PLUGIN_DIR, 'ui')
