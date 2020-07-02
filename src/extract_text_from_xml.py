#!/usr/bin/env python3

"""
Extracts text from XML files for spell-checking by PySpelling.
"""

import xml.sax
import glob

class KoboXmlHandler(xml.sax.ContentHandler):
    """
    SAX Content Events Handler
    """

    def __init__(self):
        """Constructor"""
        self.target_nodes = ["value", "label", "description", "name"]
        self.is_target_node = False
        self.data = ''

    def startElement(self, name, attrs):
        """SAX 'startElement' event handler - called when an element starts"""
        if name in self.target_nodes:
            self.is_target_node = True

    def characters(self, data):
        """SAX 'characters' event handler - called when a chunk of characters within the element are read"""
        if self.is_target_node:
            self.data += data

    def endElement(self, name):
        """SAX 'endElement' event handler - called when an element ends"""
        if self.is_target_node:
            tmp_file.write(self.data + '\n')
            self.is_target_node = False
            self.data = ''

parser = xml.sax.make_parser()
parser.setContentHandler(KoboXmlHandler())

tmp_file = open("./xml-files/extracted_text_from_xml.txt", "w")

# parse all relevant xml files
xml_files = glob.glob("./xml-files/*.xml")
for xml_file in xml_files:
    tmp_file.write("\n---------------------------------------\n")
    tmp_file.write("Text extracted from <" + xml_file + ">:\n")
    tmp_file.write("---------------------------------------\n\n")
    parser.parse(open(xml_file,"r"))

tmp_file.close()