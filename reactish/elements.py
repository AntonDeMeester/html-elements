from abc import ABC
from typing import Any, Literal, Union

from .base import BaseHtmlComponent, HtmlAttribute, HtmlMetaClass

TrueFalse = Literal["true", "false"]
TrueFalseEmpty = Union[Literal[""], TrueFalse]
ContentEditable = Union[TrueFalse, Literal["plaintext-only"]]
AutoCapitalize = Literal["none", "off", "sentences", "on", "words", "characters"]
Dir = Literal["ltr", "rtl", "auto"]
EnterKeyHint = Literal["enter", "done", "go", "next", "previous", "search", "send"]
Hidden = bool | Literal["", "hidden", "until-found"]
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
ControlsList = list[Union[str, Literal["nodownload", "nofullscreen", "noremoteplayback"]]]
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
InputType = Literal[
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
    onautocomplete: str | None = HtmlAttribute(default=None)
    onabort: str | None = HtmlAttribute(default=None)
    onautocompleteerror: str | None = HtmlAttribute(default=None)
    onblur: str | None = HtmlAttribute(default=None)
    oncancel: str | None = HtmlAttribute(default=None)
    oncanplay: str | None = HtmlAttribute(default=None)
    oncanplaythrough: str | None = HtmlAttribute(default=None)
    onchange: str | None = HtmlAttribute(default=None)
    onclick: str | None = HtmlAttribute(default=None)
    onclose: str | None = HtmlAttribute(default=None)
    oncontextmenu: str | None = HtmlAttribute(default=None)
    oncuechange: str | None = HtmlAttribute(default=None)
    ondblclick: str | None = HtmlAttribute(default=None)
    ondrag: str | None = HtmlAttribute(default=None)
    ondragend: str | None = HtmlAttribute(default=None)
    ondragenter: str | None = HtmlAttribute(default=None)
    ondragleave: str | None = HtmlAttribute(default=None)
    ondragover: str | None = HtmlAttribute(default=None)
    ondragstart: str | None = HtmlAttribute(default=None)
    ondrop: str | None = HtmlAttribute(default=None)
    ondurationchange: str | None = HtmlAttribute(default=None)
    onemptied: str | None = HtmlAttribute(default=None)
    onended: str | None = HtmlAttribute(default=None)
    onerror: str | None = HtmlAttribute(default=None)
    onfocus: str | None = HtmlAttribute(default=None)
    oninput: str | None = HtmlAttribute(default=None)
    oninvalid: str | None = HtmlAttribute(default=None)
    onkeydown: str | None = HtmlAttribute(default=None)
    onkeypress: str | None = HtmlAttribute(default=None)
    onkeyup: str | None = HtmlAttribute(default=None)
    onload: str | None = HtmlAttribute(default=None)
    onloadeddata: str | None = HtmlAttribute(default=None)
    onloadedmetadata: str | None = HtmlAttribute(default=None)
    onloadstart: str | None = HtmlAttribute(default=None)
    onmousedown: str | None = HtmlAttribute(default=None)
    onmouseenter: str | None = HtmlAttribute(default=None)
    onmouseleave: str | None = HtmlAttribute(default=None)
    onmousemove: str | None = HtmlAttribute(default=None)
    onmouseout: str | None = HtmlAttribute(default=None)
    onmouseover: str | None = HtmlAttribute(default=None)
    onmouseup: str | None = HtmlAttribute(default=None)
    onmousewheel: str | None = HtmlAttribute(default=None)
    onpause: str | None = HtmlAttribute(default=None)
    onplay: str | None = HtmlAttribute(default=None)
    onplaying: str | None = HtmlAttribute(default=None)
    onprogress: str | None = HtmlAttribute(default=None)
    onratechange: str | None = HtmlAttribute(default=None)
    onreset: str | None = HtmlAttribute(default=None)
    onresize: str | None = HtmlAttribute(default=None)
    onscroll: str | None = HtmlAttribute(default=None)
    onseeked: str | None = HtmlAttribute(default=None)
    onseeking: str | None = HtmlAttribute(default=None)
    onselect: str | None = HtmlAttribute(default=None)
    onshow: str | None = HtmlAttribute(default=None)
    onsort: str | None = HtmlAttribute(default=None)
    onstalled: str | None = HtmlAttribute(default=None)
    onsubmit: str | None = HtmlAttribute(default=None)
    onsuspend: str | None = HtmlAttribute(default=None)
    ontimeupdate: str | None = HtmlAttribute(default=None)
    ontoggle: str | None = HtmlAttribute(default=None)
    onvolumechange: str | None = HtmlAttribute(default=None)
    onwaiting: str | None = HtmlAttribute(default=None)


class GlobalHtmlAttributes(ABC, metaclass=HtmlMetaClass):
    aria: dict[str, Any] = HtmlAttribute(default_factory=dict, multi_attribute=True)
    accesskey: str | None = HtmlAttribute(default=None)
    autocapitalize: AutoCapitalize | None = HtmlAttribute(default=None)
    autofocus: bool | None = HtmlAttribute(default=None)
    classes: list[str] = HtmlAttribute(
        default_factory=list,
        html_attribute="class",
        transformer=lambda x: " ".join(x),
    )
    contenteditable: ContentEditable | None = HtmlAttribute(default=None)
    contextmenu: str | None = HtmlAttribute(default=None)
    data: dict[str, Any] = HtmlAttribute(default=None, multi_attribute=True)
    dir: Dir | None = HtmlAttribute(default=None)
    draggable: TrueFalse | None = HtmlAttribute(default=None)
    enterkeyhint: EnterKeyHint | None = HtmlAttribute(default=None)
    exportparts: str | None = HtmlAttribute(default=None)
    hidden: Hidden | None = HtmlAttribute(default=None)
    id: str | None = HtmlAttribute(default=None)
    inert: bool | None = HtmlAttribute(default=None)
    inputmode: Inputmode = HtmlAttribute(default=None)
    is_: str | None = HtmlAttribute(default=None, html_attribute="is")
    itemid: str | None = HtmlAttribute(default=None)
    itemprop: str | None = HtmlAttribute(default=None)
    itemref: str | None = HtmlAttribute(default=None)
    itemscope: bool | None = HtmlAttribute(default=None)
    itemtype: str | None = HtmlAttribute(default=None)
    lang: str | None = HtmlAttribute(default=None)
    nonce: str | None = HtmlAttribute(default=None)
    part: str | None = HtmlAttribute(default=None)
    popover: str | None = HtmlAttribute(default=None)
    role: str | None = HtmlAttribute(default=None)
    slot: str | None = HtmlAttribute(default=None)
    spellcheck: Spellcheck = HtmlAttribute(default=None)
    style: dict[str, str] = HtmlAttribute(
        default_factory=dict,
        transformer=lambda x: "; ".join(f"{key}: {value}" for key, value in x.items()),
    )
    tabindex: int | None = HtmlAttribute(default=None)
    title: str | None = HtmlAttribute(default=None)
    translate: Translate | None = HtmlAttribute(default=None)
    virtualkeyboardpolicy: VirtualKeyboardPolicy | None = HtmlAttribute(default=None)


class NoComponentsHtmlComponent(
    EventHandlerAttributes,
    GlobalHtmlAttributes,
    BaseHtmlComponent,
    ABC,
):
    pass


class HtmlComponent(NoComponentsHtmlComponent, ABC):
    components: list[Union[str, "BaseHtmlComponent"]] = HtmlAttribute(default_factory=list, kw_only=False, is_attribute=False)


class A(HtmlComponent, tag="a"):
    download: str | None = HtmlAttribute(default=None)
    href: str | None = HtmlAttribute(default=None)
    hreflang: str | None = HtmlAttribute(default=None)
    ping: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    referrerpolicy: ReferrerPolicy | None = HtmlAttribute(default=None)
    ref: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    target: Target = HtmlAttribute(default=None)
    type: str | None = HtmlAttribute(default=None)


class Abbr(HtmlComponent, tag="abbr"):
    pass


class Address(HtmlComponent, tag="address"):
    pass


class Area(NoComponentsHtmlComponent, tag="area", tag_omission=True):
    alt: str | None = HtmlAttribute(default=None)
    coords: str | None = HtmlAttribute(default=None)
    download: str | None = HtmlAttribute(default=None)
    href: str | None = HtmlAttribute(default=None)
    ping: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    referrerpolicy: ReferrerPolicy | None = HtmlAttribute(default=None)
    rel: str | None = HtmlAttribute(default=None)
    shape: Shape = HtmlAttribute(default=None)
    target: Target = HtmlAttribute(default=None)
    value: str | None = HtmlAttribute(default=None)


class Article(HtmlComponent, tag="article"):
    height: str | None = HtmlAttribute(default=None)
    width: str | None = HtmlAttribute(default=None)


class Aside(HtmlComponent, tag="aside"):
    pass


class Audio(HtmlComponent, tag="audio"):
    autoplay: bool | None = HtmlAttribute(default=None)
    controls: bool | None = HtmlAttribute(default=None)
    controlslist: list[ControlsList] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    crossorigin: CrossOrigin | None = HtmlAttribute(default=None)
    disableremoteplayback: bool | None = HtmlAttribute(default=None)
    loop: bool | None = HtmlAttribute(default=None)
    muted: bool | None = HtmlAttribute(default=None)
    preload: Preload = HtmlAttribute(default=None)
    src: str | None = HtmlAttribute(default=None)


class B(HtmlComponent, tag="b"):
    pass


class Base(NoComponentsHtmlComponent, tag="base", tag_omission=True):
    href: str
    target: Target


class Bdi(HtmlComponent, tag="bdi"):
    pass


class Bdo(HtmlComponent, tag="bdo"):
    pass


class Blockquote(HtmlComponent, tag="blockquote"):
    cite: str


class Body(HtmlComponent, tag="body"):
    onafterprint: str | None = HtmlAttribute(default=None)
    onbeforeprint: str | None = HtmlAttribute(default=None)
    onbeforeunload: str | None = HtmlAttribute(default=None)
    onblur: str | None = HtmlAttribute(default=None)
    onerror: str | None = HtmlAttribute(default=None)
    onfocus: str | None = HtmlAttribute(default=None)
    onhashchange: str | None = HtmlAttribute(default=None)
    onlanguagechange: str | None = HtmlAttribute(default=None)
    onload: str | None = HtmlAttribute(default=None)
    onmessage: str | None = HtmlAttribute(default=None)
    onoffline: str | None = HtmlAttribute(default=None)
    ononline: str | None = HtmlAttribute(default=None)
    onpopstate: str | None = HtmlAttribute(default=None)
    onredo: str | None = HtmlAttribute(default=None)
    onresize: str | None = HtmlAttribute(default=None)
    onstorage: str | None = HtmlAttribute(default=None)
    onundo: str | None = HtmlAttribute(default=None)
    onunload: str | None = HtmlAttribute(default=None)


class Br(NoComponentsHtmlComponent, tag="br", tag_omission=True):
    pass


class Button(HtmlComponent, tag="button"):
    autofocus: bool | None = HtmlAttribute(default=None)
    disable: bool | None = HtmlAttribute(default=None)
    form: str | None = HtmlAttribute(default=None)
    formaction: str | None = HtmlAttribute(default=None)
    formenctype: str | None = HtmlAttribute(default=None)
    formmethod: str | None = HtmlAttribute(default=None)
    formnovalidate: bool | None = HtmlAttribute(default=None)
    formtarget: Target | None = HtmlAttribute(default=None)
    name: str | None = HtmlAttribute(default=None)
    popovertarget: str | None = HtmlAttribute(default=None)
    popovertargetaction: str | None = HtmlAttribute(default=None)
    type: ButtonType = HtmlAttribute(default=None)


class Canvas(HtmlComponent, tag="canvas"):
    pass


class Caption(HtmlComponent, tag="caption", tag_omission=True):
    pass


class Cite(HtmlComponent, tag="cite"):
    pass


class Code(HtmlComponent, tag="code"):
    pass


class Col(NoComponentsHtmlComponent, tag="col", tag_omission=True):
    span: int | None = HtmlAttribute(default=None)


class Colgroup(HtmlComponent, tag="colgroup", tag_omission=True):
    span: int | None = HtmlAttribute(default=None)


class Data(HtmlComponent, tag="data"):
    value: Any = HtmlAttribute(default=None)


class Datalist(HtmlComponent, tag="datalist"):
    pass


class Dd(HtmlComponent, tag="dd", tag_omission=True):
    pass


class Del(HtmlComponent, tag="del"):
    cite: str | None = HtmlAttribute(default=None)
    datetime: str | None = HtmlAttribute(default=None)


class Details(HtmlComponent, tag="details"):
    open: bool | None = HtmlAttribute(default=None)


class Dfn(HtmlComponent, tag="dfn"):
    pass


class Dialog(HtmlComponent, tag="dialog"):
    open: bool | None = HtmlAttribute(default=None)


class Div(HtmlComponent, tag="div"):
    pass


class Dl(HtmlComponent, tag="dl"):
    pass


class Dt(HtmlComponent, tag="dt", tag_omission=True):
    pass


class Em(HtmlComponent, tag="em"):
    pass


class Embed(NoComponentsHtmlComponent, tag="embed", tag_omission=True):
    height: str | None = HtmlAttribute(default=None)
    src: str | None = HtmlAttribute(default=None)
    type: str | None = HtmlAttribute(default=None)
    width: str | None = HtmlAttribute(default=None)


class Fieldset(HtmlComponent, tag="fieldset"):
    disabled: bool | None = HtmlAttribute(default=None)
    form: str | None = HtmlAttribute(default=None)
    name: str | None = HtmlAttribute(default=None)


class Figcaption(HtmlComponent, tag="figcaption"):
    pass


class Figure(HtmlComponent, tag="figure"):
    pass


class Footer(HtmlComponent, tag="footer"):
    pass


class Form(HtmlComponent, tag="form"):
    accept_charset: str | None = HtmlAttribute(default=None, html_attribute="accept-charset")
    autocomplete: AutoComplete = HtmlAttribute(default=None)
    name: str | None = HtmlAttribute(default=None)
    rel: str | None = HtmlAttribute(default=None)

    action: str | None = HtmlAttribute(default=None)
    enctype: str | None = HtmlAttribute(default=None)
    method: str | None = HtmlAttribute(default=None)
    novalidate: str | None = HtmlAttribute(default=None)
    target: Target | None = HtmlAttribute(default=None)


class H1(HtmlComponent, tag="h1"):
    pass


class H2(HtmlComponent, tag="h2"):
    pass


class H3(HtmlComponent, tag="h3"):
    pass


class H4(HtmlComponent, tag="h4"):
    pass


class H5(HtmlComponent, tag="h5"):
    pass


class H6(HtmlComponent, tag="h6"):
    pass


class Head(HtmlComponent, tag="head", tag_omission=True):
    pass


class Header(HtmlComponent, tag="header"):
    pass


class Hgroup(HtmlComponent, tag="hgroup"):
    pass


class Hr(NoComponentsHtmlComponent, tag="hr", tag_omission=True):
    pass


class Html(HtmlComponent, tag="html"):
    xmlms: str | None = HtmlAttribute(default=None)

    def to_html(self, indent: int =0, indent_step:int=2, format: bool=True) -> str:
        html = super().to_html(indent=indent, indent_step=indent_step, format=format)
        return f"<!DOCTYPE html>\n{html}"


class I(HtmlComponent, tag="i"): # noqa: E742
    pass


class Iframe(NoComponentsHtmlComponent, tag="iframe"):
    allow: str | None = HtmlAttribute(default=None)
    allowfullscreen: TrueFalse | None = HtmlAttribute(default=None)
    height: str | None = HtmlAttribute(default=None)
    loading: Loading = HtmlAttribute(default=None)
    name: str | None = HtmlAttribute(default=None)
    referrerpolicy: ReferrerPolicy | None = HtmlAttribute(default=None)
    sandbox: list[Sandbox] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    src: str | None = HtmlAttribute(default=None)
    srcdoc: str | None = HtmlAttribute(default=None)
    width: str | None = HtmlAttribute(default=None)


class Img(HtmlComponent, tag="img"):
    alt: str | None = HtmlAttribute(default=None)
    crossorigin: CrossOrigin | None = HtmlAttribute(default=None)
    decoding: Decoding = HtmlAttribute(default=None)
    elementtiming: str | None = HtmlAttribute(default=None)
    fetchpriority: FetchPriority | None = HtmlAttribute(default=None)
    height: str | None = HtmlAttribute(default=None)
    ismap: bool | None = HtmlAttribute(default=None)
    loading: Loading = HtmlAttribute(default=None)
    referrerpolicy: ReferrerPolicy = HtmlAttribute(default=None)
    sizes: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    src: str | None = HtmlAttribute(default=None)
    srcset: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    width: str | None = HtmlAttribute(default=None)
    usemap: str | None = HtmlAttribute(default=None)


class Input(NoComponentsHtmlComponent, tag="input", tag_omission=True):
    accept: str | None = HtmlAttribute(default=None)
    alt: str | None = HtmlAttribute(default=None)
    autocomplete: AutoComplete | None = HtmlAttribute(default=None)
    capture: str | None = HtmlAttribute(default=None)
    checked: bool | None = HtmlAttribute(default=None)
    dirname: str | None = HtmlAttribute(default=None)
    disabled: bool | None = HtmlAttribute(default=None)
    form: str | None = HtmlAttribute(default=None)
    formaction: str | None = HtmlAttribute(default=None)
    formenctype: str | None = HtmlAttribute(default=None)
    formmethod: str | None = HtmlAttribute(default=None)
    formnovalidate: str | None = HtmlAttribute(default=None)
    formtarget: Target = HtmlAttribute(default=None)
    height: str | None = HtmlAttribute(default=None)
    list: str | None = HtmlAttribute(default=None)
    max: str | None = HtmlAttribute(default=None)
    maxlength: str | None = HtmlAttribute(default=None)
    min: str | None = HtmlAttribute(default=None)
    minlength: str | None = HtmlAttribute(default=None)
    multiple: bool | None = HtmlAttribute(default=None)
    name: str | None = HtmlAttribute(default=None)
    pattern: str | None = HtmlAttribute(default=None)
    placeholder: str | None = HtmlAttribute(default=None)
    popovertarget: str | None = HtmlAttribute(default=None)
    popovertargetaction: PopoverTargetAction | None = HtmlAttribute(default=None)
    readonly: bool | None = HtmlAttribute(default=None)
    required: bool | None = HtmlAttribute(default=None)
    size: str | None = HtmlAttribute(default=None)
    src: str | None = HtmlAttribute(default=None)
    step: int | None = HtmlAttribute(default=None)
    type: InputType = HtmlAttribute(default=None)
    value: Any = HtmlAttribute(default=None)
    width: str | None = HtmlAttribute(default=None)


# TODO Create separate classes for each Input Type with the relevant attributes


class Ins(HtmlComponent, tag="ins"):
    cite: str | None = HtmlAttribute(default=None)
    datetime: str | None = HtmlAttribute(default=None)


class Kbd(HtmlComponent, tag="kbd"):
    pass


class Label(HtmlComponent, tag="label"):
    for_: str | None = HtmlAttribute(default=None, html_attribute="for")


class Legend(HtmlComponent, tag="legend"):
    pass


class Li(HtmlComponent, tag="li", tag_omission=True):
    value: int | None = HtmlAttribute(default=None)


class Link(NoComponentsHtmlComponent, tag="link", tag_omission=True):
    as_: str | None = HtmlAttribute(default=None, html_attribute="as")
    crossorigin: CrossOrigin | None = HtmlAttribute(default=None)
    fetchpriority: FetchPriority | None = HtmlAttribute(default=None)
    href: str | None = HtmlAttribute(default=None)
    hreflang: str | None = HtmlAttribute(default=None)
    imagesizes: str | None = HtmlAttribute(default=None)
    imagesrcset: str | None = HtmlAttribute(default=None)
    integrity: str | None = HtmlAttribute(default=None)
    media: str | None = HtmlAttribute(default=None)
    referrerpolicy: ReferrerPolicy | None = HtmlAttribute(default=None)
    rel: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    sizes: str | None = HtmlAttribute(default=None)
    type: str | None = HtmlAttribute(default=None)


class Main(HtmlComponent, tag="main"):
    pass


class Map(HtmlComponent, tag="map"):
    name: str | None = HtmlAttribute(default=None)


class Mark(HtmlComponent, tag="mark"):
    pass


class Menu(HtmlComponent, tag="menu"):
    pass


class Meta(NoComponentsHtmlComponent, tag="meta", tag_omission=True):
    charset: str | None = HtmlAttribute(default=None)
    content: str | None = HtmlAttribute(default=None)
    http_equiv: str | None = HtmlAttribute(default=None, html_attribute="http-equiv")
    name: str | None = HtmlAttribute(default=None)


class Meter(HtmlComponent, tag="meter"):
    value: Any = HtmlAttribute(default=None)
    min: float | None = HtmlAttribute(default=None)
    max: float | None = HtmlAttribute(default=None)
    low: float | None = HtmlAttribute(default=None)
    high: float | None = HtmlAttribute(default=None)
    optimum: float | None = HtmlAttribute(default=None)
    form: str | None = HtmlAttribute(default=None)


class Nav(HtmlComponent, tag="nav"):
    pass


class Noscript(HtmlComponent, tag="noscript"):
    pass


class Object(HtmlComponent, tag="object"):
    data: Any = HtmlAttribute(default=None)
    form: str | None = HtmlAttribute(default=None)
    height: str | None = HtmlAttribute(default=None)
    name: str | None = HtmlAttribute(default=None)
    type: str | None = HtmlAttribute(default=None)
    width: str | None = HtmlAttribute(default=None)


class Ol(HtmlComponent, tag="ol"):
    reversed: bool | None = HtmlAttribute(default=None)
    start: int | None = HtmlAttribute(default=None)
    type: ListType = HtmlAttribute(default=None)


class Optgroup(HtmlComponent, tag="optgroup"):
    disabled: bool | None = HtmlAttribute(default=None)
    label: str | None = HtmlAttribute(default=None)


class Option(HtmlComponent, tag="option"):
    disabled: bool | None = HtmlAttribute(default=None)
    label: str | None = HtmlAttribute(default=None)
    selected: bool | None = HtmlAttribute(default=None)
    value: Any = HtmlAttribute(default=None)


class Output(HtmlComponent, tag="output"):
    for_: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    form: str | None = HtmlAttribute(default=None)
    name: str | None = HtmlAttribute(default=None)


class P(HtmlComponent, tag="p"):
    pass


class Picture(HtmlComponent, tag="picture"):
    pass


class Portal(HtmlComponent, tag="portal"):
    referrerpolicy: ReferrerPolicy | None = HtmlAttribute(default=None)
    src: str | None = HtmlAttribute(default=None)


class Pre(HtmlComponent, tag="pre"):
    pass


class Progress(HtmlComponent, tag="progress"):
    max: float | None = HtmlAttribute(default=None)
    value: float | None = HtmlAttribute(default=None)


class Q(HtmlComponent, tag="q"):
    cite: str | None = HtmlAttribute(default=None)


class Rp(HtmlComponent, tag="rp", tag_omission=True):
    pass


class Rt(HtmlComponent, tag="rt", tag_omission=True):
    pass


class Ruby(HtmlComponent, tag="ruby"):
    pass


class S(HtmlComponent, tag="s"):
    pass


class Samp(HtmlComponent, tag="samp"):
    pass


class Script(HtmlComponent, tag="script"):
    async_: bool | None = HtmlAttribute(default=None, html_attribute="async")
    blocking: list[Blocking] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    crossorigin: CrossOrigin | None = HtmlAttribute(default=None)
    defer: bool | None = HtmlAttribute(default=None)
    fetchpriority: FetchPriority | None = HtmlAttribute(default=None)
    integrity: str | None = HtmlAttribute(default=None)
    nomodule: bool | None = HtmlAttribute(default=None)
    nonce: str | None = HtmlAttribute(default=None)
    referrerpolicy: ReferrerPolicy | None = HtmlAttribute(default=None)
    src: str | None = HtmlAttribute(default=None)
    type: ScriptType = HtmlAttribute(default=None)


class Search(HtmlComponent, tag="search"):
    pass


class Section(HtmlComponent, tag="section"):
    pass


class Select(HtmlComponent, tag="select"):
    autocomplete: AutoComplete | None = HtmlAttribute(default=None)
    autofocus: bool | None = HtmlAttribute(default=None)
    disabled: bool | None = HtmlAttribute(default=None)
    form: str | None = HtmlAttribute(default=None)
    multiple: bool | None = HtmlAttribute(default=None)
    name: str | None = HtmlAttribute(default=None)
    required: bool | None = HtmlAttribute(default=None)
    size: int | None = HtmlAttribute(default=None)


class Slot(HtmlComponent, tag="slot"):
    name: str | None = HtmlAttribute(default=None)


class Small(HtmlComponent, tag="small"):
    pass


class Source(NoComponentsHtmlComponent, tag="source", tag_omission=True):
    type: str | None = HtmlAttribute(default=None)
    src: str | None = HtmlAttribute(default=None)
    srcset: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    sizes: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: ", ".join(x))
    media: str | None = HtmlAttribute(default=None)
    height: str | None = HtmlAttribute(default=None)
    width: str | None = HtmlAttribute(default=None)


