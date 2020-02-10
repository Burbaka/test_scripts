#!/usr/bin/env python

import getpass
import random
import string
from pathlib import Path

USERNAME = getpass.getuser()
CACHE_FILE_PATH = f'/Users/{USERNAME}/Library/Caches'
CACHE_NESTED_FOLDER = 'UserCache_JunkTest'
CACHE_FILE_NAME = 'user_cache_junk_file'
SMALL_SIZE = 1048576  # 1 MB
BIG_SIZE = 5242880  # 5 MB


def generate_file(name=CACHE_FILE_NAME, path=CACHE_FILE_PATH, file_size=SMALL_SIZE):
    Path(path).mkdir(parents=True, exist_ok=True)
    file_path = f"{path}/{name}"

    file = open(file_path, 'w+')
    fill_file_content(file, file_size)
    file.close()


def fill_file_content(file, size):
    content = ''.join([random.choice(string.printable) for _ in range(size)])
    file.write(content)


generate_file()
generate_file('cache_file_in_folder', f"{CACHE_FILE_PATH}/{CACHE_NESTED_FOLDER}", BIG_SIZE)

filename = 'cache_file_in_nested_folder'
generate_file(filename, f"{CACHE_FILE_PATH}/{CACHE_NESTED_FOLDER}/{CACHE_NESTED_FOLDER}1", BIG_SIZE)
generate_file(filename, f"{CACHE_FILE_PATH}/{CACHE_NESTED_FOLDER}/{CACHE_NESTED_FOLDER}2", SMALL_SIZE)

# TODO add generation for the data in Library / Containers / <App> / Data / library / Caches / <generated file>

