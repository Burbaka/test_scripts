#!/usr/bin/env python

import os
import getpass
import random
import string
from pathlib import Path

LOG_FILE_ENDING = 'log'
USERNAME = getpass.getuser()
LOG_FILE_PATH = f'/Users/{USERNAME}/Library/Logs'
LOG_FILE_NAME = 'user_test_junk_log_file_1'
SMALL_SIZE = 1048576  # 1 MB
BIG_SIZE = 5242880  # 5 MB


def generate_log_file(name=LOG_FILE_NAME, path=LOG_FILE_PATH, file_size=SMALL_SIZE):
    Path(path).mkdir(parents=True, exist_ok=True)
    file_path = f"{path}/{name}.{LOG_FILE_ENDING}"

    file = open(file_path, 'w+')
    fill_file_content(file, file_size)
    file.close()
    return os.path.abspath(f"temp_files/{name}.txt")


def fill_file_content(file, size):
    content = ''.join([random.choice(string.printable) for _ in range(size)])
    file.write(content)


generate_log_file()
generate_log_file('log_file_in_folder', f"{LOG_FILE_PATH}/UserLog_JunkTest", BIG_SIZE)
