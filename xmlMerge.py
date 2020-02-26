#Add parameters to specify root element and subelement
#Add templete file selection
#Check output file extension, change to xml

import sys
import os
import xml.etree.ElementTree as ET
import easygui

if len(sys.argv) <= 1:
  print("-- XML-MERGE --")
  print()
  print("-- Provide required parameters --")
  print('-- Source folder path:')
  sFolder = easygui.diropenbox()
  print('-- Select output file:')
  dFile = easygui.fileopenbox()
else:
  sFolder = str(sys.argv[1]) # source folder
  dFile = str(sys.argv[2]) # destination xml file

tmp = """<?xml version="1.0" encoding="UTF-8" ?>

<exchange xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://download.autodesk.com/us/navisworks/schemas/nw-exchange-12.0.xsd" units="ft" filename="F34_2.nwd" filepath="C:/_NavisworksLocal/693584">
  <viewpoints>
  </viewpoints>
</exchange>"""

droot = ET.fromstring(tmp)
sub = droot.find("viewpoints")

slist = []
for f in os.listdir(sFolder):
  if f.endswith(".xml"):
    # print(f)
    for s in ET.parse(os.path.join(sFolder, f)).findall('.//view'):
      slist.append(ET.tostring(s))

for s in slist:
  sub.append(ET.fromstring(s))

f = open(dFile, "w")
(ET.ElementTree(droot)).write((f),encoding='unicode')
f.close()