class Span(HtmlComponent, tag="span"):
    pass


class Strong(HtmlComponent, tag="strong"):
    pass


class Style(HtmlComponent, tag="style"):
    blocking: Blocking | None = HtmlAttribute(default=None)
    media: str | None = HtmlAttribute(default=None)
    nonce: str | None = HtmlAttribute(default=None)


class Sub(HtmlComponent, tag="sub"):
    pass


class Summary(HtmlComponent, tag="summary"):
    pass


class Sup(HtmlComponent, tag="sup"):
    pass


class Table(HtmlComponent, tag="table"):
    pass


class Tbody(HtmlComponent, tag="tbody", tag_omission=True):
    pass


class Td(HtmlComponent, tag="td", tag_omission=True):
    colspan: int | None = HtmlAttribute(default=None)
    headers: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    rowspan: int | None = HtmlAttribute(default=None)


class Template(HtmlComponent, tag="template"):
    shadowrootmode: ShadowRootMode = HtmlAttribute(default=None)


class Textarea(HtmlComponent, tag="textarea"):
    autocapitalize: AutoCapitalize | None = HtmlAttribute(default=None)
    autocomplete: AutoComplete | None = HtmlAttribute(default=None)
    autofocus: bool | None = HtmlAttribute(default=None)
    cols: int | None = HtmlAttribute(default=None)
    dirname: str | None = HtmlAttribute(default=None)
    disabled: bool | None = HtmlAttribute(default=None)
    form: str | None = HtmlAttribute(default=None)
    maxlength: int | None = HtmlAttribute(default=None)
    minlength: int | None = HtmlAttribute(default=None)
    name: str | None = HtmlAttribute(default=None)
    placeholder: str | None = HtmlAttribute(default=None)
    readonly: bool | None = HtmlAttribute(default=None)
    required: bool | None = HtmlAttribute(default=None)
    rows: int | None = HtmlAttribute(default=None)
    wrap: Wrap | None = HtmlAttribute(default=None)


