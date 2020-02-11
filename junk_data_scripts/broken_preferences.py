#!/usr/bin/env python
import getpass
import os
from pathlib import Path

USERNAME = getpass.getuser()
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_PATH = CURRENT_DIR + '/test_data'
TEST_DATA_FILE_XML = ''
TEST_DATA_FILE_BINARY = ''
USER_LIBRARY_PATH = f'/Users/{USERNAME}/Library/'
BROKEN_PREFERENCES_FILE_NAME = 'com.burbaka.TestBrokenPreferences_xml_format'
BROKEN_PREFERENCES_EXTENSION = 'plist'


def generate_file(test_file, name=BROKEN_PREFERENCES_FILE_NAME, path=f"{USER_LIBRARY_PATH}/Preferences"):
    Path(path).mkdir(parents=True, exist_ok=True)
    file_path = f"{path}/{name}.{BROKEN_PREFERENCES_EXTENSION}"
    test_file_path = f"{TEST_DATA_PATH}/{test_file}"
    fill_file_content(file_path, test_file_path)


def fill_file_content(target_file_path, test_file):
    source_file = open(test_file)
    target_file = open(target_file_path, 'w+')

    for line in source_file.readlines():
        target_file.write(line)

    target_file.close()
    source_file.close()


generate_file(test_file='broken_preferences_txt.xml')
generate_file(test_file='broken_preferences_binary.plist', name='com.burbaka.TestBrokenPreferences_binary_format')
# TODO add generation in /Library/Preferences dir (not user specific)

