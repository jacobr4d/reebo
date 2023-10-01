import sys
import collections
import argparse
import xml.etree.ElementTree as ET

text = sys.stdin.read()

parser = argparse.ArgumentParser(
    prog='maketext',
    description='Parse EEBO TCP XML file',
    epilog='visit https://quod.lib.umich.edu/e/eebogroup/ for more info'
)

parser.add_argument('-div1')
parser.add_argument('-div2')
args = parser.parse_args()

def sstrip(s):
    return s.rstrip('\n') 

def printsstrip(s):
    print(sstrip(s), end='')

root = ET.fromstring(sys.stdin.read());
notes = set(root.findall(".//NOTE"))
subnotes = set(root.findall(".//NOTE//*"))

if not args.div1:
    elements = root.findall(".//DIV1")
elif not args.div2:
    elements = root.findall(f".//DIV1[@N='{args.div1}']") + root.findall(f".//DIV1[@TYPE='{args.div1}']")
else:
    elements = root.findall(f".//DIV1[@N='{args.div1}']//DIV2[@N='{args.div2}']")
    
for u in elements: 
    print()
    for v in u.iter():
        if v in notes:
            if v.tail: 
                printsstrip(v.tail)
        elif v in subnotes:
            continue
        elif v.tag == 'P' or v.get('TYPE') == 'section':
            print()
            if v.text: printsstrip(v.text)
            if v.tail: printsstrip(v.tail)
        else:
            if v.text: printsstrip(v.text)
            if v.tail: printsstrip(v.tail)


