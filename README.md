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

To convert your notes to markdown:

1. In terminal, run ```kindle-to-md {downloaded_notes.json} {output_file.md}```
2. You can also run ```kindle-to-md {downloaded_notes.json}``` to output the notes to terminal.

To import to another Python script:

```python
import kindle_to_md
```

## Development

The development repository is located at [https://github.com/mikethicke/kindletomd](https://github.com/mikethicke/kindletomd).

Development workflow:

1. Clone the repository: ```git clone https://github.com/mikethicke/kindletomd.git```

