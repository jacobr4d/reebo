#!/usr/bin/env python3
import sys
import collections
import xml.etree.ElementTree

def iterwalk(root, events=None, tags=None):
    """Incrementally walks XML structure (like iterparse but for an existing ElementTree structure)
    Returns an iterator providing (event, elem) pairs.
    Events are start and end
    events is a list of events to emit - defaults to ["start","end"]
    tags is a single tag or a list of tags to emit events for - if empty/None events are generated for all tags
    """
    # each stack entry consists of a list of the xml element and a second entry initially None
    # if the second entry is None a start is emitted and all children of current element are put into the second entry
    # if the second entry is a non-empty list the first item in it is popped and then a new stack entry is created
    # once the second entry is an empty list, and end is generated and then stack is popped
    stack = [[root,None]]
    tags = [] if tags is None else tags if type(tags) == list else [tags]
    events = events or ["start","end"]
    def iterator():
        while stack:
            elnow,children = stack[-1]
            if children is None:
                # this is the start of elnow so emit a start and put its children into the stack entry
                if ( not tags or elnow.tag in tags ) and "start" in events:
                    yield ("start",elnow)
                # put the children into the top stack entry
                stack[-1][1] = list(elnow)
            elif len(children)>0:
                # do a child and remove it
                thischild = children.pop(0)
                # and now create a new stack entry for this child
                stack.append([thischild,None])                
            else:
                # finished these children - emit the end
                if ( not tags or elnow.tag in tags ) and "end" in events:
                    yield ("end",elnow)
                stack.pop()
    return iterator

root = xml.etree.ElementTree.fromstring(sys.stdin.read())

for e in root.iter():
    if e.tag == 'HEAD':
        print('<h1>')
        print(xml.etree.ElementTree.tostring(e, encoding='unicode', method='text'))
        print('</h1>')
    if e.tag == 'P':
        print('<p>')
        print(xml.etree.ElementTree.tostring(e, encoding='unicode', method='text'))
        print('</p>')

# for e1 in root.iter():
#     if e1.get('TYPE') == 'chapter':

#         print(xml.etree.ElementTree.tostring(e1, encoding='unicode', method='text'))
        