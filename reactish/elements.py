from abc import ABC
from typing import Any, Literal, Union, override

from .fancy import BaseHtmlComponent, HtmlAttribute, HtmlMetaClass

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
    onautocomplete: str = HtmlAttribute(default=None)
    onabort: str = HtmlAttribute(default=None)
    onautocompleteerror: str = HtmlAttribute(default=None)
    onblur: str = HtmlAttribute(default=None)
    oncancel: str = HtmlAttribute(default=None)
    oncanplay: str = HtmlAttribute(default=None)
    oncanplaythrough: str = HtmlAttribute(default=None)
    onchange: str = HtmlAttribute(default=None)
    onclick: str = HtmlAttribute(default=None)
    onclose: str = HtmlAttribute(default=None)
    oncontextmenu: str = HtmlAttribute(default=None)
    oncuechange: str = HtmlAttribute(default=None)
    ondblclick: str = HtmlAttribute(default=None)
    ondrag: str = HtmlAttribute(default=None)
    ondragend: str = HtmlAttribute(default=None)
    ondragenter: str = HtmlAttribute(default=None)
    ondragleave: str = HtmlAttribute(default=None)
    ondragover: str = HtmlAttribute(default=None)
    ondragstart: str = HtmlAttribute(default=None)
    ondrop: str = HtmlAttribute(default=None)
    ondurationchange: str = HtmlAttribute(default=None)
    onemptied: str = HtmlAttribute(default=None)
    onended: str = HtmlAttribute(default=None)
    onerror: str = HtmlAttribute(default=None)
    onfocus: str = HtmlAttribute(default=None)
    oninput: str = HtmlAttribute(default=None)
    oninvalid: str = HtmlAttribute(default=None)
    onkeydown: str = HtmlAttribute(default=None)
    onkeypress: str = HtmlAttribute(default=None)
    onkeyup: str = HtmlAttribute(default=None)
    onload: str = HtmlAttribute(default=None)
    onloadeddata: str = HtmlAttribute(default=None)
    onloadedmetadata: str = HtmlAttribute(default=None)
    onloadstart: str = HtmlAttribute(default=None)
    onmousedown: str = HtmlAttribute(default=None)
    onmouseenter: str = HtmlAttribute(default=None)
    onmouseleave: str = HtmlAttribute(default=None)
    onmousemove: str = HtmlAttribute(default=None)
    onmouseout: str = HtmlAttribute(default=None)
    onmouseover: str = HtmlAttribute(default=None)
    onmouseup: str = HtmlAttribute(default=None)
    onmousewheel: str = HtmlAttribute(default=None)
    onpause: str = HtmlAttribute(default=None)
    onplay: str = HtmlAttribute(default=None)
    onplaying: str = HtmlAttribute(default=None)
    onprogress: str = HtmlAttribute(default=None)
    onratechange: str = HtmlAttribute(default=None)
    onreset: str = HtmlAttribute(default=None)
    onresize: str = HtmlAttribute(default=None)
    onscroll: str = HtmlAttribute(default=None)
    onseeked: str = HtmlAttribute(default=None)
    onseeking: str = HtmlAttribute(default=None)
    onselect: str = HtmlAttribute(default=None)
    onshow: str = HtmlAttribute(default=None)
    onsort: str = HtmlAttribute(default=None)
    onstalled: str = HtmlAttribute(default=None)
    onsubmit: str = HtmlAttribute(default=None)
    onsuspend: str = HtmlAttribute(default=None)
    ontimeupdate: str = HtmlAttribute(default=None)
    ontoggle: str = HtmlAttribute(default=None)
    onvolumechange: str = HtmlAttribute(default=None)
    onwaiting: str = HtmlAttribute(default=None)


