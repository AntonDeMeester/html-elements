from typing import TypedDict

from fastapi.datastructures import URL
from reactish import components as c


def Icon(icon: str, fa_group: str, **kwargs) -> c.BaseComponent:
    return c.Span(c.I(class_name=f"fa-{fa_group} fa-{icon}"), class_name="icon", **kwargs)


def Tooltip(component: c.BaseComponent, tooltip_text: str) -> c.BaseComponent:
    return c.Div(component, c.Span(tooltip_text, class_name="tooltiptext"), class_name="tooltip")


def Tag(text: str, color: str = "") -> c.BaseComponent:
    return c.Span(text, class_name=f"tag is-{color}" if color else "tag")


class TabData(TypedDict):
    label: str
    value: str


def Tabs(
    tabs: list[TabData],
    selected: str | None = None,
    base: URL | None = None,
    **kwargs: str,
) -> c.BaseComponent:
    elements: list[c.BaseComponent] = []
    for tab in tabs:
        href = None
        if base:
            href = base.replace(path=f"{base.path}/{tab['value']}")
        elements.append(
            c.Li(
                c.A(tab["label"], href=href),
                class_name="is-active" if selected == tab["value"] else None,
            )
        )
    return c.Div(c.Ul(*elements), class_name=["tabs", "is-narrow", "row"], **kwargs)


def Notification(
    content: str | c.BaseComponent,
    *,
    icon: str | None = None,
    icon_group: str | None = None,
    has_delete: bool = False,
    color: str | None = None,
    is_light: bool = False,
) -> c.BaseComponent:
    elements: list[c.BaseComponent | str] = []
    classes = ["notification"]
    if color:
        classes.append(color)
    if is_light:
        classes.append("is-light")
    if has_delete:
        elements.append(c.Button(class_name=["delete"]))
    if icon:
        elements.append(
            Icon(
                icon,
                icon_group,
            )
        )
    elements.append(content)
    return c.Div(
        *elements,
        class_name=classes,
        style={"padding": "0.25rem", "font-size": "small", "margin-bottom": "0.5rem"},
    )
