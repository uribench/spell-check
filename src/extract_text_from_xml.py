#!/usr/bin/env python3

"""
Extracts text from XML files for spell-checking by PySpelling.
"""

import xml.sax
import glob

class ExtractXmlTextHandler(xml.sax.ContentHandler):
    """
    SAX Content Events Handler
    """

    def __init__(self, nodes, output):
        """Constructor

        Args:
            nodes (List): List of source nodes names
            output (file object): Output file object for extracted text
        """
        self.source_nodes = nodes
        self.output_file = output
        self.is_source_node = False
        self.data = ''

    def startElement(self, name, attrs):
        """SAX 'startElement' event handler - called when an element starts"""
        if name in self.source_nodes:
            self.is_source_node = True

    def characters(self, data):
        """SAX 'characters' event handler - called when a chunk of characters within the element are read"""
        if self.is_source_node:
            self.data += data

    def endElement(self, name):
        """SAX 'endElement' event handler - called when an element ends"""
        if self.is_source_node:
            self.output_file.write(self.data + '\n')
            self.is_source_node = False
            self.data = ''

def main():
    """Program entry point"""
    source_xml_files = "./xml-files/*.xml"
    source_nodes = ["value", "label", "description", "name"]
    output_file_name = "./xml-files/extracted_text_from_xml.txt"

    output_file = open(output_file_name, "w")
    parser = xml.sax.make_parser()
    parser.setContentHandler(ExtractXmlTextHandler(source_nodes, output_file))

    # parse all relevant xml files
    xml_files = glob.glob(source_xml_files)
    for xml_file in xml_files:
        output_file.write("\n---------------------------------------\n")
        output_file.write("Text extracted from <" + xml_file + ">:\n")
        output_file.write("---------------------------------------\n\n")
        parser.parse(open(xml_file,"r"))

    output_file.close()

if __name__ == '__main__':
    main()
