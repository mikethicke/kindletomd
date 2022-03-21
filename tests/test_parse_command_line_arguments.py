"""
Unit tests for kindle_to_md.py | parse_command_line_arguments
"""

import pytest
from pytest_mock import mocker

from kindle_to_md import parse_command_line_arguments
from kindle_to_md import InvalidCommandLineArguments

class TestParseCommandLineArguments :
    def test_parse_no_arguments( self, mocker ) :
        mocker.patch(
            'sys.argv',
            [
                'kindle-to-md'
            ]
        )
        with pytest.raises( InvalidCommandLineArguments ) :
            parse_command_line_arguments()
    
    def test_parse_too_many_arguments( self, mocker ) :
        mocker.patch(
            'sys.argv',
            [
                'kindle-to-md',
                'input_file',
                'output_file',
                'extra_argument'
            ]
        )
        with pytest.raises( InvalidCommandLineArguments ) :
            parse_command_line_arguments()

    def test_parse_single_argument( self, mocker ) :
        mocker.patch(
            'sys.argv',
            [
                'kindle-to-md',
                'path/input_file'
            ]
        )
        ( input_filename, output_filename ) = parse_command_line_arguments()
        assert( input_filename == 'path/input_file' )
        assert( output_filename is None )

    def test_parse_two_arguments( self, mocker ) :
        mocker.patch(
            'sys.argv',
            [
                'kindle-to-md',
                'path/input_file',
                'path/output_file'
            ]
        )
        ( input_filename, output_filename ) = parse_command_line_arguments()
        assert( input_filename == 'path/input_file' )
        assert( output_filename == 'path/output_file' )