class GlobalHtmlAttributes(ABC, metaclass=HtmlMetaClass):
    aria: dict[str, Any] = HtmlAttribute(default=None, multi_attribute=True)
    accesskey: str = HtmlAttribute(default=None)
    autocapitalize: AutoCapitalize = HtmlAttribute(default=None)
    autofocus: bool = HtmlAttribute(default=None)
    classes: list[str] = HtmlAttribute(
        default_factory=list,
        html_attribute="class",
        transformer=lambda x: " ".join(x),
    )
    contenteditable: ContentEditable = HtmlAttribute(default=None)
    contextmenu: str = HtmlAttribute(default=None)
    data: dict[str, Any] = HtmlAttribute(default=None, multi_attribute=True)
    dir: Dir = HtmlAttribute(default=None)
    draggable: TrueFalse = HtmlAttribute(default=None)
    enterkeyhint: EnterKeyHint = HtmlAttribute(default=None)
    exportparts: str = HtmlAttribute(default=None)
    hidden: Hidden = HtmlAttribute(default=None)
    id: str = HtmlAttribute(default=None)
    inert: bool = HtmlAttribute(default=None)
    inputmode: Inputmode = HtmlAttribute(default=None)
    is_: str = HtmlAttribute(default=None, html_attribute="is")
    itemid: str = HtmlAttribute(default=None)
    itemprop: str = HtmlAttribute(default=None)
    itemref: str = HtmlAttribute(default=None)
    itemscope: bool = HtmlAttribute(default=None)
    itemtype: str = HtmlAttribute(default=None)
    lang: str = HtmlAttribute(default=None)
    nonce: str = HtmlAttribute(default=None)
    part: str = HtmlAttribute(default=None)
    popover: str = HtmlAttribute(default=None)
    role: str = HtmlAttribute(default=None)
    slot: str = HtmlAttribute(default=None)
    spellcheck: TrueFalseEmpty = HtmlAttribute(default=None)
    style: dict[str, str] = HtmlAttribute(
        default_factory=dict,
        transformer=lambda x: "; ".join(f"{key}: {value}" for key, value in x.items()),
    )
    tabindex: int = HtmlAttribute(default=None)
    title: str = HtmlAttribute(default=None)
    translate: Translate = HtmlAttribute(default=None)
    virtualkeyboardpolicy: VirtualKeyboardPolicy = HtmlAttribute(default=None)


class NoComponentsHtmlComponent(
    EventHandlerAttributes,
    GlobalHtmlAttributes,
    BaseHtmlComponent,
    ABC,
):
    pass


class HtmlComponent(NoComponentsHtmlComponent, ABC):
    components: list[Union[str, "BaseHtmlComponent"]] = HtmlAttribute(default_factory=list, kw_only=False)


class A(HtmlComponent, tag="a"):
    download: str = HtmlAttribute(default=None)
    href: str = HtmlAttribute(default=None)
    hreflang: str = HtmlAttribute(default=None)
    ping: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    referrerpolicy: ReferrerPolicy = HtmlAttribute(default=None)
    ref: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    target: Target = HtmlAttribute(default=None)
    type: str = HtmlAttribute(default=None)


class Abbr(HtmlComponent, tag="abbr"):
    pass


class Address(HtmlComponent, tag="address"):
    pass


class Area(NoComponentsHtmlComponent, tag="area", tag_omission=True):
    alt: str = HtmlAttribute(default=None)
    coords: str = HtmlAttribute(default=None)
    download: str = HtmlAttribute(default=None)
    href: str = HtmlAttribute(default=None)
    ping: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    referrerpolicy: ReferrerPolicy = HtmlAttribute(default=None)
    rel: str = HtmlAttribute(default=None)
    shape: Shape = HtmlAttribute(default=None)
    target: Target = HtmlAttribute(default=None)
    value: str = HtmlAttribute(default=None)


class Article(HtmlComponent, tag="article"):
    height: str = HtmlAttribute(default=None)
    width: str = HtmlAttribute(default=None)


class Aside(HtmlComponent, tag="aside"):
    pass


class Audio(HtmlComponent, tag="audio"):
    autoplay: bool = HtmlAttribute(default=None)
    controls: bool = HtmlAttribute(default=None)
    controlslist: list[ControlsList] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    crossorigin: CrossOrigin
    disableremoteplayback: bool = HtmlAttribute(default=None)
    loop: bool = HtmlAttribute(default=None)
    muted: bool = HtmlAttribute(default=None)
    preload: Preload = HtmlAttribute(default=None)
    src: str = HtmlAttribute(default=None)


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
    onafterprint: str = HtmlAttribute(default=None)
    onbeforeprint: str = HtmlAttribute(default=None)
    onbeforeunload: str = HtmlAttribute(default=None)
    onblur: str = HtmlAttribute(default=None)
    onerror: str = HtmlAttribute(default=None)
    onfocus: str = HtmlAttribute(default=None)
    onhashchange: str = HtmlAttribute(default=None)
    onlanguagechange: str = HtmlAttribute(default=None)
    onload: str = HtmlAttribute(default=None)
    onmessage: str = HtmlAttribute(default=None)
    onoffline: str = HtmlAttribute(default=None)
    ononline: str = HtmlAttribute(default=None)
    onpopstate: str = HtmlAttribute(default=None)
    onredo: str = HtmlAttribute(default=None)
    onresize: str = HtmlAttribute(default=None)
    onstorage: str = HtmlAttribute(default=None)
    onundo: str = HtmlAttribute(default=None)
    onunload: str = HtmlAttribute(default=None)


