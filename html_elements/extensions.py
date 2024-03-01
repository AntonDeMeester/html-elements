from abc import ABC
from typing import Dict, Literal, Type, Union

from .base import BaseHtmlElement, HtmlAttribute


def add_extension(extension: Type["BaseHtmlElement"], base: Type["BaseHtmlElement"] = BaseHtmlElement) -> None:
    """
    Adds the HTML attributes of this extension to all subclasses so that they are included
    This allows more than the MDN attributes to be included in the output HTML
    #TODO Allow for proper typing of extensions
    """
    for subcls in base.__html_subclasses__:
        subcls.__html_attributes__.update(extension.__html_attributes__)


TrueFalse = Literal["true", "false"]
HxSwap = Literal["innerHTML", "outerHTML", "beforebegin", "afterbegin", "beforeend", "afterend", "delete", "none"]


class HtmxExtension(BaseHtmlElement, ABC):
    # Core attributes
    hx_get: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-get")
    hx_post: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-post")
    hx_on: Dict[str, str] = HtmlAttribute(default_factory=dict, html_attribute="hx-on", multi_attribute=True)
    hx_push_url: Union[TrueFalse, None] = HtmlAttribute(default=None, html_attribute="hx-push-url")
    hx_select: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-select")
    hx_select_oob: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-select-oob")
    hx_swap: Union[HxSwap, None] = HtmlAttribute(default=None, html_attribute="hx-swap")
    hx_swap_oob: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-swap-oob")
    hx_target: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-target")
    hx_trigger: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-trigger")
    hx_vals: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-vals")

    # Additional attributes
    hx_boost: Union[TrueFalse, None] = HtmlAttribute(default=None, html_attribute="hx-boost")
    hx_confirm: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-confirm")
    hx_delete: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-delete")
    hx_disable: Union[bool, None] = HtmlAttribute(default=None, html_attribute="hx-disable")
    hx_disabled_elt: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-disabled-elt")
    hx_disinherit: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-disinherit")
    hx_encoding: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-encoding")
    hx_ext: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-ext")
    hx_headers: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-headers")
    hx_history: Union[TrueFalse, None] = HtmlAttribute(default=None, html_attribute="hx-history")
    hx_history_elt: Union[bool, None] = HtmlAttribute(default=None, html_attribute="hx-history-elt")
    hx_include: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-include")
    hx_indicator: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-indicator")
    hx_params: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-params")
    hx_patch: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-patch")
    hx_preserve: Union[bool, None] = HtmlAttribute(default=None, html_attribute="hx-preserve")
    hx_prompt: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-prompt")
    hx_put: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-put")
    hx_replace_url: Union[TrueFalse, None] = HtmlAttribute(default=None, html_attribute="hx-replace-url")
    hx_request: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-request")
    hx_sse: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-sse")
    hx_sync: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-sync")
    hx_validate: Union[TrueFalse, None] = HtmlAttribute(default=None, html_attribute="hx-validate")
    hx_vars: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-vars")
    hx_ws: Union[str, None] = HtmlAttribute(default=None, html_attribute="hx-ws")
