# Getting started

## Installations

Installation is as simple as:

```bash
pip install html-elements
```

And afterwards in your python code

```python
from html_elements import elements as e

element = e.P(["Hello world"], style={"font-weight": "bold"})

assert element.to_html(format=False) == (
    '<p style="font-weight: bold">Hello world</p>'
)
```