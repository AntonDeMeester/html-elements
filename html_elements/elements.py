from abc import ABC
from typing import Any, Dict, List, Literal, Union

from .base import BaseHtmlElement, HtmlAttribute, HtmlMetaClass

TrueFalse = Literal["true", "false"]
TrueFalseEmpty = Union[Literal[""], TrueFalse]
ContentEditable = Union[TrueFalse, Literal["plaintext-only"]]
AutoCapitalize = Literal["none", "off", "sentences", "on", "words", "characters"]
Dir = Literal["ltr", "rtl", "auto"]
EnterKeyHint = Literal["enter", "done", "go", "next", "previous", "search", "send"]
Hidden = Union[bool, Literal["", "hidden", "until-found"]]
Inputmode = Literal["none", "text", "decimal", "numeric", "tel", "search", "email", "url"]
Translate = Literal["", "yes", "no"]
VirtualKeyboardPolicy = Literal["", "auto", "manual"]

ReferrerPolicy = Literal[
    "no-referrer",
    "no-referrer-when-downgrade",
    "origin",
    "origin-when-cross-origin",
    "same-origin",
    "strict-origin",
    "strict-origin-when-cross-origin",
    "unsafe-url",
]
Target = Union[str, Literal["_self", "_blank", "_parent", "_top"]]
Shape = Union[str, Literal["rect", "circle", "default", "poly"]]
ControlsList = Union[str, Literal["nodownload", "nofullscreen", "noremoteplayback"]]
CrossOrigin = Literal["anonymous", "use-credentials"]
Preload = Literal["", "none", "metadata", "auto"]
ButtonType = Union[str, Literal["submit", "reset", "button"]]
AutoComplete = Union[
    str,
    Literal[
        "on",
        "off",
        "name",
        "honorific-prefix",
        "given-name",
        "additional-name",
        "family-name",
        "honorary-suffix",
        "nickname",
        "email",
        "username",
        "new-password",
        "current-password",
        "one-time-code",
        "organization-title",
        "organization",
        "street-address",
        "shipping",
        "billing",
        "address-line1",
        "address-line2",
        "address-line3",
        "address-level4",
        "address-level3",
        "address-level2",
        "address-level1",
        "country",
        "country-name",
        "postal-code",
        "cc-name",
        "cc-additional-name",
        "cc-family-name",
        "cc-number",
        "cc-exp",
        "cc-exp-month",
        "cc-exp-year",
        "cc-csc",
        "cc-type",
        "transaction-currency",
        "transaction-amount",
        "language",
        "bday",
        "bday-day",
        "bday-month",
        "bday-year",
        "sex",
        "tel",
        "tel-country-code",
        "tel-national",
        "tel-area-code",
        "tel-local",
        "tel-extension",
        "impp",
        "url",
        "photo",
        "webauthn",
    ],
]
Loading = Union[str, Literal["eager", "lazy"]]
Sandbox = Literal[
    "allow-downloads",
    "allow-downloads-without-user-activation",
    "allow-forms",
    "allow-modals",
    "allow-orientation-lock",
    "allow-pointer-lock",
    "allow-popups",
    "allow-popups-to-escape-sandbox",
    "allow-presentation",
    "allow-same-origin",
    "allow-scripts",
    "allow-storage-access-by-user-activation",
    "allow-top-navigation",
    "allow-navigation-by-user-activation",
    "allow-top-navigation-to-custom-protocols",
]
Decoding = Literal["sync", "async", "auto"]
FetchPriority = Literal["high", "low", "auto"]
PopoverTargetAction = Literal["hide", "show", "toggle"]
InputType = Union[
    Literal[
        "button",
        "checkbox",
        "color",
        "date",
        "datetime-local",
        "email",
        "file",
        "hidden",
        "image",
        "month",
        "number",
        "password",
        "radio",
        "range",
        "reset",
        "search",
        "submit",
        "tel",
        "text",
        "time",
        "url",
        "week",
    ],
    str,
]
ListType = Literal["a", "A", "i", "I", "1"]
Blocking = Union[str, Literal["render"]]
ScriptType = Union[str, Literal["importmap", "module", "speculationrules"]]
ShadowRootMode = Union[str, Literal["open", "closed"]]
Spellcheck = Union[str, Literal["true", "default", "false"]]
Wrap = Union[str, Literal["hard", "soft"]]
ThScope = Union[str, Literal["row", "col", "rowgroup", "colgroup"]]
TrackType = Union[str, Literal["subtitles", "captions", "descriptions", "chapters", "metadata"]]


