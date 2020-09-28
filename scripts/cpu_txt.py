#!/bash/bin/python

import os

with open('cpu.txt', 'r') as fr, open('output.txt', 'w') as fd, open('output_mem.txt', 'w') as fo:
    for text in fr.readlines():
        x = text.split(' ')[8] 
        y = text.split(' ')[9] 
        fd.write(x)
        fd.write('\r\n')
        fo.write(y)
        fo.write('\r\n')
    print('success')
