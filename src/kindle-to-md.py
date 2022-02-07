'''
Converts JSON Amazon Kindle notes generated by Bookcision to markdown.

Bookcision (https://bookcision.readwise.io/) is a bookmarklet that exports
Kindle notes and highlights (https://read.amazon.com/notebook). This script
converts notes and highlights exported as JSON to markdown.

Syntax: kindle-to-md.py <inputfile.json> <outputfile.md> 
'''

import sys
import json

def parse_json_file( file_name: str) -> any :
    '''
    Parses json-encoded file and returns data object.
    '''
    with open( file_name, 'r' ) as file :
        data = json.load( file )
    return data

def kindle_json_to_md ( json_data: any ) -> str :
    '''
    Translate json data from Kindle export into MarkDown formatted string.
    '''
    
