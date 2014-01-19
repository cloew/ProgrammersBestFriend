from xml.dom.minidom import parseString
from xml.etree.ElementTree import tostring

def SaveEtreeXMLPrettily(tree, filename):
    """ Save the Etree XML prettily to the filename given """
    xmlString = tostring(tree.getroot())
    
    xmlString = xmlString.replace('\n', '')
    xmlString = xmlString.replace('\t', '')
    xmlString = xmlString.replace('ns0:', '')
    xmlString = xmlString.replace(':ns0', '')
    
    xml = parseString(xmlString)
    prettyXMLString = xml.toprettyxml()
    
    with open(filename, 'w') as file:
        file.write(prettyXMLString)