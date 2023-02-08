#!/usr/bin/env python3

from local_lib import path


def ex01():
    p = path.Path('./new_folder')
    if not p.isdir():
        p.mkdir()

    f = p / "new_file.txt"
    
    f.write_text("Hello, path.py!")

    print(f.text())


if __name__ == '__main__':
    ex01()