class EventHandlerAttributes(ABC, metaclass=HtmlMetaClass):
    onautocomplete: Union[str, None] = HtmlAttribute(default=None)
    onabort: Union[str, None] = HtmlAttribute(default=None)
    onautocompleteerror: Union[str, None] = HtmlAttribute(default=None)
    onblur: Union[str, None] = HtmlAttribute(default=None)
    oncancel: Union[str, None] = HtmlAttribute(default=None)
    oncanplay: Union[str, None] = HtmlAttribute(default=None)
    oncanplaythrough: Union[str, None] = HtmlAttribute(default=None)
    onchange: Union[str, None] = HtmlAttribute(default=None)
    onclick: Union[str, None] = HtmlAttribute(default=None)
    onclose: Union[str, None] = HtmlAttribute(default=None)
    oncontextmenu: Union[str, None] = HtmlAttribute(default=None)
    oncuechange: Union[str, None] = HtmlAttribute(default=None)
    ondblclick: Union[str, None] = HtmlAttribute(default=None)
    ondrag: Union[str, None] = HtmlAttribute(default=None)
    ondragend: Union[str, None] = HtmlAttribute(default=None)
    ondragenter: Union[str, None] = HtmlAttribute(default=None)
    ondragleave: Union[str, None] = HtmlAttribute(default=None)
    ondragover: Union[str, None] = HtmlAttribute(default=None)
    ondragstart: Union[str, None] = HtmlAttribute(default=None)
    ondrop: Union[str, None] = HtmlAttribute(default=None)
    ondurationchange: Union[str, None] = HtmlAttribute(default=None)
    onemptied: Union[str, None] = HtmlAttribute(default=None)
    onended: Union[str, None] = HtmlAttribute(default=None)
    onerror: Union[str, None] = HtmlAttribute(default=None)
    onfocus: Union[str, None] = HtmlAttribute(default=None)
    oninput: Union[str, None] = HtmlAttribute(default=None)
    oninvalid: Union[str, None] = HtmlAttribute(default=None)
    onkeydown: Union[str, None] = HtmlAttribute(default=None)
    onkeypress: Union[str, None] = HtmlAttribute(default=None)
    onkeyup: Union[str, None] = HtmlAttribute(default=None)
    onload: Union[str, None] = HtmlAttribute(default=None)
    onloadeddata: Union[str, None] = HtmlAttribute(default=None)
    onloadedmetadata: Union[str, None] = HtmlAttribute(default=None)
    onloadstart: Union[str, None] = HtmlAttribute(default=None)
    onmousedown: Union[str, None] = HtmlAttribute(default=None)
    onmouseenter: Union[str, None] = HtmlAttribute(default=None)
    onmouseleave: Union[str, None] = HtmlAttribute(default=None)
    onmousemove: Union[str, None] = HtmlAttribute(default=None)
    onmouseout: Union[str, None] = HtmlAttribute(default=None)
    onmouseover: Union[str, None] = HtmlAttribute(default=None)
    onmouseup: Union[str, None] = HtmlAttribute(default=None)
    onmousewheel: Union[str, None] = HtmlAttribute(default=None)
    onpause: Union[str, None] = HtmlAttribute(default=None)
    onplay: Union[str, None] = HtmlAttribute(default=None)
    onplaying: Union[str, None] = HtmlAttribute(default=None)
    onprogress: Union[str, None] = HtmlAttribute(default=None)
    onratechange: Union[str, None] = HtmlAttribute(default=None)
    onreset: Union[str, None] = HtmlAttribute(default=None)
    onresize: Union[str, None] = HtmlAttribute(default=None)
    onscroll: Union[str, None] = HtmlAttribute(default=None)
    onseeked: Union[str, None] = HtmlAttribute(default=None)
    onseeking: Union[str, None] = HtmlAttribute(default=None)
    onselect: Union[str, None] = HtmlAttribute(default=None)
    onshow: Union[str, None] = HtmlAttribute(default=None)
    onsort: Union[str, None] = HtmlAttribute(default=None)
    onstalled: Union[str, None] = HtmlAttribute(default=None)
    onsubmit: Union[str, None] = HtmlAttribute(default=None)
    onsuspend: Union[str, None] = HtmlAttribute(default=None)
    ontimeupdate: Union[str, None] = HtmlAttribute(default=None)
    ontoggle: Union[str, None] = HtmlAttribute(default=None)
    onvolumechange: Union[str, None] = HtmlAttribute(default=None)
    onwaiting: Union[str, None] = HtmlAttribute(default=None)


