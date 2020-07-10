#!/usr/bin/env python3

"""
Extracts text from XML files for spell-checking by PySpelling.
"""

import xml.sax
import glob
import os
import sys

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
            sys.stdout.write(self.data + '\n')  # for testing
            self.is_source_node = False
            self.data = ''

def init_parameters():
    """Set actual parameters values"""
    # default parameters values
    def_source_xml_files = "./xml-files/*.xml"
    def_source_nodes = ["value", "label", "description", "name"]
    def_output_file_name = "./xml-files/extracted_text_from_xml.txt"

    # set actual parameters values from environment variables (for tests) or use the defaults
    source_xml_files = os.environ.get('SOURCE_XML_FILES')
    if source_xml_files == None:
        source_xml_files = def_source_xml_files

    source_nodes_str = os.environ.get('SOURCE_NODES')
    if source_nodes_str == None:
        source_nodes = def_source_nodes
    else:
        source_nodes = source_nodes_str.split(', ')

    output_file_name = os.environ.get('OUTPUT_FILE_NAME')
    if output_file_name == None:
        output_file_name = def_output_file_name

    return source_xml_files, source_nodes, output_file_name

def main():
    """Program entry point"""
    source_xml_files, source_nodes, output_file_name = init_parameters()

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
