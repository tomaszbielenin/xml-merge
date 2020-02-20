#Add file selection window
#Add parameters to specify root element and subelement
#Add templete file selection

import sys
import os
import xml.etree.ElementTree as ET

# sFolder = 'C:/Scripting/PenXml'
# dFile = 'XmlCombined.xml'
print(sys.argv)
if len(sys.argv) <= 1:
  print()
  print("-- Provide required parameters --")
  sFolder = str(input('-- Source folder path:'))
  dFile = os.path.join(sFolder, str(input('-- Output file name:')))
  # vfolders = input('Viewfolder/s:')
  # tolerance = str(0.001*float(input('Tolerance (mm):')))
else:
  sFolder = str(sys.argv[1]) # source xml file with search sets
  dFile = str(sys.argv[2]) # destination xml file
#   vfolders = sys.argv[3].split(",") # viewfolder list to be processed
#   tolerance = str(0.001*float(sys.argv[4])) # add function to set tolerance

# ((os.path.basename(dst)).split(".")[0]) - get file name
tmp = """<?xml version="1.0" encoding="UTF-8" ?>

<exchange xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://download.autodesk.com/us/navisworks/schemas/nw-exchange-12.0.xsd" units="ft" filename="F34_2.nwd" filepath="C:/_NavisworksLocal/693584">
  <viewpoints>
  </viewpoints>
</exchange>"""

droot = ET.fromstring(tmp)
vPts = droot.find("viewpoints")

vlist = []
for f in os.listdir(sFolder):
  if f.endswith(".xml"):
    # print(file)
    for v in ET.parse(os.path.join(sFolder, f)).findall('.//view'):
      vlist.append(ET.tostring(v))

for v in vlist:
  vPts.append(ET.fromstring(v))

f = open(dFile, "w")
(ET.ElementTree(droot)).write((f),encoding='unicode')
f.close()
