"""
Unit tests for kindle_to_md.py | parse_json_file().
"""

import pytest

from kindle_to_md import parse_json_file
from kindle_to_md import MisformattedKindleData

@pytest.mark.usefixtures( 'file_paths' )
@pytest.mark.usefixtures( 'test_data' )
class TestParseJSONFile :
    def test_parse_good_book( self ) :
        parsed_book = parse_json_file( self.file_paths['good'] )
        assert( isinstance( parsed_book, dict ) )
        assert( parsed_book['asin'] == 'A0A0A0A0A0' )
        assert( parsed_book['title'] == 'A Book (With Parentheses)' ) 
        assert( parsed_book['authors'] == 'An Author, Another Author, and Third Author' )
        assert( isinstance( parsed_book['highlights'], list ) )
        assert( parsed_book['highlights'][0] == self.test_data['individual_highlights']['just-highlight'] )
        assert( parsed_book['highlights'][1] == self.test_data['individual_highlights']['highlight-and-note'] )
        assert( parsed_book['highlights'][2] == self.test_data['individual_highlights']['just-note'] )
        assert( parsed_book['highlights'][3] == self.test_data['individual_highlights']['cyrillic' ] )
    
    def test_parse_book_not_kindle( self ) :
        parsed_book = parse_json_file( self.file_paths['not-kindle'] )
        assert( parsed_book is not None )

    def test_parse_book_bad_json( self ) :
        with pytest.raises( MisformattedKindleData ) :
            parsed_book = parse_json_file( self.file_paths['bad-json'] )
    
    def test_parse_book_not_json( self ) :
        with pytest.raises( MisformattedKindleData ) :
            parsed_book = parse_json_file( self.file_paths['not-json'] )
    
    def test_parse_non_existent_book( self ) :
        with pytest.raises( FileNotFoundError ) :
            parsed_book = parse_json_file( 'path/no-book-here.json' )
