# Some examlpes: https://www.deltaxml.com/products/merge/xml-merge/ 
#Add parameters to specify root element and subelement
#Add templete file selection
#Check output file extension, change to xml
#What if file/folder selection cancelled

import sys
import os
import xml.etree.ElementTree as ET
import easygui

if len(sys.argv) <= 1:
  print("-- XML-MERGE --")
  print()
  print("-- Provide required parameters --")
  print('-- Source folder path:')
  sFolder = str(easygui.diropenbox()) # this causes problem in line 39
  print(sFolder)
  print('-- Select output file:')
  dFile = easygui.fileopenbox(default=sFolder)
  print(dFile)
else:
  sFolder = str(sys.argv[1]) # source folder
  dFile = str(sys.argv[2]) # destination xml file

tmp = """<?xml version="1.0" encoding="UTF-8" ?>

<exchange xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://download.autodesk.com/us/navisworks/schemas/nw-exchange-12.0.xsd" units="ft" filename="F34_2.nwd" filepath="C:/_NavisworksLocal/693584">
  <viewpoints>
  </viewpoints>
</exchange>"""

d = ET.fromstring(tmp)
droot = d.find("viewpoints")

slist = []
for f in os.listdir(sFolder):
  if f.endswith(".xml"):
    # print(os.path.join(sFolder, f))
    for s in ET.parse(os.path.join(sFolder, f)).findall('.//view'): # there's a problem caused by folder path, line 16
      slist.append(ET.tostring(s))

for s in slist:
  droot.append(ET.fromstring(s))

f = open(dFile, "w")
(ET.ElementTree(d)).write((f),encoding='unicode')
f.close()
