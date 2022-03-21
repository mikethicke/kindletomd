"""
Tests for kindle_to_md.py | kindle_to_md().
"""

import pytest
from kindle_to_md import kindle_to_md

from kindle_to_md import MisformattedKindleData

@pytest.mark.usefixtures( 'test_data' )
class TestKindleToMd :
    def test_parse_highlights_with_notes_section( self ) :
        markdown = kindle_to_md( self.test_data['good_book'], True )
        assert( isinstance( markdown, str ) )
        assert( markdown.startswith( "# A Book (With Parentheses)\n\nAuthors: An Author, Another Author, and Third Author" ) )
        assert( '## Highlights with Notes' in markdown )
        assert( '## All Highlights' in markdown )
    
    def test_parse_highlights_without_notes_section( self ) :
        markdown = kindle_to_md( self.test_data['good_book'], False )
        assert( isinstance( markdown, str ) )
        assert( markdown.startswith( "# A Book (With Parentheses)\n\nAuthors: An Author, Another Author, and Third Author" ) )
        assert( '## Highlights with Notes' not in markdown )
        assert( '## All Highlights' in markdown )

    def test_missing_title( self ) :
        with pytest.raises( MisformattedKindleData ) :
            markdown = kindle_to_md( self.test_data['missing_title'] )
    
    def test_missing_authors( self ) :
        with pytest.raises( MisformattedKindleData ) :
            markdown = kindle_to_md( self.test_data['missing_authors'] )

    def test_missing_highlights( self ) :
        with pytest.raises( MisformattedKindleData ) :
            markdown = kindle_to_md( self.test_data['missing_highlights'] )
    