class GlobalHtmlAttributes(ABC, metaclass=HtmlMetaClass):
    aria: Dict[str, Any] = HtmlAttribute(default_factory=dict, multi_attribute=True)
    accesskey: Union[str, None] = HtmlAttribute(default=None)
    autocapitalize: Union[AutoCapitalize, None] = HtmlAttribute(default=None)
    autofocus: Union[bool, None] = HtmlAttribute(default=None)
    classes: List[str] = HtmlAttribute(
        default_factory=list,
        html_attribute="class",
        transformer=lambda x: " ".join(x),
    )
    contenteditable: Union[ContentEditable, None] = HtmlAttribute(default=None)
    contextmenu: Union[str, None] = HtmlAttribute(default=None)
    data: Dict[str, Any] = HtmlAttribute(default=None, multi_attribute=True)
    dir: Union[Dir, None] = HtmlAttribute(default=None)
    draggable: Union[TrueFalse, None] = HtmlAttribute(default=None)
    enterkeyhint: Union[EnterKeyHint, None] = HtmlAttribute(default=None)
    exportparts: Union[str, None] = HtmlAttribute(default=None)
    hidden: Union[Hidden, None] = HtmlAttribute(default=None)
    id: Union[str, None] = HtmlAttribute(default=None)
    inert: Union[bool, None] = HtmlAttribute(default=None)
    inputmode: Inputmode = HtmlAttribute(default=None)
    is_: Union[str, None] = HtmlAttribute(default=None, html_attribute="is")
    itemid: Union[str, None] = HtmlAttribute(default=None)
    itemprop: Union[str, None] = HtmlAttribute(default=None)
    itemref: Union[str, None] = HtmlAttribute(default=None)
    itemscope: Union[bool, None] = HtmlAttribute(default=None)
    itemtype: Union[str, None] = HtmlAttribute(default=None)
    lang: Union[str, None] = HtmlAttribute(default=None)
    nonce: Union[str, None] = HtmlAttribute(default=None)
    part: Union[str, None] = HtmlAttribute(default=None)
    popover: Union[str, None] = HtmlAttribute(default=None)
    role: Union[str, None] = HtmlAttribute(default=None)
    slot: Union[str, None] = HtmlAttribute(default=None)
    spellcheck: Spellcheck = HtmlAttribute(default=None)
    style: Dict[str, str] = HtmlAttribute(
        default_factory=dict,
        transformer=lambda x: "; ".join(f"{key}: {value}" for key, value in x.items()),
    )
    tabindex: Union[int, None] = HtmlAttribute(default=None)
    title: Union[str, None] = HtmlAttribute(default=None)
    translate: Union[Translate, None] = HtmlAttribute(default=None)
    virtualkeyboardpolicy: Union[VirtualKeyboardPolicy, None] = HtmlAttribute(default=None)


class BaseNoChildrenHtmlElement(
    EventHandlerAttributes,
    GlobalHtmlAttributes,
    BaseHtmlElement,
    ABC,
):
    pass


class BaseChildrenHtmlElement(BaseNoChildrenHtmlElement, ABC):
    children: List[Union[str, BaseHtmlElement]] = HtmlAttribute(default_factory=list, kw_only=False, attribute_type="content")


