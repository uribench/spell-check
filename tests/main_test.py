"""Functional test of the 'extract_text_from_xml.py' script"""
from subprocess import Popen, PIPE
from .test_helper import set_test_env

def test_output_of_main():
    """Sample tests of the text extracted from XML by the 'extract_text_from_xml.py' script"""
    program = 'src/extract_text_from_xml.py'
    output = Popen([program], stdout=PIPE).communicate()[0]
    assert b'Some text in "value" node' in output
    assert b'Some other text in "value" node' in output
    assert b'Some text in "description" node' in output
    assert b'Some other instance text in "name" node' in output
    assert b'Some other instance text in a deeper nested "label" node' in output

set_test_env()
