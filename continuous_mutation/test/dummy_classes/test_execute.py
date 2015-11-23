import xml.etree.ElementTree

def executeXML(filename):
    e = xml.etree.ElementTree.parse(filename).getroot()
    
    l = []
    for atype in e.findall('test'):
        l += (atype.get('ref'))
     
    return " dummy_classes/".join(l)