class Br(NoComponentsHtmlComponent, tag="br", tag_omission=True):
    pass


class Button(HtmlComponent, tag="button"):
    autofocus: bool = HtmlAttribute(default=None)
    disable: bool = HtmlAttribute(default=None)
    form: str = HtmlAttribute(default=None)
    formaction: str = HtmlAttribute(default=None)
    formenctype: str = HtmlAttribute(default=None)
    formmethod: str = HtmlAttribute(default=None)
    formnovalidate: bool = HtmlAttribute(default=None)
    formtarget: Target = HtmlAttribute(default=None)
    name: str = HtmlAttribute(default=None)
    popovertarget: str = HtmlAttribute(default=None)
    popovertargetaction: str = HtmlAttribute(default=None)
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
    span: int = HtmlAttribute(default=None)


class Colgroup(HtmlComponent, tag="colgroup", tag_omission=True):
    span: int = HtmlAttribute(default=None)


class Data(HtmlComponent, tag="data"):
    value: Any = HtmlAttribute(default=None)


class Datalist(HtmlComponent, tag="datalist"):
    pass


class Dd(HtmlComponent, tag="dd", tag_omission=True):
    pass


class Del(HtmlComponent, tag="del"):
    cite: str = HtmlAttribute(default=None)
    datetime: str = HtmlAttribute(default=None)


class Details(HtmlComponent, tag="details"):
    open: bool = HtmlAttribute(default=None)


class Dfn(HtmlComponent, tag="dfn"):
    pass


class Dialog(HtmlComponent, tag="dialog"):
    open: bool = HtmlAttribute(default=None)


class Div(HtmlComponent, tag="div"):
    pass


class Dl(HtmlComponent, tag="dl"):
    pass


class Dt(HtmlComponent, tag="dt", tag_omission=True):
    pass


class Em(HtmlComponent, tag="em"):
    pass


class Embed(NoComponentsHtmlComponent, tag="embed", tag_omission=True):
    height: str = HtmlAttribute(default=None)
    src: str = HtmlAttribute(default=None)
    type: str = HtmlAttribute(default=None)
    width: str = HtmlAttribute(default=None)


class Fieldset(HtmlComponent, tag="fieldset"):
    disabled: bool = HtmlAttribute(default=None)
    form: str = HtmlAttribute(default=None)
    name: str = HtmlAttribute(default=None)


class Figcaption(HtmlComponent, tag="figcaption"):
    pass


class Figure(HtmlComponent, tag="figure"):
    pass


class Footer(HtmlComponent, tag="footer"):
    pass


class Form(HtmlComponent, tag="form"):
    accept_charset: str = HtmlAttribute(default=None, html_attribute="accept-charset")
    autocomplete: AutoComplete = HtmlAttribute(default=None)
    name: str = HtmlAttribute(default=None)
    rel: str = HtmlAttribute(default=None)

    action: str = HtmlAttribute(default=None)
    enctype: str = HtmlAttribute(default=None)
    method: str = HtmlAttribute(default=None)
    novalidate: str = HtmlAttribute(default=None)
    target: Target = HtmlAttribute(default=None)


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
    xmlms: str = HtmlAttribute(default=None)

    @override
    def to_html(self, indent=0, indent_step=2, format=True) -> str:
        html = super().to_html(indent=indent, indent_step=indent_step, format=format)
        return f"<!DOCTYPE html>\n{html}"


class I(HtmlComponent, tag="i"):
    pass


class Iframe(NoComponentsHtmlComponent, tag="iframe"):
    allow: str = HtmlAttribute(default=None)
    allowfullscreen: TrueFalse = HtmlAttribute(default=None)
    height: str = HtmlAttribute(default=None)
    loading: Loading = HtmlAttribute(default=None)
    name: str = HtmlAttribute(default=None)
    referrerpolicy: ReferrerPolicy = HtmlAttribute(default=None)
    sandbox: list[Sandbox] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    src: str = HtmlAttribute(default=None)
    srcdoc: str = HtmlAttribute(default=None)
    width: str = HtmlAttribute(default=None)


