import os
import sys


def walk(basepath: str):
    print(f'walk on {basepath}')
    for dir_path, dir_name , filenames in os.walk(basepath):
        print(dir_path, dir_name, filenames)


if __name__ == '__main__':
    walk(sys.argv[1])
