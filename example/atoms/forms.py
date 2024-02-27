from typing import Any, TypedDict

from reactish import components as c
from reactish.base import Component


def FormField(
    type: str,
    label: str | None = None,
    name: str | None = None,
    placeholder: str | None = None,
    value: Any | None = None,
    **kwargs: Any,
) -> Component:
    elements = []
    if label:
        elements.append(c.Label(label, class_name="label"))
    elements.append(
        c.Div(
            c.Input(
                class_name="input",
                type=type,
                name=name,
                placeholder=placeholder,
                value=value,
                id=f"form-{name}",
                **kwargs,
            ),
            class_name="control is-fullwidth",
        )
    )
    return c.Div(
        *elements,
        class_name="field",
    )


class Option(TypedDict):
    label: str
    value: Any


def FormSelect(
    options: list[Option],
    label: str | None = None,
    selected: list[str] | None = None,
    hx_get: str | None = None,
    name: str | None = None,
    allow_none: bool = False,
    **kwargs: Any,
) -> Component:
    html_options = [
        c.Option(
            opt["label"],
            value=opt["value"],
            selected=any(v == opt["value"] for v in (selected or [])),
            # selected=selected == opt["value"],
        )
        for opt in options
    ]
    if allow_none:
        html_options.insert(
            0,
            c.Option(
                "Clear",
                value="",
                onclick=f"""
            const elements = document.getElementById('{name}').getElementsByTagName('option');
            for(const el of elements) {{
                el.selected = false;
            }}
        """,
            ),
        )
    elements = []
    if label:
        elements.append(c.Label(label, class_name="label"))
    elements.append(
        c.Div(
            c.Select(
                *html_options,
                multiple=False,
                id=name,
                name=name,
                hx_get=hx_get,
                **kwargs,
            ),
            class_name="select is-fullwidth",
        ),
    )
    return c.Div(
        *elements,
        class_name="control block",
    )


def FormMultiSelect(
    label: str,
    options: list[Option],
    selected: list[str] | None = None,
    hx_get: str | None = None,
    name: str | None = None,
    allow_none: bool = False,
) -> Component:
    html_options = [
        c.Option(
            opt["label"],
            value=opt["value"],
            selected=any(v == opt["value"] for v in (selected or [])),
            # selected=selected == opt["value"],
        )
        for opt in options
    ]
    if allow_none:
        html_options.insert(
            0,
            c.Option(
                "Clear",
                value="",
                onclick=f"""
            const elements = document.getElementById('{name}').getElementsByTagName('option');
            for(const el of elements) {{
                el.selected = false;
            }}
        """,
            ),
        )
    classes = ["select", "is-multiple", "is-fullwidth"]
    if len(selected) == 0:
        shown_value = "None selected"
    elif len(selected) == 1:
        shown_value = selected[0]
    else:
        shown_value = f"Multiple selected ({len(selected)})"
    return c.Div(
        c.Label(label, class_name="label"),
        c.Div(
            c.Select(
                # c.Option(shown_value, selected=True),
                *html_options,
                id=name,
                name=name,
                hx_get=hx_get,
                multiple=True,
            ),
            # c.Div(
            #     c.Ul(
            #         *[c.Li(c.Input(opt["label"], type="checkbox", value=opt["value"])) for opt in options]
            #     ),
            #     class_name="dropdown",
            # ),
            class_name=classes,
            # onclick="""event.currentTarget.classList.toggle('open');""",
        ),
        class_name="control block",
    )


def LabeledField(
    label: str,
    value: Any | None = None,
) -> Component:
    return c.Div(
        c.Label(label, class_name="label"),
        c.Div(value),
        class_name="field",
    )


def ComplexForm(*fields: Component) -> Component:
    return c.Form(
        *fields,
        c.Input(class_name="button", type="submit", value="submit"),
    )


def CombinedFormField(*fields: c.BaseComponent, label: str | None = None) -> c.BaseComponent:
    elements = []
    if label:
        elements.append(c.Label(label, class_name="label"))
    elements.append(
        c.Div(
            *fields,
            class_name=[
                "field",
                "has-addons",
            ],
        )
    )
    return c.Div(*elements)


def TextAreaFormField(
    label: str | None = None,
    name: str | None = None,
    placeholder: str | None = None,
    value: Any | None = None,
    **kwargs: Any,
) -> Component:
    elements = []
    if label:
        elements.append(c.Label(label, class_name="label"))
    elements.append(
        c.Div(
            c.TextArea(
                value,
                name=name,
                placeholder=placeholder,
                class_name=["textarea"],
                **kwargs,
            ),
            class_name="control is-fullwidth",
        )
    )
    return c.Div(
        *elements,
        class_name="field",
    )
