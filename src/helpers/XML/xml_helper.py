from xml.dom.minidom import parseString
from xml.etree.ElementTree import tostring

def SaveEtreeXMLPrettily(tree, filename):
    """ Save the Etree XML prettily to the filename given """
    xmlString = tostring(tree.getroot())
    
    xmlString = xmlString.replace('\n', '')
    xmlString = xmlString.replace('\t', '')
    
    xml = parseString(xmlString)
    prettyXMLString = xml.toprettyxml()
    
    with open(filename, 'w') as file:
        file.write(prettyXMLString)