from html_elements import elements as e

element = e.P(["Hello world"], style={"font-weight": "bold"})

assert element.to_html(format=False) == (
    '<p style="font-weight: bold">Hello world</p>'
)
