# -*- coding:UTF-8 -*-
import os


def save_content(content):
    with open(r"D:\code.doc", "a", encoding="utf8") as bf:
        bf.write(content)


def run(b_p):
    directory = os.listdir(b_p)
    for item in directory:
        temp_path = os.path.join(b_p, item)
        if os.path.isdir(temp_path):
            run(temp_path)
        elif os.path.isfile(temp_path) and temp_path.endswith(".java"):
            with open(temp_path, "r", encoding="utf8") as f:
                save_content(f.read())


if __name__ == '__main__':
    base_path = r"E:\cerium\app\gs-promotion-android\app\src\main\java\com\shrise\gspromotion\view"
    run(base_path)