class Img(HtmlComponent, tag="img"):
    alt: str = HtmlAttribute(default=None)
    crossorigin: CrossOrigin = HtmlAttribute(default=None)
    decoding: Decoding = HtmlAttribute(default=None)
    elementtiming: str = HtmlAttribute(default=None)
    fetchpriority: FetchPriority = HtmlAttribute(default=None)
    height: str = HtmlAttribute(default=None)
    ismap: bool = HtmlAttribute(default=None)
    loading: Loading = HtmlAttribute(default=None)
    referrerpolicy: ReferrerPolicy = HtmlAttribute(default=None)
    sizes: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    src: str = HtmlAttribute(default=None)
    srcset: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    width: str = HtmlAttribute(default=None)
    usemap: str = HtmlAttribute(default=None)


class Input(NoComponentsHtmlComponent, tag="input", tag_omission=True):
    accept: str = HtmlAttribute(default=None)
    alt: str = HtmlAttribute(default=None)
    autocomplete: AutoComplete = HtmlAttribute(default=None)
    capture: str = HtmlAttribute(default=None)
    checked: bool = HtmlAttribute(default=None)
    dirname: str = HtmlAttribute(default=None)
    disabled: bool = HtmlAttribute(default=None)
    form: str = HtmlAttribute(default=None)
    formaction: str = HtmlAttribute(default=None)
    formenctype: str = HtmlAttribute(default=None)
    formmethod: str = HtmlAttribute(default=None)
    formnovalidate: str = HtmlAttribute(default=None)
    formtarget: Target = HtmlAttribute(default=None)
    height: str = HtmlAttribute(default=None)
    list: str = HtmlAttribute(default=None)
    max: str = HtmlAttribute(default=None)
    maxlength: str = HtmlAttribute(default=None)
    min: str = HtmlAttribute(default=None)
    minlength: str = HtmlAttribute(default=None)
    multiple: bool = HtmlAttribute(default=None)
    name: str = HtmlAttribute(default=None)
    pattern: str = HtmlAttribute(default=None)
    placeholder: str = HtmlAttribute(default=None)
    popovertarget: str = HtmlAttribute(default=None)
    popovertargetaction: PopoverTargetAction = HtmlAttribute(default=None)
    readonly: bool = HtmlAttribute(default=None)
    required: bool = HtmlAttribute(default=None)
    size: str = HtmlAttribute(default=None)
    src: str = HtmlAttribute(default=None)
    step: int = HtmlAttribute(default=None)
    type: InputType = HtmlAttribute(default=None)
    value: Any = HtmlAttribute(default=None)
    width: str = HtmlAttribute(default=None)


# TODO Create separate classes for each Input Type with the relevant attributes


class Ins(HtmlComponent, tag="ins"):
    cite: str = HtmlAttribute(default=None)
    datetime: str = HtmlAttribute(default=None)


class Kbd(HtmlComponent, tag="kbd"):
    pass


class Label(HtmlComponent, tag="label"):
    for_: str = HtmlAttribute(default=None, html_attribute="for")


class Legend(HtmlComponent, tag="legend"):
    pass


class Li(HtmlComponent, tag="li", tag_omission=True):
    value: int = HtmlAttribute(default=None)


class Link(NoComponentsHtmlComponent, tag="link", tag_omission=True):
    as_: str = HtmlAttribute(default=None, html_attribute="as")
    crossorigin: CrossOrigin = HtmlAttribute(default=None)
    fetchpriority: FetchPriority = HtmlAttribute(default=None)
    href: str = HtmlAttribute(default=None)
    hreflang: str = HtmlAttribute(default=None)
    imagesizes: str = HtmlAttribute(default=None)
    imagesrcset: str = HtmlAttribute(default=None)
    integrity: str = HtmlAttribute(default=None)
    media: str = HtmlAttribute(default=None)
    referrerpolicy: ReferrerPolicy = HtmlAttribute(default=None)
    rel: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    sizes: str = HtmlAttribute(default=None)
    type: str = HtmlAttribute(default=None)


class Main(HtmlComponent, tag="main"):
    pass


