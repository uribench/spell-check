#!/usr/bin/env python3

import xml.sax
import glob

class KoboXmlHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.target_nodes = ["value", "label", "description", "name"]
        self.is_target_node = False

    # called when an element starts
    def startElement(self, name, attrs):
        if name in self.target_nodes:
            self.is_target_node = True

    # called when a character is read
    def characters( self, data):
        if self.is_target_node:
            tmp_file.write(data + '\n')

    # called when an elements ends
    def endElement(self, tag):
        self.is_target_node = False

parser = xml.sax.make_parser()
parser.setContentHandler(KoboXmlHandler())

tmp_file = open("./xml-files/extracted_text_from_xml.txt", "w")

# parse all relevant xml files
xml_files = glob.glob("./xml-files/*.xml")
for xml_file in xml_files:
    tmp_file.write("\n---------------------------------------\n")
    tmp_file.write("Text extracted from <" + xml_file + ">:\n")
    parser.parse(open(xml_file,"r"))

tmp_file.close()