class A(BaseChildrenHtmlElement, tag="a"):
    download: Union[str, None] = HtmlAttribute(default=None)
    href: Union[str, None] = HtmlAttribute(default=None)
    hreflang: Union[str, None] = HtmlAttribute(default=None)
    ping: List[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    referrerpolicy: Union[ReferrerPolicy, None] = HtmlAttribute(default=None)
    ref: List[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    target: Target = HtmlAttribute(default=None)
    type: Union[str, None] = HtmlAttribute(default=None)


class Abbr(BaseChildrenHtmlElement, tag="abbr"):
    pass


class Address(BaseChildrenHtmlElement, tag="address"):
    pass


class Area(BaseNoChildrenHtmlElement, tag="area", tag_omission=True):
    alt: Union[str, None] = HtmlAttribute(default=None)
    coords: Union[str, None] = HtmlAttribute(default=None)
    download: Union[str, None] = HtmlAttribute(default=None)
    href: Union[str, None] = HtmlAttribute(default=None)
    ping: List[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    referrerpolicy: Union[ReferrerPolicy, None] = HtmlAttribute(default=None)
    rel: Union[str, None] = HtmlAttribute(default=None)
    shape: Shape = HtmlAttribute(default=None)
    target: Target = HtmlAttribute(default=None)
    value: Union[str, None] = HtmlAttribute(default=None)


class Article(BaseChildrenHtmlElement, tag="article"):
    height: Union[str, None] = HtmlAttribute(default=None)
    width: Union[str, None] = HtmlAttribute(default=None)


class Aside(BaseChildrenHtmlElement, tag="aside"):
    pass


class Audio(BaseChildrenHtmlElement, tag="audio"):
    autoplay: Union[bool, None] = HtmlAttribute(default=None)
    controls: Union[bool, None] = HtmlAttribute(default=None)
    controlslist: List[ControlsList] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    crossorigin: Union[CrossOrigin, None] = HtmlAttribute(default=None)
    disableremoteplayback: Union[bool, None] = HtmlAttribute(default=None)
    loop: Union[bool, None] = HtmlAttribute(default=None)
    muted: Union[bool, None] = HtmlAttribute(default=None)
    preload: Preload = HtmlAttribute(default=None)
    src: Union[str, None] = HtmlAttribute(default=None)


class B(BaseChildrenHtmlElement, tag="b"):
    pass


class Base(BaseNoChildrenHtmlElement, tag="base", tag_omission=True):
    href: str = HtmlAttribute(default=None)
    target: Target = HtmlAttribute(default=None)


class Bdi(BaseChildrenHtmlElement, tag="bdi"):
    pass


class Bdo(BaseChildrenHtmlElement, tag="bdo"):
    pass


class Blockquote(BaseChildrenHtmlElement, tag="blockquote"):
    cite: Union[str, None] = HtmlAttribute(default=None)


class Body(BaseChildrenHtmlElement, tag="body"):
    onafterprint: Union[str, None] = HtmlAttribute(default=None)
    onbeforeprint: Union[str, None] = HtmlAttribute(default=None)
    onbeforeunload: Union[str, None] = HtmlAttribute(default=None)
    onhashchange: Union[str, None] = HtmlAttribute(default=None)
    onlanguagechange: Union[str, None] = HtmlAttribute(default=None)
    onmessage: Union[str, None] = HtmlAttribute(default=None)
    onoffline: Union[str, None] = HtmlAttribute(default=None)
    ononline: Union[str, None] = HtmlAttribute(default=None)
    onpopstate: Union[str, None] = HtmlAttribute(default=None)
    onredo: Union[str, None] = HtmlAttribute(default=None)
    onstorage: Union[str, None] = HtmlAttribute(default=None)
    onundo: Union[str, None] = HtmlAttribute(default=None)
    onunload: Union[str, None] = HtmlAttribute(default=None)


class Br(BaseNoChildrenHtmlElement, tag="br", tag_omission=True):
    pass


class Button(BaseChildrenHtmlElement, tag="button"):
    autofocus: Union[bool, None] = HtmlAttribute(default=None)
    disable: Union[bool, None] = HtmlAttribute(default=None)
    form: Union[str, None] = HtmlAttribute(default=None)
    formaction: Union[str, None] = HtmlAttribute(default=None)
    formenctype: Union[str, None] = HtmlAttribute(default=None)
    formmethod: Union[str, None] = HtmlAttribute(default=None)
    formnovalidate: Union[bool, None] = HtmlAttribute(default=None)
    formtarget: Union[Target, None] = HtmlAttribute(default=None)
    name: Union[str, None] = HtmlAttribute(default=None)
    popovertarget: Union[str, None] = HtmlAttribute(default=None)
    popovertargetaction: Union[str, None] = HtmlAttribute(default=None)
    type: ButtonType = HtmlAttribute(default=None)


class Canvas(BaseChildrenHtmlElement, tag="canvas"):
    pass


class Caption(BaseChildrenHtmlElement, tag="caption", tag_omission=True):
    pass


class Cite(BaseChildrenHtmlElement, tag="cite"):
    pass


class Code(BaseChildrenHtmlElement, tag="code"):
    pass


class Col(BaseNoChildrenHtmlElement, tag="col", tag_omission=True):
    span: Union[int, None] = HtmlAttribute(default=None)


class Colgroup(BaseChildrenHtmlElement, tag="colgroup", tag_omission=True):
    span: Union[int, None] = HtmlAttribute(default=None)


class Data(BaseChildrenHtmlElement, tag="data"):
    value: Any = HtmlAttribute(default=None)


class Datalist(BaseChildrenHtmlElement, tag="datalist"):
    pass


class Dd(BaseChildrenHtmlElement, tag="dd", tag_omission=True):
    pass


class Del(BaseChildrenHtmlElement, tag="del"):
    cite: Union[str, None] = HtmlAttribute(default=None)
    datetime: Union[str, None] = HtmlAttribute(default=None)


class Details(BaseChildrenHtmlElement, tag="details"):
    open: Union[bool, None] = HtmlAttribute(default=None)


class Dfn(BaseChildrenHtmlElement, tag="dfn"):
    pass


class Dialog(BaseChildrenHtmlElement, tag="dialog"):
    open: Union[bool, None] = HtmlAttribute(default=None)


class Div(BaseChildrenHtmlElement, tag="div"):
    pass


class Dl(BaseChildrenHtmlElement, tag="dl"):
    pass


class Dt(BaseChildrenHtmlElement, tag="dt", tag_omission=True):
    pass


class Em(BaseChildrenHtmlElement, tag="em"):
    pass


class Embed(BaseNoChildrenHtmlElement, tag="embed", tag_omission=True):
    height: Union[str, None] = HtmlAttribute(default=None)
    src: Union[str, None] = HtmlAttribute(default=None)
    type: Union[str, None] = HtmlAttribute(default=None)
    width: Union[str, None] = HtmlAttribute(default=None)


class Fieldset(BaseChildrenHtmlElement, tag="fieldset"):
    disabled: Union[bool, None] = HtmlAttribute(default=None)
    form: Union[str, None] = HtmlAttribute(default=None)
    name: Union[str, None] = HtmlAttribute(default=None)


class Figcaption(BaseChildrenHtmlElement, tag="figcaption"):
    pass


class Figure(BaseChildrenHtmlElement, tag="figure"):
    pass


class Footer(BaseChildrenHtmlElement, tag="footer"):
    pass


class Form(BaseChildrenHtmlElement, tag="form"):
    accept_charset: Union[str, None] = HtmlAttribute(default=None, html_attribute="accept-charset")
    autocomplete: AutoComplete = HtmlAttribute(default=None)
    name: Union[str, None] = HtmlAttribute(default=None)
    rel: Union[str, None] = HtmlAttribute(default=None)

    action: Union[str, None] = HtmlAttribute(default=None)
    enctype: Union[str, None] = HtmlAttribute(default=None)
    method: Union[str, None] = HtmlAttribute(default=None)
    novalidate: Union[bool, None] = HtmlAttribute(default=None)
    target: Union[Target, None] = HtmlAttribute(default=None)


class H1(BaseChildrenHtmlElement, tag="h1"):
    pass


class H2(BaseChildrenHtmlElement, tag="h2"):
    pass


class H3(BaseChildrenHtmlElement, tag="h3"):
    pass


class H4(BaseChildrenHtmlElement, tag="h4"):
    pass


class H5(BaseChildrenHtmlElement, tag="h5"):
    pass


class H6(BaseChildrenHtmlElement, tag="h6"):
    pass


class Head(BaseChildrenHtmlElement, tag="head", tag_omission=True):
    pass


class Header(BaseChildrenHtmlElement, tag="header"):
    pass


class Hgroup(BaseChildrenHtmlElement, tag="hgroup"):
    pass


class Hr(BaseNoChildrenHtmlElement, tag="hr", tag_omission=True):
    pass


class Html(BaseChildrenHtmlElement, tag="html"):
    xmlms: Union[str, None] = HtmlAttribute(default=None)

    def to_html(self, indent: int = 0, indent_step: int = 2, format: bool = True) -> str:
        html = super().to_html(indent=indent, indent_step=indent_step, format=format)
        newline = "\n" if format else ""
        return f"<!DOCTYPE html>{newline}{html}"


class I(BaseChildrenHtmlElement, tag="i"):  # noqa: E742
    pass


class Iframe(BaseNoChildrenHtmlElement, tag="iframe"):
    allow: Union[str, None] = HtmlAttribute(default=None)
    allowfullscreen: Union[TrueFalse, None] = HtmlAttribute(default=None)
    height: Union[str, None] = HtmlAttribute(default=None)
    loading: Loading = HtmlAttribute(default=None)
    name: Union[str, None] = HtmlAttribute(default=None)
    referrerpolicy: Union[ReferrerPolicy, None] = HtmlAttribute(default=None)
    sandbox: List[Sandbox] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    src: Union[str, None] = HtmlAttribute(default=None)
    srcdoc: Union[str, None] = HtmlAttribute(default=None)
    width: Union[str, None] = HtmlAttribute(default=None)


class Img(BaseChildrenHtmlElement, tag="img"):
    alt: Union[str, None] = HtmlAttribute(default=None)
    crossorigin: Union[CrossOrigin, None] = HtmlAttribute(default=None)
    decoding: Decoding = HtmlAttribute(default=None)
    elementtiming: Union[str, None] = HtmlAttribute(default=None)
    fetchpriority: Union[FetchPriority, None] = HtmlAttribute(default=None)
    height: Union[str, None] = HtmlAttribute(default=None)
    ismap: Union[bool, None] = HtmlAttribute(default=None)
    loading: Loading = HtmlAttribute(default=None)
    referrerpolicy: ReferrerPolicy = HtmlAttribute(default=None)
    sizes: List[str] = HtmlAttribute(default_factory=list, transformer=lambda x: ", ".join(x))
    src: Union[str, None] = HtmlAttribute(default=None)
    srcset: List[str] = HtmlAttribute(default_factory=list, transformer=lambda x: ", ".join(x))
    width: Union[str, None] = HtmlAttribute(default=None)
    usemap: Union[str, None] = HtmlAttribute(default=None)


class Input(BaseNoChildrenHtmlElement, tag="input", tag_omission=True):
    accept: Union[str, None] = HtmlAttribute(default=None)
    alt: Union[str, None] = HtmlAttribute(default=None)
    autocomplete: Union[AutoComplete, None] = HtmlAttribute(default=None)
    capture: Union[str, None] = HtmlAttribute(default=None)
    checked: Union[bool, None] = HtmlAttribute(default=None)
    dirname: Union[str, None] = HtmlAttribute(default=None)
    disabled: Union[bool, None] = HtmlAttribute(default=None)
    form: Union[str, None] = HtmlAttribute(default=None)
    formaction: Union[str, None] = HtmlAttribute(default=None)
    formenctype: Union[str, None] = HtmlAttribute(default=None)
    formmethod: Union[str, None] = HtmlAttribute(default=None)
    formnovalidate: Union[str, None] = HtmlAttribute(default=None)
    formtarget: Target = HtmlAttribute(default=None)
    height: Union[str, None] = HtmlAttribute(default=None)
    list: Union[str, None] = HtmlAttribute(default=None)
    max: Union[int, None] = HtmlAttribute(default=None)
    maxlength: Union[int, None] = HtmlAttribute(default=None)
    min: Union[int, None] = HtmlAttribute(default=None)
    minlength: Union[int, None] = HtmlAttribute(default=None)
    multiple: Union[bool, None] = HtmlAttribute(default=None)
    name: Union[str, None] = HtmlAttribute(default=None)
    pattern: Union[str, None] = HtmlAttribute(default=None)
    placeholder: Union[str, None] = HtmlAttribute(default=None)
    popovertarget: Union[str, None] = HtmlAttribute(default=None)
    popovertargetaction: Union[PopoverTargetAction, None] = HtmlAttribute(default=None)
    readonly: Union[bool, None] = HtmlAttribute(default=None)
    required: Union[bool, None] = HtmlAttribute(default=None)
    size: Union[int, None] = HtmlAttribute(default=None)
    src: Union[str, None] = HtmlAttribute(default=None)
    step: Union[int, None] = HtmlAttribute(default=None)
    type: InputType = HtmlAttribute(default=None)
    value: Any = HtmlAttribute(default=None)
    width: Union[str, None] = HtmlAttribute(default=None)


# TODO Create separate classes for each Input Type with the relevant attributes


class Ins(BaseChildrenHtmlElement, tag="ins"):
    cite: Union[str, None] = HtmlAttribute(default=None)
    datetime: Union[str, None] = HtmlAttribute(default=None)


class Kbd(BaseChildrenHtmlElement, tag="kbd"):
    pass


class Label(BaseChildrenHtmlElement, tag="label"):
    for_: Union[str, None] = HtmlAttribute(default=None, html_attribute="for")


class Legend(BaseChildrenHtmlElement, tag="legend"):
    pass


class Li(BaseChildrenHtmlElement, tag="li", tag_omission=True):
    value: Union[int, None] = HtmlAttribute(default=None)


class Link(BaseNoChildrenHtmlElement, tag="link", tag_omission=True):
    as_: Union[str, None] = HtmlAttribute(default=None, html_attribute="as")
    crossorigin: Union[CrossOrigin, None] = HtmlAttribute(default=None)
    fetchpriority: Union[FetchPriority, None] = HtmlAttribute(default=None)
    href: Union[str, None] = HtmlAttribute(default=None)
    hreflang: Union[str, None] = HtmlAttribute(default=None)
    imagesizes: Union[List[str], None] = HtmlAttribute(default_factory=list, transformer=lambda x: ", ".join(x))
    imagesrcset: Union[List[str], None] = HtmlAttribute(default_factory=list, transformer=lambda x: ", ".join(x))
    integrity: Union[str, None] = HtmlAttribute(default=None)
    media: Union[str, None] = HtmlAttribute(default=None)
    referrerpolicy: Union[ReferrerPolicy, None] = HtmlAttribute(default=None)
    rel: Union[List[str], None] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    sizes: Union[List[str], None] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    type: Union[str, None] = HtmlAttribute(default=None)


class Main(BaseChildrenHtmlElement, tag="main"):
    pass


class Map(BaseChildrenHtmlElement, tag="map"):
    name: Union[str, None] = HtmlAttribute(default=None)


class Mark(BaseChildrenHtmlElement, tag="mark"):
    pass


class Menu(BaseChildrenHtmlElement, tag="menu"):
    pass


class Meta(BaseNoChildrenHtmlElement, tag="meta", tag_omission=True):
    charset: Union[str, None] = HtmlAttribute(default=None)
    content: Union[str, None] = HtmlAttribute(default=None)
    http_equiv: Union[str, None] = HtmlAttribute(default=None, html_attribute="http-equiv")
    name: Union[str, None] = HtmlAttribute(default=None)


class Meter(BaseChildrenHtmlElement, tag="meter"):
    value: Any = HtmlAttribute(default=None)
    min: Union[float, None] = HtmlAttribute(default=None)
    max: Union[float, None] = HtmlAttribute(default=None)
    low: Union[float, None] = HtmlAttribute(default=None)
    high: Union[float, None] = HtmlAttribute(default=None)
    optimum: Union[float, None] = HtmlAttribute(default=None)
    form: Union[str, None] = HtmlAttribute(default=None)


class Nav(BaseChildrenHtmlElement, tag="nav"):
    pass


class Noscript(BaseChildrenHtmlElement, tag="noscript"):
    pass


class Object(BaseChildrenHtmlElement, tag="object"):
    data: Any = HtmlAttribute(default=None)
    form: Union[str, None] = HtmlAttribute(default=None)
    height: Union[str, None] = HtmlAttribute(default=None)
    name: Union[str, None] = HtmlAttribute(default=None)
    type: Union[str, None] = HtmlAttribute(default=None)
    width: Union[str, None] = HtmlAttribute(default=None)


class Ol(BaseChildrenHtmlElement, tag="ol"):
    reversed: Union[bool, None] = HtmlAttribute(default=None)
    start: Union[int, None] = HtmlAttribute(default=None)
    type: ListType = HtmlAttribute(default=None)


class Optgroup(BaseChildrenHtmlElement, tag="optgroup"):
    disabled: Union[bool, None] = HtmlAttribute(default=None)
    label: Union[str, None] = HtmlAttribute(default=None)


class Option(BaseChildrenHtmlElement, tag="option"):
    disabled: Union[bool, None] = HtmlAttribute(default=None)
    label: Union[str, None] = HtmlAttribute(default=None)
    selected: Union[bool, None] = HtmlAttribute(default=None)
    value: Any = HtmlAttribute(default=None)


class Output(BaseChildrenHtmlElement, tag="output"):
    for_: List[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x), html_attribute="for")
    form: Union[str, None] = HtmlAttribute(default=None)
    name: Union[str, None] = HtmlAttribute(default=None)


class P(BaseChildrenHtmlElement, tag="p"):
    pass


class Picture(BaseChildrenHtmlElement, tag="picture"):
    pass


class Portal(BaseChildrenHtmlElement, tag="portal"):
    referrerpolicy: Union[ReferrerPolicy, None] = HtmlAttribute(default=None)
    src: Union[str, None] = HtmlAttribute(default=None)


class Pre(BaseChildrenHtmlElement, tag="pre"):
    pass


class Progress(BaseChildrenHtmlElement, tag="progress"):
    max: Union[float, None] = HtmlAttribute(default=None)
    value: Union[float, None] = HtmlAttribute(default=None)


class Q(BaseChildrenHtmlElement, tag="q"):
    cite: Union[str, None] = HtmlAttribute(default=None)


class Rp(BaseChildrenHtmlElement, tag="rp", tag_omission=True):
    pass


class Rt(BaseChildrenHtmlElement, tag="rt", tag_omission=True):
    pass


class Ruby(BaseChildrenHtmlElement, tag="ruby"):
    pass


class S(BaseChildrenHtmlElement, tag="s"):
    pass


class Samp(BaseChildrenHtmlElement, tag="samp"):
    pass


class Script(BaseChildrenHtmlElement, tag="script"):
    async_: Union[bool, None] = HtmlAttribute(default=None, html_attribute="async")
    blocking: List[Blocking] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    crossorigin: Union[CrossOrigin, None] = HtmlAttribute(default=None)
    defer: Union[bool, None] = HtmlAttribute(default=None)
    fetchpriority: Union[FetchPriority, None] = HtmlAttribute(default=None)
    integrity: Union[str, None] = HtmlAttribute(default=None)
    nomodule: Union[bool, None] = HtmlAttribute(default=None)
    referrerpolicy: Union[ReferrerPolicy, None] = HtmlAttribute(default=None)
    src: Union[str, None] = HtmlAttribute(default=None)
    type: ScriptType = HtmlAttribute(default=None)


class Search(BaseChildrenHtmlElement, tag="search"):
    pass


class Section(BaseChildrenHtmlElement, tag="section"):
    pass


class Select(BaseChildrenHtmlElement, tag="select"):
    autocomplete: Union[AutoComplete, None] = HtmlAttribute(default=None)
    disabled: Union[bool, None] = HtmlAttribute(default=None)
    form: Union[str, None] = HtmlAttribute(default=None)
    multiple: Union[bool, None] = HtmlAttribute(default=None)
    name: Union[str, None] = HtmlAttribute(default=None)
    required: Union[bool, None] = HtmlAttribute(default=None)
    size: Union[int, None] = HtmlAttribute(default=None)


class Slot(BaseChildrenHtmlElement, tag="slot"):
    name: Union[str, None] = HtmlAttribute(default=None)


class Small(BaseChildrenHtmlElement, tag="small"):
    pass


class Source(BaseNoChildrenHtmlElement, tag="source", tag_omission=True):
    type: Union[str, None] = HtmlAttribute(default=None)
    src: Union[str, None] = HtmlAttribute(default=None)
    srcset: List[str] = HtmlAttribute(default_factory=list, transformer=lambda x: ", ".join(x))
    sizes: List[str] = HtmlAttribute(default_factory=list, transformer=lambda x: ", ".join(x))
    media: Union[str, None] = HtmlAttribute(default=None)
    height: Union[str, None] = HtmlAttribute(default=None)
    width: Union[str, None] = HtmlAttribute(default=None)


class Span(BaseChildrenHtmlElement, tag="span"):
    pass


class Strong(BaseChildrenHtmlElement, tag="strong"):
    pass


class Style(BaseChildrenHtmlElement, tag="style"):
    blocking: Union[Blocking, None] = HtmlAttribute(default=None)
    media: Union[str, None] = HtmlAttribute(default=None)


class Sub(BaseChildrenHtmlElement, tag="sub"):
    pass


class Summary(BaseChildrenHtmlElement, tag="summary"):
    pass


class Sup(BaseChildrenHtmlElement, tag="sup"):
    pass


class Table(BaseChildrenHtmlElement, tag="table"):
    pass


class Tbody(BaseChildrenHtmlElement, tag="tbody", tag_omission=True):
    pass


class Td(BaseChildrenHtmlElement, tag="td", tag_omission=True):
    colspan: Union[int, None] = HtmlAttribute(default=None)
    headers: List[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    rowspan: Union[int, None] = HtmlAttribute(default=None)


class Template(BaseChildrenHtmlElement, tag="template"):
    shadowrootmode: ShadowRootMode = HtmlAttribute(default=None)


class Textarea(BaseChildrenHtmlElement, tag="textarea"):
    autocapitalize: Union[AutoCapitalize, None] = HtmlAttribute(default=None)
    autocomplete: Union[AutoComplete, None] = HtmlAttribute(default=None)
    cols: Union[int, None] = HtmlAttribute(default=None)
    dirname: Union[str, None] = HtmlAttribute(default=None)
    disabled: Union[bool, None] = HtmlAttribute(default=None)
    form: Union[str, None] = HtmlAttribute(default=None)
    maxlength: Union[int, None] = HtmlAttribute(default=None)
    minlength: Union[int, None] = HtmlAttribute(default=None)
    name: Union[str, None] = HtmlAttribute(default=None)
    placeholder: Union[str, None] = HtmlAttribute(default=None)
    readonly: Union[bool, None] = HtmlAttribute(default=None)
    required: Union[bool, None] = HtmlAttribute(default=None)
    rows: Union[int, None] = HtmlAttribute(default=None)
    wrap: Union[Wrap, None] = HtmlAttribute(default=None)


class Tfoot(BaseChildrenHtmlElement, tag="tfoot", tag_omission=True):
    pass


class Th(BaseChildrenHtmlElement, tag="th", tag_omission=True):
    abbr: Union[str, None] = HtmlAttribute(default=None)
    colspan: Union[int, None] = HtmlAttribute(default=None)
    headers: List[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    rowspan: Union[int, None] = HtmlAttribute(default=None)
    scope: Union[ThScope, None] = HtmlAttribute(default=None)


class Thead(BaseChildrenHtmlElement, tag="thead", tag_omission=True):
    pass


class Time(BaseChildrenHtmlElement, tag="time"):
    datetime: Union[str, None] = HtmlAttribute(default=None)


class Title(BaseChildrenHtmlElement, tag="title"):
    pass


class Tr(BaseChildrenHtmlElement, tag="tr", tag_omission=True):
    pass


class Track(BaseNoChildrenHtmlElement, tag="track", tag_omission=True):
    default: Union[bool, None] = HtmlAttribute(default=None)
    kind: Union[TrackType, None] = HtmlAttribute(default=None)
    label: Union[str, None] = HtmlAttribute(default=None)
    src: Union[str, None] = HtmlAttribute(default=None)
    srclang: Union[str, None] = HtmlAttribute(default=None)


class U(BaseChildrenHtmlElement, tag="u"):
    pass


class Ul(BaseChildrenHtmlElement, tag="ul"):
    pass


class Var(BaseChildrenHtmlElement, tag="var"):
    pass


class Video(BaseChildrenHtmlElement, tag="video"):
    autoplay: Union[bool, None] = HtmlAttribute(default=None)
    controls: Union[str, None] = HtmlAttribute(default=None)
    controlslist: List[ControlsList] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    crossorigin: Union[CrossOrigin, None] = HtmlAttribute(default=None)
    disablepictureinpicture: Union[bool, None] = HtmlAttribute(default=None)
    disableremoteplayback: Union[bool, None] = HtmlAttribute(default=None)
    height: Union[str, None] = HtmlAttribute(default=None)
    loop: Union[bool, None] = HtmlAttribute(default=None)
    muted: Union[bool, None] = HtmlAttribute(default=None)
    playsinline: Union[bool, None] = HtmlAttribute(default=None)
    poster: Union[str, None] = HtmlAttribute(default=None)
    preload: Preload = HtmlAttribute(default=None)
    src: Union[str, None] = HtmlAttribute(default=None)
    width: Union[str, None] = HtmlAttribute(default=None)


class Wbr(BaseNoChildrenHtmlElement, tag="wbr", tag_omission=True):
    pass
