from abc import ABC

from reactish import elements as e
from reactish.base import BaseHtmlComponent, HtmlAttribute


class HtmxExtension(BaseHtmlComponent, ABC):
    hx_get: str = HtmlAttribute(html_attribute="hx-get", default=None)


class BetterA(HtmxExtension, e.A):
    pass


class BetterDiv(HtmxExtension, e.A):
    pass

def test_add_simple_extension():
    BaseHtmlComponent.add_extension(HtmxExtension)
    field = e.Div([e.P(["Test"])], hx_get="false", classes=["test"])
    assert field.to_html(format=False) == '<div hx-get="false"><p>Test</p></div>'

def test_better_a():
    a = BetterA(hx_get="a")
    b = BetterDiv(["test", "test"], hx_get="/test")
    b.to_html()
    a.to_html()
