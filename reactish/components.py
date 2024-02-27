from typing import Any

from .base import BaseComponent


class A(BaseComponent):
    html_tag = "a"
    extra_attrs = ["download", "href", "target"]

    def __init__(
        self,
        *args: Any,
        download: bool | None = None,
        href: str | None = None,
        target: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)
        self.download = download
        self.href = href
        self.target = target


class Aside(BaseComponent):
    html_tag = "aside"


class Br(BaseComponent):
    html_tag = "br"


class Button(BaseComponent):
    html_tag = "button"
    extra_attrs = [
        "autofocus",
        "disabled",
        "form",
        "formaction",
        "formenctype",
        "formmethod",
        "formonvalidate",
        "formtarget",
        "name",
        "popovertarget",
        "popovertargetaction",
        "type",
        "value",
    ]

    def __init__(
        self,
        *args: Any,
        autofocus: bool | None = None,
        disabled: bool | None = None,
        form: str | None = None,
        formaction: str | None = None,
        formenctype: str | None = None,
        formmethod: str | None = None,
        formonvalidate: str | None = None,
        formtarget: str | None = None,
        name: str | None = None,
        popovertarget: str | None = None,
        popovertargetaction: str | None = None,
        type: str | None = None,
        value: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)
        self.autofocus = autofocus
        self.disabled = disabled
        self.form = form
        self.formaction = formaction
        self.formenctype = formenctype
        self.formmethod = formmethod
        self.formonvalidate = formonvalidate
        self.formtarget = formtarget
        self.name = name
        self.popovertarget = popovertarget
        self.popovertargetaction = popovertargetaction
        self.type = type
        self.value = value


class Caption(BaseComponent):
    html_tag = "caption"


class Cite(BaseComponent):
    html_tag = "cite"


class Code(BaseComponent):
    html_tag = "code"


