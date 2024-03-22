from typing import Any, List, Sequence, Union

from html_elements import elements as e


def SimpleTable(data: Sequence[Any], columns: Sequence[str]) -> e.BaseHtmlElement:
    rows: List[e.BaseHtmlElement] = []
    for item in data:
        cells: List[Union[e.BaseHtmlElement, str]] = []
        for field in columns:
            cells.append(e.Td([item.get(field, "")]))
        rows.append(e.Tr(cells))
    return e.Table([e.Thead([e.Tr([e.Th([heading]) for heading in columns])]), *rows], classes=["table"])

data = [
    {"id": "1", "name": "Bobby Greenfield", "email": "bobby@greenfield.com"},
    {"id": "2", "name": "Johnny Smith", "email": "johhnySmith@gmail.com"},
    {"id": "3", "name": "Faith Dogman", "email": "faith.dogman@hotmail.com"},
    {"id": "4", "name": "Gregory House", "email": "greg.house@on.tv"},
]

table = SimpleTable(data, ["id", "name", "email"])
raw = table.to_html()

def test_error():
    SimpleTable(object(), ["test"]) # type: ignore
