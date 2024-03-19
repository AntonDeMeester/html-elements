from typing import Any, List, Sequence

from html_elements import elements as e


def SimpleTable(data: Sequence[Any], columns: Sequence[str]) -> e.BaseHtmlElement:
    rows: List[e.BaseHtmlElement] = []
    for item in data:
        cells: List[e.BaseHtmlElement | str] = []
        for field in columns:
            cells.append(e.Td([getattr(item, field, "")]))
        rows.append(e.Tr(cells))
    return e.Table([e.Thead([e.Tr([e.Th([heading]) for heading in columns])]), *rows], classes=["table"])


data = [
    {"id": "1", "name": "Bobby Greenfield", "email": "bobby@greenfield.com"},
    {"id": "2", "name": "Johnny Smith", "email": "johhnySmith@gmail.com"},
    {"id": "3", "name": "Faith Dogman", "email": "faith.dogman@hotmail.com"},
    {"id": "4", "name": "Gregory House", "email": "greg.house@on.tv"},
]
table = SimpleTable(data, ["id", "name", "email"])
table.to_html()


SimpleTable(object(), ["test"])


from html_elements import elements as e


def Input(type: str, label: str) -> e.BaseHtmlElement:
    display = label.title()
    return e.Div(
        [
            e.Label([display], classes=["label"]),
            e.Div(
                [
                    e.Input(classes=["input"], type=type, placeholder=display, name=label),
                ],
                classes=["control"],
            ),
        ]
    )


Input(label="test", type="text")


html = e.Form(
    [
        Input("text", "name"),
        Input("email", "email"),
        e.Button("Submit", classes=["button"], type="submit"),
    ]
)

print(html.to_html())