class Col(BaseComponent):
    html_tag = "col"
    extra_attrs = ["span"]

    def __init__(self, *args: Any, span: int | None = None, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.span = span


class Colgroup(BaseComponent):
    html_tag = "colgroup"
    extra_attrs = ["span"]

    def __init__(self, *args: Any, span: int | None = None, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.span = span


class Data(BaseComponent):
    html_tag = "data"
    extra_attrs = ["value"]

    def __init__(self, *args: Any, value: Any | None = None, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.value = value


class Datalist(BaseComponent):
    html_tag = "datalist"


class Div(BaseComponent):
    html_tag = "div"


class Em(BaseComponent):
    html_tag = "em"


class Figure(BaseComponent):
    html_tag = "figure"


class Footer(BaseComponent):
    html_tag = "footer"


class Form(BaseComponent):
    html_tag = "form"
    extra_attrs = [
        "accept_charset",
        "autocapitalize",
        "autocomplete",
        "name",
        "rel",
        "action",
        "enctype",
        "method",
        "novalidate",
        "target",
    ]

    def __init__(
        self,
        *args: Any,
        accept_charset: str | None = None,
        autocapitalize: str | None = None,
        autocomplete: str | None = None,
        name: str | None = None,
        rel: str | None = None,
        action: str | None = None,
        enctype: str | None = None,
        method: str | None = None,
        novalidate: str | None = None,
        target: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)
        self.accept_charset = accept_charset
        self.autocapitalize = autocapitalize
        self.autocomplete = autocomplete
        self.name = name
        self.rel = rel
        self.action = action
        self.enctype = enctype
        self.method = method
        self.novalidate = novalidate
        self.target = target


class H(BaseComponent):
    def __init__(self, *args: Any, level: int, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.level = level

    @property
    def html_tag(self):
        return f"h{self.level}"


class I(BaseComponent):
    html_tag = "i"


class Img(BaseComponent):
    html_tag = "img"
    extra_attrs = [
        "alt",
        "crossorigin",
        "decoding",
        "elementtiming",
        "fetchpriority",
        "height",
        "ismap",
        "loading",
        "referrerpolicy",
        "sizes",
        "src",
        "srcset",
        "width",
        "usemap",
    ]

    def __init__(
        self,
        *args: Any,
        src: str,
        alt: str | None = None,
        crossorigin: str | None = None,
        decoding: str | None = None,
        elementtiming: str | None = None,
        fetchpriority: str | None = None,
        height: str | None = None,
        ismap: str | None = None,
        loading: str | None = None,
        referrerpolicy: str | None = None,
        sizes: str | None = None,
        srcset: str | None = None,
        width: str | None = None,
        usemap: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)
        self.alt = alt
        self.crossorigin = crossorigin
        self.decoding = decoding
        self.elementtiming = elementtiming
        self.fetchpriority = fetchpriority
        self.height = height
        self.ismap = ismap
        self.loading = loading
        self.referrerpolicy = referrerpolicy
        self.sizes = sizes
        self.src = src
        self.srcset = srcset
        self.width = width
        self.usemap = usemap


class Input(BaseComponent):
    html_tag = "input"
    extra_attrs = [
        "accept",
        "alt",
        "autocapitalize",
        "autocomplete",
        "capture",
        "checked",
        "dirname",
        "disabled",
        "form",
        "formaction",
        "formenctype",
        "formmethod",
        "formnovalidate",
        "formtarget",
        "height",
        "list",
        "max",
        "maxlength",
        "min",
        "minlength",
        "multiple",
        "name",
        "pattern",
        "placeholder",
        "popovertarget",
        "popovertargetaction",
        "readonly",
        "required",
        "size",
        "src",
        "step",
        "type",
        "value",
        "width",
    ]

    def __init__(
        self,
        *args: Any,
        accept: str | None = None,
        alt: str | None = None,
        autocapitalize: str | None = None,
        autocomplete: str | None = None,
        capture: str | None = None,
        checked: str | None = None,
        dirname: str | None = None,
        disabled: str | None = None,
        form: str | None = None,
        formaction: str | None = None,
        formenctype: str | None = None,
        formmethod: str | None = None,
        formnovalidate: str | None = None,
        formtarget: str | None = None,
        height: str | None = None,
        list: str | None = None,
        max: str | None = None,
        maxlength: str | None = None,
        min: str | None = None,
        minlength: str | None = None,
        multiple: str | None = None,
        name: str | None = None,
        pattern: str | None = None,
        placeholder: str | None = None,
        popovertarget: str | None = None,
        popovertargetaction: str | None = None,
        readonly: str | None = None,
        required: str | None = None,
        size: str | None = None,
        src: str | None = None,
        step: str | None = None,
        type: str | None = None,
        value: str | None = None,
        width: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)
        self.accept = accept
        self.alt = alt
        self.autocapitalize = autocapitalize
        self.autocomplete = autocomplete
        self.capture = capture
        self.checked = checked
        self.dirname = dirname
        self.disabled = disabled
        self.form = form
        self.formaction = formaction
        self.formenctype = formenctype
        self.formmethod = formmethod
        self.formnovalidate = formnovalidate
        self.formtarget = formtarget
        self.height = height
        self.list = list
        self.max = max
        self.maxlength = maxlength
        self.min = min
        self.minlength = minlength
        self.multiple = multiple
        self.name = name
        self.pattern = pattern
        self.placeholder = placeholder
        self.popovertarget = popovertarget
        self.popovertargetaction = popovertargetaction
        self.readonly = readonly
        self.required = required
        self.size = size
        self.src = src
        self.step = step
        self.type = type
        self.value = value
        self.width = width


class Label(BaseComponent):
    html_tag = "label"
    extra_attrs = ("for_",)

    def __init__(self, *args: Any, for_: str | None = None, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.for_ = for_


class Li(BaseComponent):
    html_tag = "li"
    extra_attrs = ("value",)

    def __init__(self, *args: Any, value: str | None = None, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.value = value


class Main(BaseComponent):
    html_tag = "main"


class Nav(BaseComponent):
    html_tag = "nav"


class Object(BaseComponent):
    html_tag = "object"
    extra_attrs = (
        "data",
        "form",
        "height",
        "name",
        "type",
        "width",
    )

    def __init__(
        self,
        *args: Any,
        data: str | None = None,
        form: str | None = None,
        height: str | None = None,
        name: str | None = None,
        type: str | None = None,
        width: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)
        self.data = data
        self.form = form
        self.height = height
        self.name = name
        self.type = type
        self.width = width


class Ol(BaseComponent):
    html_tag = "ol"
    extra_attrs = (
        "reserved",
        "start",
        "type",
    )

    def __init__(
        self,
        *args: Any,
        reversed: bool | None = None,
        start: int | None = None,
        type: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)
        self.reversed = reversed
        self.start = start
        self.type = type


class OptGroup(BaseComponent):
    html_tag = "optgroup"
    extra_attrs = (
        "disabled",
        "label",
    )

    def __init__(
        self,
        *args: Any,
        disabled: bool | None = None,
        label: int | None = None,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)
        self.disabled = disabled
        self.label = label


class Option(BaseComponent):
    html_tag = "option"
    extra_attrs = ("disabled", "label", "selected", "value")

    def __init__(
        self,
        *args: Any,
        disabled: bool | None = None,
        label: int | None = None,
        selected: bool | None = None,
        value: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)
        self.disabled = disabled
        self.label = label
        self.selected = selected
        self.value = value


class P(BaseComponent):
    html_tag = "p"


class Picture(BaseComponent):
    html_tag = "picture"


class Pre(BaseComponent):
    html_tag = "pre"


class S(BaseComponent):
    html_tag = "s"


class Search(BaseComponent):
    html_tag = "search"


class Section(BaseComponent):
    html_tag = "section"


class Select(BaseComponent):
    html_tag = "select"
    extra_attrs = (
        "autocomplete",
        "autofocus",
        "disabled",
        "form",
        "multiple",
        "name",
        "required",
        "size",
    )

    def __init__(
        self,
        *args: Any,
        autocomplete: bool | None = None,
        autofocus: bool | None = None,
        disabled: bool | None = None,
        form: str | None = None,
        multiple: bool | None = None,
        name: str | None = None,
        required: bool | None = None,
        size: int | None = None,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)
        self.autocomplete = autocomplete
        self.autofocus = autofocus
        self.disabled = disabled
        self.form = form
        self.multiple = multiple
        self.name = name
        self.required = required
        self.size = size


class Small(BaseComponent):
    html_tag = "small"


class Source(BaseComponent):
    html_tag = "source"
    extra_attrs = (
        "type",
        "src",
        "srcset",
        "sizes",
        "media",
        "height",
        "width",
    )

    def __init__(
        self,
        *args: Any,
        type: str | None = None,
        src: str | None = None,
        srcset: str | None = None,
        sizes: str | None = None,
        media: str | None = None,
        height: str | None = None,
        width: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)
        self.type = type
        self.src = src
        self.srcset = srcset
        self.sizes = sizes
        self.media = media
        self.height = height
        self.width = width


class Span(BaseComponent):
    html_tag = "span"


class Strong(BaseComponent):
    html_tag = "strong"


class Sub(BaseComponent):
    html_tag = "sub"


class Summary(BaseComponent):
    html_tag = "summary"


class Sup(BaseComponent):
    html_tag = "sup"


class Table(BaseComponent):
    html_tag = "table"


class Tbody(BaseComponent):
    html_tag = "tbody"


class Td(BaseComponent):
    html_tag = "td"
    extra_attrs = ("colspan", "rowspan", "headers")

    def __init__(
        self,
        *args: Any,
        colspan: int | None = None,
        rowspan: int | None = None,
        headers: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)
        self.colspan = colspan
        self.rowspan = rowspan
        self.headers = headers


class TextArea(BaseComponent):
    html_tag = "textarea"

    def to_html(self, indent=0, indent_step=2, format=True) -> str:
        # TODO Clean this up. TextArea should not hold its value in a new line / tabs
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
                    new_indent = ""
                    html_string += f"{new_indent}{c}{endline}"
            html_string += f"{block_indent}</{self.html_tag}>{endline}"
        else:
            html_string += f"></{self.html_tag}>{endline}"

        return html_string


class Tfoot(BaseComponent):
    html_tag = "tfoot"


class Th(BaseComponent):
    html_tag = "th"
    extra_attrs = ("abbr", "colspan", "rowspan", "headers", "scope")

    def __init__(
        self,
        *args: Any,
        abbr: str | None = None,
        colspan: int | None = None,
        rowspan: int | None = None,
        headers: str | None = None,
        scope: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)
        self.abbr = abbr
        self.colspan = colspan
        self.rowspan = rowspan
        self.headers = headers
        self.scope = scope


class Thead(BaseComponent):
    html_tag = "thead"


class Time(BaseComponent):
    html_tag = "time"
    extra_attrs = ("datetime",)

    def __init__(
        self,
        *args: Any,
        datetime: str | None,
        **kwargs: Any,
    ):
        super().__init__(*args, **kwargs)
        self.datetime = datetime


class Tr(BaseComponent):
    html_tag = "tr"


class U(BaseComponent):
    html_tag = "u"


class Ul(BaseComponent):
    html_tag = "ul"


class Var(BaseComponent):
    html_tag = "var"
