import os
from clint.textui import indent, puts, colored


root_dir = os.getcwd()
root_list = root_dir.split('\\')
root = root_list[-1]
for x, y, z in os.walk(os.getcwd(), topdown=True):
    x_list = x.split('\\')
    if root in x_list:
        len_curr_list = len(x_list)
        root_position = x_list.index(root)
        distance_root = len_curr_list - root_position
        with indent(distance_root, quote='|'):
            puts(x_list[-1])
        #print('-' * distance_root, x_list[-1])
        for file in z:
            with indent(distance_root + 2, quote='—'*(distance_root+1)):
                puts(file)
            #print('-' * (distance_root + 3), file)





