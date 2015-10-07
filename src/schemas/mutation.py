import xml.etree.ElementTree as parser

file = parser.parse("testconstellations.xsd")
root = file.getroot()
print(root)
