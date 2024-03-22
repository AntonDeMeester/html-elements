from typing import List, Union

from html_elements import elements as e


def Input(type: str, name: str) -> e.BaseHtmlElement:
    return e.Div(
        [
            e.Label([name], classes=["label"]),
            e.Div(
                [e.Input(classes=["input"], type=type, placeholder=name, name=name)],
                classes=["control"]
            )
        ],
        classes=["field"]
    )

def InputTwo(
    type: str, 
    name: str, 
    label: str = "", 
    placeholder: str = "", 
    classes: Union[List[str], None] = None
) -> e.BaseHtmlElement:
    if not label:
        label = name.title()
    if not placeholder:
        placeholder = label
    if not classes:
        classes = ["control"]
    return e.Div(
        [
            e.Label([label], classes=["label"]),
            e.Div(
                [e.Input(classes=["input"], type=type, placeholder=label, name=name)],
                classes=classes
            )
        ],
        classes=["field"]
    )
