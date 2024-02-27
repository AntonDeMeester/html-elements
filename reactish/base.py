from abc import ABC
from typing import Any, ClassVar, Protocol, TypeVar

Style = dict[str, str]
Aria = dict[str, str]
HtmlClass = list[str] | str

T = TypeVar("T")


def listify(value: list[T] | T) -> list[T]:
    if isinstance(value, list):
        return value
    return [value]


def listify_or_none(value: list[T] | T | None) -> list[T] | None:
    if value is None:
        return None
    return listify(value)


class Component(Protocol):
    class_name: list[str]

    def to_html(self) -> str:
        ...


class BaseComponent(ABC):
    html_tag: str
    extra_attrs: ClassVar[list[str]] = []

    def __init__(
        self,
        *components: "Component",
        style: Style | None = None,
        aria: Aria | None = None,
        class_name: HtmlClass | None = None,
        id: str | None = None,
        **kwargs: Any,
    ):
        self.components = components
        self.style = style
        self.aria = aria
        self.class_name = listify_or_none(class_name) or []
        self.id = id
        self.kwargs = kwargs

    def to_html(self, indent=0, indent_step=2, format=True) -> str:
        # https://github.com/justpy-org/justpy/blob/master/justpy/htmlcomponents.py#L459C5-L474C17
        block_indent = " " * indent if format else ""
        endline = "\n" if format else ""
        html_string = f"{block_indent}<{self.html_tag}"

        for attr, value in self.attrs().items():
            if value is None:
                continue
            if isinstance(value, bool):
                if value:
                    # So `disabled`, `defer` etc are properly set
                    html_string += f" {attr}"
            else:
                html_string += f' {attr}="{value}"'

        if self.components:
            html_string += f">{endline}"
            new_indent_amount = indent + indent_step
            for c in self.components:
                if isinstance(c, BaseComponent):
                    html_string += c.to_html(indent=new_indent_amount, indent_step=indent_step, format=format)
                else:
                    new_indent = " " * new_indent_amount
                    html_string += f"{new_indent}{c}{endline}"
            html_string += f"{block_indent}</{self.html_tag}>{endline}"
        else:
            html_string += f"></{self.html_tag}>{endline}"

        return html_string

    def attrs(self) -> dict[str, str]:
        attrs = {}
        if self.style is not None:
            attrs["style"] = "; ".join(f"{key}: {value}" for key, value in self.style.items())
        if self.aria is not None:
            for key, value in self.aria.items():
                attrs[f"aria-{key}"] = value
        if self.class_name:
            attrs["class"] = " ".join(self.class_name)
        if self.id is not None:
            attrs["id"] = self.id
        for key, value in self.kwargs.items():
            if value is None:
                continue
            attrs[key.replace("_", "-")] = str(value)
        for key in self.extra_attrs:
            # Allow for `for_` to be parsed  as `for`
            value = getattr(self, key)
            if value is None or value == "":
                continue
            real_key = key if not key.endswith("_") else key[:-1]
            attrs[real_key] = value
        return attrs


class Body(BaseComponent):
    html_tag = "body"


class Page(BaseComponent):
    html_tag = "html"

    def to_html(self, indent=0, indent_step=2, format=True) -> str:
        html = super().to_html(indent=indent, indent_step=indent_step, format=format)
        return "<!DOCTYPE html>\n" + html
