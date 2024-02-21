from reactish import components as c
from reactish.base import BaseComponent, Page
from reactish.head import Body, Head, Link, Meta, Script


def BasePage(*content: BaseComponent, selected: str | None = None) -> BaseComponent:
    is_selected = lambda x: "is-active" if selected == x else None
    menu = c.Aside(
        c.P("General", class_name="menu-label"),
        c.Ul(
            c.Li(c.A("Invoices", href="/invoices", class_name=is_selected("invoices"))),
            c.Li(c.A("Expenses", href="/expenses", class_name=is_selected("expenses"))),
            c.Li(c.A("Cards", href="/cards", class_name=is_selected("cards"))),
            c.Li(c.A("Manager", href="/manager", class_name=is_selected("manager"))),
            class_name="menu-list",
        ),
        class_name="menu",
    )
    layout = c.Div(
        c.Nav(menu, class_name="sidebar"),
        c.Main(
            *content,
            class_name="centerpiece",
            style={"overflow": "hidden", "width": "calc(100% - 200px)"}
        ),
        class_name="wrapper",
    )

    return Page(
        Head(
            Meta(charset="UTF-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Link(
                rel="stylesheet",
                href="/static/css/style.css",
            ),
            Link(
                href="/static/css/base.css",
                rel="stylesheet",
            ),
            Script(
                src="https://kit.fontawesome.com/605ae70237.js", crossorigin="anonymous"
            ),
            Script(src="/static/js/htmx.js", crossorigin="anonymous"),
        ),
        Body(
            layout,
            hx_boost="true",
        ),
    )
