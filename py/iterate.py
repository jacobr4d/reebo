#!/usr/bin/env python3
import sys
import collections
import xml.etree.ElementTree as ET

root = ET.fromstring(sys.stdin.read())

out = [""]
for element in root.iter():
    if element.tag == 'PB':
        out.append("")
    if element.text is not None:
        print(element.tag, 'text', repr(element.text))
        out[-1] = out[-1] + element.text

    if element.tail is not None:
        print(element.tag, 'tail', repr(element.tail))
        out[-1] = out[-1] + element.tail

print(out[:10])
