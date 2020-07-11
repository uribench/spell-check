"""Test Helper"""
import os

def set_test_env():
    """Set test environment variables"""
    os.environ['SOURCE_XML_FILES'] = './tests/test_fixture.xml'
    os.environ['SOURCE_NODES'] = 'value, label, description, name'
    os.environ['OUTPUT_FILE_NAME'] = 'Any text here will redirect output to sys.stdout'
