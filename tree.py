import os
from clint.textui import indent, puts, colored
import sys


def directory_checker():
    root_dir = os.getcwd()
    root_list = root_dir.split('\\')
    root = root_list[-1]
    for main_dir, sub_dir, file_names in os.walk(os.getcwd(), topdown=True):
        main_dir_list = main_dir.split('\\')
        if root in main_dir_list:
            len_curr_list = len(main_dir_list)
            root_position = main_dir_list.index(root)
            distance_root = len_curr_list - root_position
            with indent(distance_root, quote='|' + '-' * (distance_root * 3)):
                puts(colored.green(main_dir_list[-1]))
            # print('-' * distance_root, x_list[-1])
            for file in file_names:
                with indent(distance_root + 2, quote='|' + ' ' * (distance_root * 3 + 4)):
                    if not len(file_names):
                        print('No files in this folder')
                    else:
                        puts(file)
                    # print('-' * (distance_root + 3), file)


if __name__ == '__main__':
    directory_checker()