class Map(HtmlComponent, tag="map"):
    name: str = HtmlAttribute(default=None)


class Mark(HtmlComponent, tag="mark"):
    pass


class Menu(HtmlComponent, tag="menu"):
    pass


class Meta(NoComponentsHtmlComponent, tag="meta", tag_omission=True):
    charset: str = HtmlAttribute(default=None)
    content: str = HtmlAttribute(default=None)
    http_equiv: str = HtmlAttribute(default=None, html_attribute="http-equiv")
    name: str = HtmlAttribute(default=None)


class Meter(HtmlComponent, tag="meter"):
    value: Any = HtmlAttribute(default=None)
    min: float = HtmlAttribute(default=None)
    max: float = HtmlAttribute(default=None)
    low: float = HtmlAttribute(default=None)
    high: float = HtmlAttribute(default=None)
    optimum: float = HtmlAttribute(default=None)
    form: str = HtmlAttribute(default=None)


class Nav(HtmlComponent, tag="nav"):
    pass


class Noscript(HtmlComponent, tag="noscript"):
    pass


class Object(HtmlComponent, tag="object"):
    data: Any = HtmlAttribute(default=None)
    form: str = HtmlAttribute(default=None)
    height: str = HtmlAttribute(default=None)
    name: str = HtmlAttribute(default=None)
    type: str = HtmlAttribute(default=None)
    width: str = HtmlAttribute(default=None)


class Ol(HtmlComponent, tag="ol"):
    reversed: bool = HtmlAttribute(default=None)
    start: int  = HtmlAttribute(default=None)
    type: ListType = HtmlAttribute(default=None)


class Optgroup(HtmlComponent, tag="optgroup"):
    disabled: bool = HtmlAttribute(default=None)
    label: str= HtmlAttribute(default=None)


class Option(HtmlComponent, tag="option"):
    disabled: bool = HtmlAttribute(default=None)
    label: str= HtmlAttribute(default=None)
    selected: bool = HtmlAttribute(default=None)
    value: Any = HtmlAttribute(default=None)


class Output(HtmlComponent, tag="output"):
    for_: list[str]  = HtmlAttribute(default_factory=list, transformer=lambda x:" ".join(x))
    form: str  = HtmlAttribute(default=None)
    name:str  = HtmlAttribute(default=None)


class P(HtmlComponent, tag="p"):
    pass


class Picture(HtmlComponent, tag="picture"):
    pass


class Portal(HtmlComponent, tag="portal"):
    referrerpolicy: ReferrerPolicy = HtmlAttribute(default=None)
    src: str = HtmlAttribute(default=None)


class Pre(HtmlComponent, tag="pre"):
    pass


class Progress(HtmlComponent, tag="progress"):
    max: float = HtmlAttribute(default=None)
    value: float  = HtmlAttribute(default=None)


class Q(HtmlComponent, tag="q"):
    cite: str = HtmlAttribute(default=None)


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
    async_: bool = HtmlAttribute(default=None,html_attribute="async")
    blocking: list[Blocking] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    crossorigin: CrossOrigin  = HtmlAttribute(default=None)
    defer: bool  = HtmlAttribute(default=None)
    fetchpriority: FetchPriority = HtmlAttribute(default=None)
    integrity: str  = HtmlAttribute(default=None)
    nomodule: bool = HtmlAttribute(default=None)
    nonce: str = HtmlAttribute(default=None)
    referrerpolicy: ReferrerPolicy = HtmlAttribute(default=None)
    src: str = HtmlAttribute(default=None)
    type: ScriptType = HtmlAttribute(default=None)


class Search(HtmlComponent, tag="search"):
    pass


class Section(HtmlComponent, tag="section"):
    pass


class Select(HtmlComponent, tag="select"):
    autocomplete: AutoComplete = HtmlAttribute(default=None)
    autofocus: bool = HtmlAttribute(default=None)
    disabled: bool = HtmlAttribute(default=None)
    form: str = HtmlAttribute(default=None)
    multiple:bool = HtmlAttribute(default=None)
    name: str  = HtmlAttribute(default=None)
    required: bool = HtmlAttribute(default=None)
    size: int = HtmlAttribute(default=None)


class Slot(HtmlComponent, tag="slot"):
    name: str  = HtmlAttribute(default=None)


class Small(HtmlComponent, tag="small"):
    pass


