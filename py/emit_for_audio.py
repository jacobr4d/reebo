#!/usr/bin/env python3
import sys
import collections
import xml.etree.ElementTree
import os

root = xml.etree.ElementTree.fromstring(sys.stdin.read())

proj_root = os.path.join(os.path.dirname(__file__), '..')
os.system('mktemp -d -q ' + os.path.join(proj_root, 'tmp'))

for x in root.iter():
    if x.get('TYPE') == 'book':
        for y in x.iter():
            if y.get('TYPE') == 'chapter':
                bookno, chapno = x.get('N'), y.get('N')
                fname = 'b' + bookno.zfill(3) + 'c' + chapno.zfill(3)
                with open(os.path.join(proj_root, 'tmp', fname), 'w') as f:
                    t = xml.etree.ElementTree.tostring(y, encoding='unicode', method='text')
                    t = " ".join(t.split())
                    f.write(t)


