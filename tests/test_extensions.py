from abc import ABC

from html_elements.base import BaseHtmlElement, HtmlAttribute
from html_elements.extensions import HtmxExtension, add_extension


class Baseline(BaseHtmlElement, tag="base"):
    field: str | None = HtmlAttribute(default=None)


class Extension(BaseHtmlElement, ABC):
    extra: str | None = HtmlAttribute(default=None)


def test_add_extension():
    add_extension(Extension)
    c = Baseline(extra="hello")  # type: ignore
    assert c.to_html(format=False) == '<base extra="hello"></base>'


def test_htmx_extension():
    add_extension(HtmxExtension)
    c = Baseline(
        hx_get="get",  # type: ignore
        hx_post="post",  # type: ignore
        hx_on={"click": "do", "test": "something"},  # type: ignore
        hx_push_url="true",  # type: ignore
        hx_select="this",  # type: ignore
        hx_select_oob="this",  # type: ignore
        hx_swap="innerHTML",  # type: ignore
        hx_swap_oob="this",  # type: ignore
        hx_target="this",  # type: ignore
        hx_trigger="this",  # type: ignore
        hx_vals="something",  # type: ignore
        hx_boost="true",  # type: ignore
        hx_confirm="please",  # type: ignore
        hx_delete="there",  # type: ignore
        hx_disable=True,  # type: ignore
        hx_disabled_elt="please",  # type: ignore
        hx_disinherit="true",  # type: ignore
        hx_encoding="nice",  # type: ignore
        hx_ext="test",  # type: ignore
        hx_headers="test",  # type: ignore
        hx_history="true",  # type: ignore
        hx_history_elt=True,  # type: ignore
        hx_include="name",  # type: ignore
        hx_indicator="#test",  # type: ignore
        hx_params="hello",  # type: ignore
        hx_patch="there",  # type: ignore
        hx_preserve="please",  # type: ignore
        hx_prompt="nooo",  # type: ignore
        hx_put="there",  # type: ignore
        hx_replace_url="true",  # type: ignore
        hx_request="there",  # type: ignore
        hx_sse="deprecated",  # type: ignore
        hx_sync="there",  # type: ignore
        hx_validate="true",  # type: ignore
        hx_vars="some",  # type: ignore
        hx_ws="deprecated",  # type: ignore
    )
    assert (
        c.to_html(format=False)
        == '<base hx-get="get" hx-post="post" hx-on-click="do" hx-on-test="something" hx-push-url="true" hx-select="this" hx-select-oob="this" hx-swap="innerHTML" hx-swap-oob="this" hx-target="this" hx-trigger="this" hx-vals="something" hx-boost="true" hx-confirm="please" hx-delete="there" hx-disable hx-disabled-elt="please" hx-disinherit="true" hx-encoding="nice" hx-ext="test" hx-headers="test" hx-history="true" hx-history-elt hx-include="name" hx-indicator="#test" hx-params="hello" hx-patch="there" hx-preserve="please" hx-prompt="nooo" hx-put="there" hx-replace-url="true" hx-request="there" hx-sse="deprecated" hx-sync="there" hx-validate="true" hx-vars="some" hx-ws="deprecated"></base>'
    )
