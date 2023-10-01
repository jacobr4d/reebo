#!/usr/bin/env python3
import sys
import collections
import xml.etree.ElementTree

t = sys.stdin.read()
t = t.replace('<HEAD>', '<h1>')
t = t.replace('</HEAD>', '</h1>')
t = t.replace('<LIST>', '<ul>')
t = t.replace('</LIST>', '</ul>')
t = t.replace('<ITEM>', '<li>')
t = t.replace('</ITEM>', '</li>')
t = t.replace('<P>', '<P style="text-align: justify;">')

print('<html lang="en">')
print('<head>')
print('<meta charset="utf-8">')
print('</head>')
print('<body>')
print('<div style="display: flex; align-items: center; justify-content: center;">')
print('<div style="width: 600px;">')
print(t, end='')
print('</div>')
print('</div>')
print('</body>')