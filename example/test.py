from reactish import components as c
from reactish.base import Page
from reactish.head import Body, Head, Link, Meta, Script

content = c.Div(
    c.Div(
        c.Div(
            c.Div(
                c.A(
                    "Back",
                    class_name="button",
                    href="https://opulent-rotary-phone-rrrrg74gpxf5xx5-8000.app.github.dev/snapshots",
                ),
                class_name=["column", "is-narrow"],
            ),
            c.Div(c.H("New snapshot", level=1, class_name="title")),
            class_name="columns",
        ),
        c.Form(
            c.Div(
                c.Label("Version", class_name="label"),
                c.Div(
                    c.Input(
                        class_name="input",
                        type="number",
                        placeholder="Version",
                        value=1,
                    ),
                    class_name="control",
                ),
                class_name="field",
            ),
            c.Div(
                c.Label("Name", class_name="label"),
                c.Div(
                    c.Input(
                        class_name="input",
                        type="text",
                        placeholder="name",
                        value="Hello World",
                    ),
                    class_name="control",
                ),
                class_name="field",
            ),
            c.Div(
                c.Label("Status", class_name="label"),
                c.Div("Active"),
                class_name="field",
            ),
            c.Input(class_name="button", type="submit", value="submit"),
        ),
        class_name=["block", "container"],
    ),
    class_name="section",
)

menu = c.Aside(
    c.P("General", class_name="menu-label"),
    c.Ul(c.Li(c.A("Snapshots", href="/snapshots")), class_name="menu-list"),
    class_name="menu",
)

layout = c.Div(
    c.Nav(menu, class_name="sidebar"), c.Main(content, class_name="centerpiece")
)

html = Page(
    Head(
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Link(
            rel="stylesheet",
            href="file:///Users/anton/Documents/personal/code/html/example/static/css/bulma.min.css",
        ),
        Script(
            src="https://kit.fontawesome.com/605ae70237.js", crossorigin="anonymous"
        ),
    ),
    Body(
        Link(
            href="file:///Users/anton/Documents/personal/code/html/example/static/css/base.css",
            rel="stylesheet",
        ),
        layout,
    ),
)

with open("test.html", "w") as f:
    f.write(html.to_html())