class Source(NoComponentsHtmlComponent, tag="source", tag_omission=True):
    type: str = HtmlAttribute(default=None)
    src: str = HtmlAttribute(default=None)
    srcset: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: " ".join(x))
    sizes: list[str] = HtmlAttribute(default_factory=list, transformer=lambda x: ", ".join(x))
    media: str = HtmlAttribute(default=None)
    height: str = HtmlAttribute(default=None)
    width: str = HtmlAttribute(default=None)


class Span(HtmlComponent, tag="span"):
    pass


class Strong(HtmlComponent, tag="strong"):
    pass


class Style(HtmlComponent, tag="style"):
    blocking: Blocking = HtmlAttribute(default=None)
    media: str = HtmlAttribute(default=None)
    nonce: str = HtmlAttribute(default=None)


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
    colspan: int = HtmlComponent(default=None)
    headers: list[str] = HtmlComponent(default_factory=list, transformer=lambda x: " ".join(x))
    rowspan: int  = HtmlComponent(default=None)


class Template(HtmlComponent, tag="template"):
    shadowrootmode: ShadowRootMode  = HtmlComponent(default=None)


class Textarea(HtmlComponent, tag="textarea"):
    autocapitalize: AutoCapitalize = HtmlComponent(default=None)
    autocomplete: AutoComplete = HtmlComponent(default=None)
    autofocus: bool = HtmlComponent(default=None)
    cols: int  = HtmlComponent(default=None)
    dirname: str = HtmlComponent(default=None)
    disabled: bool = HtmlComponent(default=None)
    form: str = HtmlComponent(default=None)
    maxlength: int = HtmlComponent(default=None)
    minlength: int = HtmlComponent(default=None)
    name: str  = HtmlComponent(default=None)
    placeholder: str = HtmlComponent(default=None)
    readonly: bool = HtmlComponent(default=None)
    required: bool = HtmlComponent(default=None)
    rows: int = HtmlComponent(default=None)
    spellcheck: Spellcheck = HtmlComponent(default=None)
    wrap: Wrap = HtmlComponent(default=None)


class Tfoot(HtmlComponent, tag="tfoot", tag_omission=True):
    pass


class Th(HtmlComponent, tag="th", tag_omission=True):
    abbr: str = HtmlComponent(default=None)
    colspan: int = HtmlComponent(default=None)
    headers: list[str] = HtmlComponent(default_factory=list, transformer=lambda x: " ".join(x))
    rowspan: int  = HtmlComponent(default=None)
    scope: ThScope = HtmlComponent(default=None)


class Thead(HtmlComponent, tag="thead", tag_omission=True):
    pass


class Time(HtmlComponent, tag="time"):
    datetime: str = HtmlComponent(default=None)


class Title(HtmlComponent, tag="title"):
    pass


class Tr(HtmlComponent, tag="tr", tag_omission=True):
    pass


class Track(NoComponentsHtmlComponent, tag="track", tag_omission=True):
    default: bool  = HtmlComponent(default=None)
    kind: TrackType  = HtmlComponent(default=None)
    label: str = HtmlComponent(default=None)
    str: str = HtmlComponent(default=None)
    srclang: str  = HtmlComponent(default=None)


class U(HtmlComponent, tag="u"):
    pass


class Ul(HtmlComponent, tag="ul"):
    pass


class Var(HtmlComponent, tag="var"):
    pass


class Video(HtmlComponent, tag="video"):
    autoplay: bool  = HtmlComponent(default=None)
    controls: str = HtmlComponent(default=None)
    controlslist: list[ControlsList] = HtmlComponent(default_factory=list, transformer=lambda x: " ".join(x))
    crossorigin: CrossOrigin = HtmlComponent(default=None)
    disablepictureinpicture: bool = HtmlComponent(default=None)
    disableremoteplayback: bool  = HtmlComponent(default=None)
    height: str  = HtmlComponent(default=None)
    loop: bool = HtmlComponent(default=None)
    muted: bool = HtmlComponent(default=None)
    playsinline: bool = HtmlComponent(default=None)
    poster: str = HtmlComponent(default=None)
    preload: Preload = HtmlComponent(default=None)
    src: str = HtmlComponent(default=None)
    width: str = HtmlComponent(default=None)


class Wbr(NoComponentsHtmlComponent, tag="wbr", tag_omission=True):
    pass
