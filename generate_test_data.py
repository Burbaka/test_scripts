#!/usr/bin/env python
import subprocess

TEST_SCRIPTS = 'junk_data_scripts'
LOGIN_ITEMS = 'broken_login_items.py'
PREFERENCES_FILES = 'broken_preferences.py'
CACHE_FILES = 'user_cache_files.py'
LOG_FILES = 'user_log_files.py'


subprocess.call(f"./{TEST_SCRIPTS}/{LOG_FILES}", shell=True)
subprocess.call(f"./{TEST_SCRIPTS}/{CACHE_FILES}", shell=True)
subprocess.call(f"./{TEST_SCRIPTS}/{PREFERENCES_FILES}", shell=True)
# Because of Login Items this script requires root permissions to execute
# TODO think about optimizing this. Could be migrated to classes / methods usage in future
subprocess.call(f"./{TEST_SCRIPTS}/{LOGIN_ITEMS}", shell=True)
