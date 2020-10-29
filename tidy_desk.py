#!/usr/bin/env python3
from os import listdir, path, makedirs, rename
from datetime import date


def main():
    base_path = path.expanduser("~") + "/Desktop/"
    screenshots_path = base_path + "Screenshots/"
    only_files_desktop = [f for f in listdir(base_path) if path.isfile(path.join(base_path, f))]

    if len(only_files_desktop) == 0:
        return 0

    makedirs(screenshots_path, exist_ok=True)

    today_screenshots_path = screenshots_path + str(date.today()) + "/"
    makedirs(today_screenshots_path, exist_ok=True)

    for file in only_files_desktop:
        if "screenshot" in file.lower():
            rename(base_path + file, today_screenshots_path + file)
    return 0


if __name__ == '__main__':
    main()
