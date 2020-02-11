#!/usr/bin/env python
import getpass
import os
from pathlib import Path

USERNAME = getpass.getuser()
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_PATH = CURRENT_DIR + '/test_data'
TEST_DATA_FILE_NAME = 'launch_agent_test_record.xml'
USER_LIBRARY_PATH = f'/Users/{USERNAME}/Library/'
SYSTEM_LIBRARY_PATH = f'/Library'
LOGIN_AGENT_FILE_NAME = 'com.burbaka.TestBrokenLoginItem_Agent'
LOGIN_AGENT_EXTENSION = 'plist'


def generate_file(name=LOGIN_AGENT_FILE_NAME, path=f"{SYSTEM_LIBRARY_PATH}/LaunchAgents"):
    Path(path).mkdir(parents=True, exist_ok=True)
    file_path = f"{path}/{name}.{LOGIN_AGENT_EXTENSION}"
    fill_file_content(file_path)


def fill_file_content(target_file_path):
    original_xml_file = f"{TEST_DATA_PATH}/{TEST_DATA_FILE_NAME}"
    source_file = open(original_xml_file)
    target_file = open(target_file_path, 'w+')

    for line in source_file.readlines():
        target_file.write(line)

    target_file.close()
    source_file.close()


generate_file()
generate_file(name='com.burbaka.TestBrokenLoginItem_Daemon', path=f"{SYSTEM_LIBRARY_PATH}/LaunchDaemons")
# TODO we run this script under 'root', thus it creates test files under wrong user. Need to fix this
# generate_file(path=f"{USER_LIBRARY_PATH}/LaunchAgents")
