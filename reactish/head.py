from typing import Any

from .base import BaseComponent


class Head(BaseComponent):
    html_tag = "head"


class Body(BaseComponent):
    html_tag = "body"


class Script(BaseComponent):
    html_tag = "script"
    extra_attrs = ["src", "defer", "crossorigin"]

    def __init__(
        self, *args: Any, src: str | None = None, defer: bool | None = None, crossorigin: str | None = None, **kwargs: Any
    ):
        super().__init__(*args, **kwargs)
        self.src = src
        self.defer = defer
        self.crossorigin = crossorigin


class Link(BaseComponent):
    html_tag = "link"
    extra_attrs = ["rel", "href"]

    def __init__(self, *args: Any, rel: str | None = None, href: str | None = None, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.rel = rel
        self.href = href


class Meta(BaseComponent):
    html_tag = "meta"
    extra_attrs = ["charset", "name", "content"]

    def __init__(
        self, *args: Any, charset: str | None = None, name: str | None = None, content: str | None = None, **kwargs: Any
    ):
        super().__init__(*args, **kwargs)
        self.charset = charset
        self.name = name
        self.content = content


class Title(BaseComponent):
    html_tag = "title"
