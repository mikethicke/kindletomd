# Kindle to Markdown

Kindle to Markdown converts Kindle notes and highlights exported by Bookcision as JSON into Markdown.

## Installation

1. Ensure [pip is installed](https://pip.pypa.io/en/stable/installation/).
2. ```pip install kindle-to-md```

## Usage

To export your Kindle notes and highlights using Bookcision:

1. [Install Bookcision](https://readwise.io/bookcision).
2. View your [notes an highlights](https://read.amazon.com/notebook) on Amazon.
3. Run the Bookcision bookmarklet.
4. Select Download | as JSON from the Bookcision menu.

To convert your notes to Markdown:

1. In terminal, run ```kindle-to-md {downloaded_notes.json} {output_file.md}```
2. You can also run ```kindle-to-md {downloaded_notes.json}``` to output the notes to terminal.

To import to another Python script:

```python
import kindle_to_md
```

## Bug Reports and Feature Requests

To submit a bug report or make a feature request, [create an issue](https://github.com/mikethicke/kindletomd/issues/new) on the GitHub repostitory.

## Development

The development repository is located at [https://github.com/mikethicke/kindletomd](https://github.com/mikethicke/kindletomd).

Pull Requests should be accompianed by unit tests that fail before the changes are merged and pass afterwards.

This project follows Google's [Python Style Guide](https://google.github.io/styleguide/pyguide.html).

This package uses a src layout, so you will have to build and install the package locally to run the tests.

Sample development workflow (for MacOS / Linux):

1. Clone the repository: ```git clone https://github.com/mikethicke/kindletomd.git```
2. Change to your repository directory: ```cd kindletomd```
3. Create a virtual environment: ```python3 -m venv venv```
4. Activate the virtual environment: ```source venv/bin/activate```
5. Install development dependencies: ```pip install -r requirements.txt```
6. Write test or tests that fail for the bug you are addressing or feature you are developing. Tests are located in the ```tests``` directory. Avoid putting test data directly in the unit tests themselves. Instead, put data in ```test-data``` directory or in ```conftest.py```. This makes it easier to reuse data in other tests. If your test addresses a specific issue, reference the issue in the test's docblock.
7. Build the package: ```python -m build```
8. Install the package locally: ```pip install dist/{pacakge}.tar.gz```
9. Run pytest:
    1. ```cd tests```
    2. ```pytest```
10. Your tests should fail and none others should.
11. Implement your changes.
12. Rebuild the package.
13. Reinstall the package.
14. Re-run pytest and confirm your changes cause your tests to pass.
15. Commit your changes and open a Pull Request on Github to merge your changes. 

