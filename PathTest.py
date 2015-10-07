#! usr/bin/env python
#! --coding: utf8--

import os
import sys

with open('C:\\Users\\Joey\\Documents\\GitHub\\flasky\\text.txt', 'w+') as f:
    dirname, filename = os.path.split(os.path.realpath(__file__))
    f.write(os.path.dirname(__file__)+'\n')
    f.write(os.path.abspath(os.path.dirname(__file__))+'\n')
    f.write('dirname = ' + dirname + '\n')
    f.write('filename = ' + filename + '\n')
    f.write('realpath = ' + os.path.join(dirname,'data.sqlite') + '\n')
    f.write('sys.argv[0] = ' + sys.argv[0])

f.close()