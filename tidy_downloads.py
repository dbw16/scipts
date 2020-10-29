#!/usr/bin/env python3
from os import listdir, path, makedirs, rename
from datetime import date


def main():
    base_path = path.expanduser("~") + "/Downloads/"
    only_files_base = [f for f in listdir(base_path) if path.isfile(path.join(base_path, f))]

    if len(only_files_base) == 0:
        return 0

    today_download_path = base_path + str(date.today()) + "/"
    makedirs(today_download_path, exist_ok=True)

    for file in only_files_base:
        rename(base_path + file, today_download_path + file)
    return 0


if __name__ == '__main__':
    main()
