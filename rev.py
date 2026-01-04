from xml.etree import ElementTree as ET
from xml.dom import minidom

def remove_whitespace_nodes(node):
    for child in list(node.childNodes):
        if child.nodeType == child.TEXT_NODE and child.data.strip() == "":
            node.removeChild(child)
        elif child.hasChildNodes():
            remove_whitespace_nodes(child)

input_path = "publications_pretty.xml"
output_path = "publications_chronological1.xml"

# Parse XML
tree = ET.parse(input_path)
root = tree.getroot()

# Reverse publication order
pubs = list(root.findall("publication"))
root.clear()
for p in reversed(pubs):
    root.append(p)

# Convert to DOM
rough = ET.tostring(root, encoding="utf-8")
dom = minidom.parseString(rough)

# 🔑 Remove whitespace-only text nodes
remove_whitespace_nodes(dom)

# Pretty print without blank lines
pretty = dom.toprettyxml(indent="  ", encoding="utf-8")

with open(output_path, "wb") as f:
    f.write(pretty)
