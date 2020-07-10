#!/usr/bin/env python3

"""
Extracts text from XML files for spell-checking by PySpelling.
"""

import xml.sax
import glob
import os
import sys
import contextlib

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
        self.output = output
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
            self.output.write(self.data + '\n')
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
    if source_xml_files is None:
        source_xml_files = def_source_xml_files

    source_nodes_str = os.environ.get('SOURCE_NODES')
    if source_nodes_str is None:
        source_nodes = def_source_nodes
    else:
        source_nodes = source_nodes_str.split(', ')

    output_file_name = os.environ.get('OUTPUT_FILE_NAME')
    if output_file_name is None:
        output_file_name = def_output_file_name
    else:
        output_file_name = None # ignore the environ 'OUTPUT_FILE_NAME' and use sys.stdout instead

    return source_xml_files, source_nodes, output_file_name

@contextlib.contextmanager
def file_writer(file_name = None):
    """Create writer object based on file_name"""
    if file_name is not None:
        writer = open(file_name, "w")
    else:
        writer = sys.stdout

    yield writer

    if file_name is not None: 
        writer.close()

def main():
    """Program entry point"""
    source_xml_files, source_nodes, output_file_name = init_parameters()

    with file_writer(output_file_name) as output:
        parser = xml.sax.make_parser()
        parser.setContentHandler(ExtractXmlTextHandler(source_nodes, output))

        # parse all relevant xml files
        xml_files = glob.glob(source_xml_files)
        for xml_file in xml_files:
            output.write("\n---------------------------------------\n")
            output.write("Text extracted from <" + xml_file + ">:\n")
            output.write("---------------------------------------\n\n")
            parser.parse(open(xml_file,"r"))

if __name__ == '__main__':
    main()
