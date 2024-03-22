from html_elements import elements as e


def Input(type: str, label: str) -> e.BaseHtmlElement:
    display = label.title()
    return e.Div(
        [
            e.Label([display], classes=["label"]),
            e.Div(
                [e.Input(classes=["input"], type=type, placeholder=display, name=label)],
                classes=["control"]
            )
        ],
        classes=["field"]
    )

html = e.Form([
    Input("text", "name"),
    Input("email", "email"),
    e.Button(["Submit"], classes=["button"], type="submit")
])

raw = html.to_html(indent_step=2)
