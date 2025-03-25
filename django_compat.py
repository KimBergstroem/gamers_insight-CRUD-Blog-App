"""
Compatibility patch for running Django 3.2 with Python 3.13+
"""
import sys
import re
from types import ModuleType
import email.parser

# Create a mock cgi module with the minimum functionality Django needs
class MockFieldStorage:
    def __init__(self, *args, **kwargs):
        self.list = []
        self.file = None
    
    def getvalue(self, key, default=None):
        return default
    
    def getlist(self, key):
        return []

def parse_header(line):
    """Parse a Content-type like header.
    
    This is a replacement for the cgi.parse_header function that was removed in Python 3.11+
    """
    if not line:
        return '', {}
    
    # Use email.parser to handle the header parsing
    header = email.parser.HeaderParser().parsestr(f'Content-Type: {line}')
    main_value = header.get_content_type()
    
    # Extract parameters
    params = {}
    for key, value in header.get_params()[1:]:  # Skip the first one as it's the main value
        params[key] = value
    
    return main_value, params

def valid_boundary(boundary):
    """Check if the boundary string is valid.
    
    This is a replacement for the cgi.valid_boundary function that was removed in Python 3.11+
    """
    # Convert boundary to string if it's not already
    if not isinstance(boundary, str):
        try:
            boundary = str(boundary)
        except:
            return False
            
    # Per RFC 2046, section 5.1.1, the boundary may be any string
    # that doesn't occur in the body, including the hyphens.
    if not boundary:
        return False
        
    # Make sure the boundary is a valid MIME boundary
    # The spec says the boundary should be 1-70 ASCII chars,
    # not ending with a space and not containing control chars
    if len(boundary) > 70:
        return False
        
    for c in boundary:
        # Make sure c is a single character string
        if not isinstance(c, str) or len(c) != 1:
            return False
        char_code = ord(c)
        if char_code < 32 or char_code > 126:
            return False
            
    if boundary.endswith(' '):
        return False
        
    return True

# Create the mock cgi module
mock_cgi = ModuleType('cgi')
mock_cgi.FieldStorage = MockFieldStorage
mock_cgi.parse_header = parse_header
mock_cgi.valid_boundary = valid_boundary

# Add the mock module to sys.modules
sys.modules['cgi'] = mock_cgi
print("Applied Django compatibility patch for Python 3.13+")