class Tfoot(HtmlComponent, tag="tfoot", tag_omission=True):
    pass


class Th(HtmlComponent, tag="th", tag_omission=True):
    abbr: str | None = HtmlAttribute(default=None)
    colspan: int | None = HtmlAttribute(default=None)
    headers: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    rowspan: int | None = HtmlAttribute(default=None)
    scope: ThScope | None = HtmlAttribute(default=None)


class Thead(HtmlComponent, tag="thead", tag_omission=True):
    pass


class Time(HtmlComponent, tag="time"):
    datetime: str | None = HtmlAttribute(default=None)


class Title(HtmlComponent, tag="title"):
    pass


class Tr(HtmlComponent, tag="tr", tag_omission=True):
    pass


class Track(NoComponentsHtmlComponent, tag="track", tag_omission=True):
    default: bool | None = HtmlAttribute(default=None)
    kind: TrackType | None = HtmlAttribute(default=None)
    label: str | None = HtmlAttribute(default=None)
    src: str | None = HtmlAttribute(default=None)
    srclang: str | None = HtmlAttribute(default=None)


class U(HtmlComponent, tag="u"):
    pass


class Ul(HtmlComponent, tag="ul"):
    pass


class Var(HtmlComponent, tag="var"):
    pass


class Video(HtmlComponent, tag="video"):
    autoplay: bool | None = HtmlAttribute(default=None)
    controls: str | None = HtmlAttribute(default=None)
    controlslist: list[ControlsList] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    crossorigin: CrossOrigin | None = HtmlAttribute(default=None)
    disablepictureinpicture: bool | None = HtmlAttribute(default=None)
    disableremoteplayback: bool | None = HtmlAttribute(default=None)
    height: str | None = HtmlAttribute(default=None)
    loop: bool | None = HtmlAttribute(default=None)
    muted: bool | None = HtmlAttribute(default=None)
    playsinline: bool | None = HtmlAttribute(default=None)
    poster: str | None = HtmlAttribute(default=None)
    preload: Preload = HtmlAttribute(default=None)
    src: str | None = HtmlAttribute(default=None)
    width: str | None = HtmlAttribute(default=None)


class Wbr(NoComponentsHtmlComponent, tag="wbr", tag_omission=True):
    pass
