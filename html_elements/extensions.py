from abc import ABC
from typing import Literal, Type

from .base import BaseHtmlElement, HtmlAttribute


def add_extension(extension: Type["BaseHtmlElement"], base: Type["BaseHtmlElement"] = BaseHtmlElement) -> None:
    """
    Adds the HTML attributes of this extension to all subclasses so that they are included
    This allows more than the MDN attributes to be included in the output HTML
    #TODO Allow for proper typing of extensions
    """
    for subcls in base.__html_subclasses__:
        subcls.__html_attributes__ |= extension.__html_attributes__


TrueFalse = Literal["true", "false"]
HxSwap = Literal["innerHTML", "outerHTML", "beforebegin", "afterbegin", "beforeend", "afterend", "delete", "none"]


class HtmxExtension(BaseHtmlElement, ABC):
    # Core attributes
    hx_get: str | None = HtmlAttribute(default=None, html_attribute="hx-get")
    hx_post: str | None = HtmlAttribute(default=None, html_attribute="hx-post")
    hx_on: dict[str, str] = HtmlAttribute(default_factory=dict, html_attribute="hx-on", multi_attribute=True)
    hx_push_url: TrueFalse | None = HtmlAttribute(default=None, html_attribute="hx-push-url")
    hx_select: str | None = HtmlAttribute(default=None, html_attribute="hx-select")
    hx_select_oob: str | None = HtmlAttribute(default=None, html_attribute="hx-select-oob")
    hx_swap: HxSwap | None = HtmlAttribute(default=None, html_attribute="hx-swap")
    hx_swap_oob: str | None = HtmlAttribute(default=None, html_attribute="hx-swap-oob")
    hx_target: str | None = HtmlAttribute(default=None, html_attribute="hx-target")
    hx_trigger: str | None = HtmlAttribute(default=None, html_attribute="hx-trigger")
    hx_vals: str | None = HtmlAttribute(default=None, html_attribute="hx-vals")

    # Additional attributes
    hx_boost: TrueFalse | None = HtmlAttribute(default=None, html_attribute="hx-boost")
    hx_confirm: str | None = HtmlAttribute(default=None, html_attribute="hx-confirm")
    hx_delete: str | None = HtmlAttribute(default=None, html_attribute="hx-delete")
    hx_disable: bool | None = HtmlAttribute(default=None, html_attribute="hx-disable")
    hx_disabled_elt: str | None = HtmlAttribute(default=None, html_attribute="hx-disabled-elt")
    hx_disinherit: str | None = HtmlAttribute(default=None, html_attribute="hx-disinherit")
    hx_encoding: str | None = HtmlAttribute(default=None, html_attribute="hx-encoding")
    hx_ext: str | None = HtmlAttribute(default=None, html_attribute="hx-ext")
    hx_headers: str | None = HtmlAttribute(default=None, html_attribute="hx-headers")
    hx_history: TrueFalse | None = HtmlAttribute(default=None, html_attribute="hx-history")
    hx_history_elt: bool | None = HtmlAttribute(default=None, html_attribute="hx-history-elt")
    hx_include: str | None = HtmlAttribute(default=None, html_attribute="hx-include")
    hx_indicator: str | None = HtmlAttribute(default=None, html_attribute="hx-indicator")
    hx_params: str | None = HtmlAttribute(default=None, html_attribute="hx-params")
    hx_patch: str | None = HtmlAttribute(default=None, html_attribute="hx-patch")
    hx_preserve: bool | None = HtmlAttribute(default=None, html_attribute="hx-preserve")
    hx_prompt: str | None = HtmlAttribute(default=None, html_attribute="hx-prompt")
    hx_put: str | None = HtmlAttribute(default=None, html_attribute="hx-put")
    hx_replace_url: TrueFalse | None = HtmlAttribute(default=None, html_attribute="hx-replace-url")
    hx_request: str | None = HtmlAttribute(default=None, html_attribute="hx-request")
    hx_sse: str | None = HtmlAttribute(default=None, html_attribute="hx-sse")
    hx_sync: str | None = HtmlAttribute(default=None, html_attribute="hx-sync")
    hx_validate: TrueFalse | None = HtmlAttribute(default=None, html_attribute="hx-validate")
    hx_vars: str | None = HtmlAttribute(default=None, html_attribute="hx-vars")
    hx_ws: str | None = HtmlAttribute(default=None, html_attribute="hx-ws")
