import os
import sys
import shutil
import re


def walk(basepath: str):
    pic_files = []
    wmv_files = []
    print(f'walk on {basepath}')
    for dir_path, dirnames, filenames in os.walk(basepath):
        rel_path = os.path.relpath(dir_path, basepath)
        for filename in filenames:
            if filename.startswith('.'):
                continue
            if filename.endswith('.jpg') or filename.endswith('.JPG'):
                pic_files.append((rel_path, filename))
            elif filename.endswith('.wmv') or filename.endswith('.mov') or filename.endswith('.mp4') or filename.endswith('.3gp'):
                wmv_files.append((rel_path, filename))
    return pic_files, wmv_files


def move(files, folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

    for rel_path, filename in files:
        src_path = os.path.join(rel_path, filename)
        dst_dir = re.sub(r'[ /\\]', '_', rel_path)
        dst_path = os.path.join(folder_name, f'{dst_dir}-{filename}')

        print(src_path, '--', dst_path)
        shutil.move(src_path, dst_path)


def perform(basepath):
    os.chdir(basepath)
    pic_files, wmv_files = walk('.')
    move(pic_files, 'jpg')
    move(wmv_files, 'wmv')


if __name__ == '__main__':
    perform(sys.argv[1])
