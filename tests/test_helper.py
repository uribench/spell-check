import os

def set_test_env():
    os.environ['SOURCE_XML_FILES'] = './tests/test_fixture.xml'
    os.environ['SOURCE_NODES'] = 'value, label, description, name'
    # os.environ['OUTPUT_FILE_NAME'] = ...
