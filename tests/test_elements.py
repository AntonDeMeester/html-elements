from typing import Set, Type, Union

import pytest
from html_elements import elements as e
from html_elements.base import BaseHtmlElement

ALL_ELEMENTS: Set[Type[e.BaseHtmlElement]] = {
    e.A,
    e.Abbr,
    e.Address,
    e.Area,
    e.Article,
    e.Aside,
    e.Audio,
    e.B,
    e.Base,
    e.Bdi,
    e.Bdo,
    e.Blockquote,
    e.Body,
    e.Br,
    e.Button,
    e.Canvas,
    e.Caption,
    e.Cite,
    e.Code,
    e.Col,
    e.Colgroup,
    e.Data,
    e.Datalist,
    e.Dd,
    e.Del,
    e.Details,
    e.Dfn,
    e.Dialog,
    e.Div,
    e.Dl,
    e.Dt,
    e.Em,
    e.Embed,
    e.Fieldset,
    e.Figcaption,
    e.Figure,
    e.Footer,
    e.Form,
    e.H1,
    e.H2,
    e.H3,
    e.H4,
    e.H5,
    e.H6,
    e.Head,
    e.Header,
    e.Hgroup,
    e.Hr,
    e.Html,
    e.I,
    e.Iframe,
    e.Img,
    e.Input,
    e.Ins,
    e.Kbd,
    e.Label,
    e.Legend,
    e.Li,
    e.Link,
    e.Main,
    e.Map,
    e.Mark,
    e.Menu,
    e.Meta,
    e.Meter,
    e.Nav,
    e.Noscript,
    e.Object,
    e.Ol,
    e.Optgroup,
    e.Option,
    e.Output,
    e.P,
    e.Picture,
    e.Portal,
    e.Pre,
    e.Progress,
    e.Q,
    e.Rp,
    e.Rt,
    e.Ruby,
    e.S,
    e.Samp,
    e.Script,
    e.Search,
    e.Section,
    e.Select,
    e.Slot,
    e.Small,
    e.Source,
    e.Span,
    e.Strong,
    e.Style,
    e.Sub,
    e.Summary,
    e.Sup,
    e.Table,
    e.Tbody,
    e.Td,
    e.Template,
    e.Textarea,
    e.Tfoot,
    e.Th,
    e.Thead,
    e.Time,
    e.Title,
    e.Tr,
    e.Track,
    e.U,
    e.Ul,
    e.Var,
    e.Video,
    e.Wbr,
}
WITH_CHILDREN_ELEMENTS: Set[Type[e.BaseChildrenHtmlElement]] = {
    e.A,
    e.Abbr,
    e.Address,
    e.Article,
    e.Aside,
    e.Audio,
    e.B,
    e.Bdi,
    e.Bdo,
    e.Blockquote,
    e.Body,
    e.Button,
    e.Canvas,
    e.Caption,
    e.Cite,
    e.Code,
    e.Colgroup,
    e.Data,
    e.Datalist,
    e.Dd,
    e.Del,
    e.Details,
    e.Dfn,
    e.Dialog,
    e.Div,
    e.Dl,
    e.Dt,
    e.Em,
    e.Fieldset,
    e.Figcaption,
    e.Figure,
    e.Footer,
    e.Form,
    e.H1,
    e.H2,
    e.H3,
    e.H4,
    e.H5,
    e.H6,
    e.Head,
    e.Header,
    e.Hgroup,
    e.Html,
    e.I,
    e.Img,
    e.Ins,
    e.Kbd,
    e.Label,
    e.Legend,
    e.Li,
    e.Main,
    e.Map,
    e.Mark,
    e.Menu,
    e.Meter,
    e.Nav,
    e.Noscript,
    e.Object,
    e.Ol,
    e.Optgroup,
    e.Option,
    e.Output,
    e.P,
    e.Picture,
    e.Portal,
    e.Pre,
    e.Progress,
    e.Q,
    e.Rp,
    e.Rt,
    e.Ruby,
    e.S,
    e.Samp,
    e.Script,
    e.Search,
    e.Section,
    e.Select,
    e.Slot,
    e.Small,
    e.Span,
    e.Strong,
    e.Style,
    e.Sub,
    e.Summary,
    e.Sup,
    e.Table,
    e.Tbody,
    e.Td,
    e.Template,
    e.Textarea,
    e.Tfoot,
    e.Th,
    e.Thead,
    e.Time,
    e.Title,
    e.Tr,
    e.U,
    e.Ul,
    e.Var,
    e.Video,
}
NO_CHILDREN_ELEMENTS: Set[Type[e.BaseNoChildrenHtmlElement]] = {
    e.Area,
    e.Base,
    e.Br,
    e.Col,
    e.Embed,
    e.Hr,
    e.Iframe,
    e.Input,
    e.Link,
    e.Meta,
    e.Source,
    e.Track,
    e.Wbr,
}
NO_TAG_OMISSION_ELEMENTS: Set[Type[e.BaseHtmlElement]] = {
    e.A,
    e.Abbr,
    e.Address,
    e.Article,
    e.Aside,
    e.Audio,
    e.B,
    e.Bdi,
    e.Bdo,
    e.Blockquote,
    e.Body,
    e.Button,
    e.Canvas,
    e.Cite,
    e.Code,
    e.Data,
    e.Datalist,
    e.Del,
    e.Details,
    e.Dfn,
    e.Dialog,
    e.Div,
    e.Dl,
    e.Em,
    e.Fieldset,
    e.Figcaption,
    e.Figure,
    e.Footer,
    e.Form,
    e.H1,
    e.H2,
    e.H3,
    e.H4,
    e.H5,
    e.H6,
    e.Header,
    e.Hgroup,
    e.Html,
    e.I,
    e.Iframe,
    e.Img,
    e.Ins,
    e.Kbd,
    e.Label,
    e.Legend,
    e.Main,
    e.Map,
    e.Mark,
    e.Menu,
    e.Meter,
    e.Nav,
    e.Noscript,
    e.Object,
    e.Ol,
    e.Optgroup,
    e.Option,
    e.Output,
    e.P,
    e.Picture,
    e.Portal,
    e.Pre,
    e.Progress,
    e.Q,
    e.Ruby,
    e.S,
    e.Samp,
    e.Script,
    e.Search,
    e.Section,
    e.Select,
    e.Slot,
    e.Small,
    e.Span,
    e.Strong,
    e.Style,
    e.Sub,
    e.Summary,
    e.Sup,
    e.Table,
    e.Template,
    e.Textarea,
    e.Time,
    e.Title,
    e.U,
    e.Ul,
    e.Var,
    e.Video,
}
TAG_OMISSION_ELEMENTS: Set[Type[e.BaseHtmlElement]] = {
    e.Area,
    e.Base,
    e.Br,
    e.Col,
    e.Embed,
    e.Hr,
    e.Input,
    e.Link,
    e.Meta,
    e.Source,
    e.Track,
    e.Wbr,
    e.Caption,
    e.Colgroup,
    e.Dd,
    e.Dt,
    e.Head,
    e.Li,
    e.Rp,
    e.Rt,
    e.Tbody,
    e.Td,
    e.Tfoot,
    e.Th,
    e.Thead,
    e.Tr,
}


def _tag(el: Union[Type[e.BaseHtmlElement], e.BaseHtmlElement]) -> str:
    return el.get_config_value("tag")


def test_setup_children_complete():
    assert WITH_CHILDREN_ELEMENTS & NO_CHILDREN_ELEMENTS == set()
    assert ALL_ELEMENTS == (WITH_CHILDREN_ELEMENTS | NO_CHILDREN_ELEMENTS)


def test_setup_tag_omission_complete():
    assert TAG_OMISSION_ELEMENTS & NO_TAG_OMISSION_ELEMENTS == set()
    assert ALL_ELEMENTS == (TAG_OMISSION_ELEMENTS | NO_TAG_OMISSION_ELEMENTS)


@pytest.mark.parametrize("element_class", NO_CHILDREN_ELEMENTS)
def test_has_no_children(element_class: Type[BaseHtmlElement]):
    with pytest.raises(TypeError):
        element_class(["test"])
    assert "children" not in element_class.__html_attributes__
    assert all(attr.attribute_type == "attribute" for attr in element_class.__html_attributes__.values())


@pytest.mark.parametrize("element_class", WITH_CHILDREN_ELEMENTS)
def test_has_children(element_class: Type[e.BaseChildrenHtmlElement]):
    c = element_class(["test"])
    assert "children" in element_class.__html_attributes__
    assert all(
        attr.attribute_type == "attribute" for field, attr in element_class.__html_attributes__.items() if field != "children"
    )
    assert c.children == ["test"]


def test_global_attributes():
    class Basic(e.BaseNoChildrenHtmlElement, tag="basic"):
        pass

    c = Basic(
        onautocomplete="onautocomplete",
        onabort="onabort",
        onautocompleteerror="onautocompleteerror",
        onblur="onblur",
        oncancel="oncancel",
        oncanplay="oncanplay",
        oncanplaythrough="oncanplaythrough",
        onchange="onchange",
        onclick="onclick",
        onclose="onclose",
        oncontextmenu="oncontextmenu",
        oncuechange="oncuechange",
        ondblclick="ondblclick",
        ondrag="ondrag",
        ondragend="ondragend",
        ondragenter="ondragenter",
        ondragleave="ondragleave",
        ondragover="ondragover",
        ondragstart="ondragstart",
        ondrop="ondrop",
        ondurationchange="ondurationchange",
        onemptied="onemptied",
        onended="onended",
        onerror="onerror",
        onfocus="onfocus",
        oninput="oninput",
        oninvalid="oninvalid",
        onkeydown="onkeydown",
        onkeypress="onkeypress",
        onkeyup="onkeyup",
        onload="onload",
        onloadeddata="onloadeddata",
        onloadedmetadata="onloadedmetadata",
        onloadstart="onloadstart",
        onmousedown="onmousedown",
        onmouseenter="onmouseenter",
        onmouseleave="onmouseleave",
        onmousemove="onmousemove",
        onmouseout="onmouseout",
        onmouseover="onmouseover",
        onmouseup="onmouseup",
        onmousewheel="onmousewheel",
        onpause="onpause",
        onplay="onplay",
        onplaying="onplaying",
        onprogress="onprogress",
        onratechange="onratechange",
        onreset="onreset",
        onresize="onresize",
        onscroll="onscroll",
        onseeked="onseeked",
        onseeking="onseeking",
        onselect="onselect",
        onshow="onshow",
        onsort="onsort",
        onstalled="onstalled",
        onsubmit="onsubmit",
        onsuspend="onsuspend",
        ontimeupdate="ontimeupdate",
        ontoggle="ontoggle",
        onvolumechange="onvolumechange",
        onwaiting="onwaiting",
        aria={
            "foo": "bar",
            "True": True,
            "false": False,
            "None": None,
            "int": 5,
            "float": 5.5,
        },
        accesskey="accesskey",
        autocapitalize="none",
        autofocus=True,
        classes=["rows", "columns"],
        contenteditable="plaintext-only",
        contextmenu="contextmenu",
        data={
            "foo": "bar",
            "True": True,
            "false": False,
            "None": None,
            "int": 5,
            "float": 5.5,
        },
        dir="ltr",
        draggable="true",
        enterkeyhint="enter",
        exportparts="exportparts",
        hidden="hidden",
        id="id",
        inert=True,
        inputmode="none",
        is_="is_",
        itemid="itemid",
        itemprop="itemprop",
        itemref="itemref",
        itemscope=True,
        itemtype="itemtype",
        lang="lang",
        nonce="nonce",
        part="part",
        popover="popover",
        role="role",
        slot="slot",
        spellcheck="spellcheck",
        style={"foo": "bar", "empty": "", "reset": "none"},
        tabindex=5,
        title="title",
        translate="yes",
        virtualkeyboardpolicy="auto",
    )
    expected = """<basic
aria-foo="bar"
aria-True
aria-int="5"
aria-float="5.5"
accesskey="accesskey"
autocapitalize="none"
autofocus
class="rows columns"
contenteditable="plaintext-only"
contextmenu="contextmenu"
data-foo="bar"
data-True
data-int="5"
data-float="5.5"
dir="ltr"
draggable="true"
enterkeyhint="enter"
exportparts="exportparts"
hidden="hidden"
id="id"
inert
inputmode="none"
is="is_"
itemid="itemid"
itemprop="itemprop"
itemref="itemref"
itemscope
itemtype="itemtype"
lang="lang"
nonce="nonce"
part="part"
popover="popover"
role="role"
slot="slot"
spellcheck="spellcheck"
style="foo: bar; empty: ; reset: none"
tabindex="5"
title="title"
translate="yes"
virtualkeyboardpolicy="auto"
onautocomplete="onautocomplete"
onabort="onabort"
onautocompleteerror="onautocompleteerror"
onblur="onblur"
oncancel="oncancel"
oncanplay="oncanplay"
oncanplaythrough="oncanplaythrough"
onchange="onchange"
onclick="onclick"
onclose="onclose"
oncontextmenu="oncontextmenu"
oncuechange="oncuechange"
ondblclick="ondblclick"
ondrag="ondrag"
ondragend="ondragend"
ondragenter="ondragenter"
ondragleave="ondragleave"
ondragover="ondragover"
ondragstart="ondragstart"
ondrop="ondrop"
ondurationchange="ondurationchange"
onemptied="onemptied"
onended="onended"
onerror="onerror"
onfocus="onfocus"
oninput="oninput"
oninvalid="oninvalid"
onkeydown="onkeydown"
onkeypress="onkeypress"
onkeyup="onkeyup"
onload="onload"
onloadeddata="onloadeddata"
onloadedmetadata="onloadedmetadata"
onloadstart="onloadstart"
onmousedown="onmousedown"
onmouseenter="onmouseenter"
onmouseleave="onmouseleave"
onmousemove="onmousemove"
onmouseout="onmouseout"
onmouseover="onmouseover"
onmouseup="onmouseup"
onmousewheel="onmousewheel"
onpause="onpause"
onplay="onplay"
onplaying="onplaying"
onprogress="onprogress"
onratechange="onratechange"
onreset="onreset"
onresize="onresize"
onscroll="onscroll"
onseeked="onseeked"
onseeking="onseeking"
onselect="onselect"
onshow="onshow"
onsort="onsort"
onstalled="onstalled"
onsubmit="onsubmit"
onsuspend="onsuspend"
ontimeupdate="ontimeupdate"
ontoggle="ontoggle"
onvolumechange="onvolumechange"
onwaiting="onwaiting"></basic>"""
    assert c.to_html(format=False) == expected.replace("\n", " ")


@pytest.mark.parametrize("element_class", ALL_ELEMENTS)
def test_everything_has_global_attributes(element_class: Type[BaseHtmlElement]):
    assert issubclass(element_class, e.GlobalHtmlAttributes)


@pytest.mark.parametrize("element_class", ALL_ELEMENTS)
def test_everything_has_event_attributes(element_class: Type[BaseHtmlElement]):
    assert issubclass(element_class, e.EventHandlerAttributes)


@pytest.mark.parametrize("element_class", TAG_OMISSION_ELEMENTS & NO_CHILDREN_ELEMENTS)
def test_tag_omission_no_children_no_attributes(element_class: Type[BaseHtmlElement]):
    a = element_class()
    assert a.to_html(format=False) == f"<{_tag(a)} />"


@pytest.mark.parametrize("element_class", TAG_OMISSION_ELEMENTS & NO_CHILDREN_ELEMENTS)
def test_tag_omission_no_children_attributes(element_class: Type[BaseHtmlElement]):
    a = element_class(classes=["one"])
    assert a.to_html(format=False) == f"""<{_tag(a)} class="one" />"""


@pytest.mark.parametrize("element_class", TAG_OMISSION_ELEMENTS & WITH_CHILDREN_ELEMENTS)
def test_tag_omission_optional_children_none_present_no_attributes(
    element_class: Type[BaseHtmlElement],
):
    a = element_class()
    assert a.to_html(format=False) == f"<{_tag(a)} />"


@pytest.mark.parametrize("element_class", TAG_OMISSION_ELEMENTS & WITH_CHILDREN_ELEMENTS)
def test_tag_omission_optional_children_none_present_attributes(
    element_class: Type[BaseHtmlElement],
):
    a = element_class(classes=["one"])
    assert a.to_html(format=False) == f"""<{_tag(a)} class="one" />"""


@pytest.mark.parametrize("element_class", TAG_OMISSION_ELEMENTS & WITH_CHILDREN_ELEMENTS)
def test_tag_omission_optional_children_some_present_no_attributes(
    element_class: Type[BaseHtmlElement],
):
    a = element_class(["test"])
    assert a.to_html(format=False) == f"<{_tag(a)}>test</{_tag(a)}>"


@pytest.mark.parametrize("element_class", TAG_OMISSION_ELEMENTS & WITH_CHILDREN_ELEMENTS)
def test_tag_omission_optional_children_some_present_attributes(
    element_class: Type[BaseHtmlElement],
):
    a = element_class(["test"], classes=["one"])
    assert a.to_html(format=False) == f"""<{_tag(a)} class="one">test</{_tag(a)}>"""


def test_a():
    c = e.A(
        ["test"],
        download="download",
        href="href",
        hreflang="hreflang",
        ping=["one", "two"],
        referrerpolicy="no-referrer",
        ref=["one", "two"],
        target="_self",
        type="type",
    )
    assert (
        c.to_html(format=False)
        == '<a download="download" href="href" hreflang="hreflang" ping="one two" referrerpolicy="no-referrer" ref="one two" target="_self" type="type">test</a>'
    )


def test_abbr():
    c = e.Abbr(["test"])
    assert c.to_html(format=False) == "<abbr>test</abbr>"


def test_address():
    c = e.Address(["test"])
    assert c.to_html(format=False) == "<address>test</address>"


def test_article():
    c = e.Article(["test"], width="100px", height="100px")
    assert c.to_html(format=False) == '<article height="100px" width="100px">test</article>'


def test_aside():
    c = e.Aside(["test"])
    assert c.to_html(format=False) == "<aside>test</aside>"


def test_audio():
    c = e.Audio(
        ["test"],
        autoplay=True,
        controls=True,
        controlslist=["nodownload", "nofullscreen"],
        crossorigin="anonymous",
        disableremoteplayback=True,
        loop=True,
        muted=True,
        preload="none",
        src="src",
    )
    assert (
        c.to_html(format=False)
        == '<audio autoplay controls controlslist="nodownload nofullscreen" crossorigin="anonymous" disableremoteplayback loop muted preload="none" src="src">test</audio>'
    )


def test_b():
    c = e.B(["test"])
    assert c.to_html(format=False) == "<b>test</b>"


def test_bdi():
    c = e.Bdi(["test"])
    assert c.to_html(format=False) == "<bdi>test</bdi>"


def test_bdo():
    c = e.Bdo(["test"])
    assert c.to_html(format=False) == "<bdo>test</bdo>"


def test_blockquote():
    c = e.Blockquote(["test"], cite="Hello world")
    assert c.to_html(format=False) == '<blockquote cite="Hello world">test</blockquote>'


def test_body():
    c = e.Body(
        ["test"],
        onafterprint="onafterprint",
        onbeforeprint="onbeforeprint",
        onbeforeunload="onbeforeunload",
        onhashchange="onhashchange",
        onlanguagechange="onlanguagechange",
        onmessage="onmessage",
        onoffline="onoffline",
        ononline="ononline",
        onpopstate="onpopstate",
        onredo="onredo",
        onstorage="onstorage",
        onundo="onundo",
        onunload="onunload",
    )
    assert (
        c.to_html(format=False)
        == '<body onafterprint="onafterprint" onbeforeprint="onbeforeprint" onbeforeunload="onbeforeunload" onhashchange="onhashchange" onlanguagechange="onlanguagechange" onmessage="onmessage" onoffline="onoffline" ononline="ononline" onpopstate="onpopstate" onredo="onredo" onstorage="onstorage" onundo="onundo" onunload="onunload">test</body>'
    )


def test_button():
    c = e.Button(
        ["test"],
        autofocus=True,
        disable=True,
        form="form",
        formaction="formaction",
        formenctype="formenctype",
        formmethod="formmethod",
        formnovalidate=True,
        formtarget="formtarget",
        name="name",
        popovertarget="popovertarget",
        popovertargetaction="popovertargetaction",
        type="submit",
    )
    assert (
        c.to_html(format=False)
        == '<button autofocus disable form="form" formaction="formaction" formenctype="formenctype" formmethod="formmethod" formnovalidate formtarget="formtarget" name="name" popovertarget="popovertarget" popovertargetaction="popovertargetaction" type="submit">test</button>'
    )


def test_canvas():
    c = e.Canvas(["test"])
    assert c.to_html(format=False) == "<canvas>test</canvas>"


def test_caption():
    c = e.Caption(["test"])
    assert c.to_html(format=False) == "<caption>test</caption>"


def test_cite():
    c = e.Cite(["test"])
    assert c.to_html(format=False) == "<cite>test</cite>"


def test_code():
    c = e.Code(["test"])
    assert c.to_html(format=False) == "<code>test</code>"


def test_colgroup():
    c = e.Colgroup(["test"], span=5)
    assert c.to_html(format=False) == '<colgroup span="5">test</colgroup>'


def test_data():
    c = e.Data(["test"], value="Wololo")
    assert c.to_html(format=False) == '<data value="Wololo">test</data>'


def test_datalist():
    c = e.Datalist(["test"])
    assert c.to_html(format=False) == "<datalist>test</datalist>"


def test_dd():
    c = e.Dd(["test"])
    assert c.to_html(format=False) == "<dd>test</dd>"


def test_del():
    c = e.Del(["test"], cite="Smart person", datetime="2023-01-01")
    assert c.to_html(format=False) == '<del cite="Smart person" datetime="2023-01-01">test</del>'


def test_details():
    c = e.Details(["test"], open=True)
    assert c.to_html(format=False) == "<details open>test</details>"


def test_dfn():
    c = e.Dfn(["test"])
    assert c.to_html(format=False) == "<dfn>test</dfn>"


def test_dialog():
    c = e.Dialog(["test"], open=True)
    assert c.to_html(format=False) == "<dialog open>test</dialog>"


def test_div():
    c = e.Div(["test"])
    assert c.to_html(format=False) == "<div>test</div>"


def test_dl():
    c = e.Dl(["test"])
    assert c.to_html(format=False) == "<dl>test</dl>"


def test_dt():
    c = e.Dt(["test"])
    assert c.to_html(format=False) == "<dt>test</dt>"


def test_em():
    c = e.Em(["test"])
    assert c.to_html(format=False) == "<em>test</em>"


def test_fieldset():
    c = e.Fieldset(["test"], disabled=True, form="form", name="name")
    assert c.to_html(format=False) == '<fieldset disabled form="form" name="name">test</fieldset>'


def test_figcaption():
    c = e.Figcaption(["test"])
    assert c.to_html(format=False) == "<figcaption>test</figcaption>"


def test_figure():
    c = e.Figure(["test"])
    assert c.to_html(format=False) == "<figure>test</figure>"


def test_footer():
    c = e.Footer(["test"])
    assert c.to_html(format=False) == "<footer>test</footer>"


def test_form():
    c = e.Form(
        ["test"],
        accept_charset="charset",
        autocomplete="on",
        name="name",
        rel="rel",
        action="action",
        enctype="enctype",
        method="method",
        novalidate=True,
        target="_self",
    )
    assert (
        c.to_html(format=False)
        == '<form accept-charset="charset" autocomplete="on" name="name" rel="rel" action="action" enctype="enctype" method="method" novalidate target="_self">test</form>'
    )


def test_h1():
    c = e.H1(["test"])
    assert c.to_html(format=False) == "<h1>test</h1>"


def test_h2():
    c = e.H2(["test"])
    assert c.to_html(format=False) == "<h2>test</h2>"


def test_h3():
    c = e.H3(["test"])
    assert c.to_html(format=False) == "<h3>test</h3>"


def test_h4():
    c = e.H4(["test"])
    assert c.to_html(format=False) == "<h4>test</h4>"


def test_h5():
    c = e.H5(["test"])
    assert c.to_html(format=False) == "<h5>test</h5>"


def test_h6():
    c = e.H6(["test"])
    assert c.to_html(format=False) == "<h6>test</h6>"


def test_head():
    c = e.Head(["test"])
    assert c.to_html(format=False) == "<head>test</head>"


def test_header():
    c = e.Header(["test"])
    assert c.to_html(format=False) == "<header>test</header>"


def test_hgroup():
    c = e.Hgroup(["test"])
    assert c.to_html(format=False) == "<hgroup>test</hgroup>"


def test_html():
    c = e.Html(["test"])
    assert c.to_html(format=False) == "<!DOCTYPE html><html>test</html>"


def test_html_format():
    c = e.Html(["test"])
    assert c.to_html(format=True) == "<!DOCTYPE html>\n<html>\n  test\n</html>\n"


def test_i():
    c = e.I(["test"])
    assert c.to_html(format=False) == "<i>test</i>"


def test_img():
    c = e.Img(
        ["test"],
        alt="alt",
        crossorigin="anonymous",
        decoding="sync",
        elementtiming="elementtiming",
        fetchpriority="high",
        height="height",
        ismap=True,
        loading="loading",
        referrerpolicy="no-referrer",
        sizes=["size one", "size two"],
        src="src",
        srcset=["source one", "source two"],
        width="width",
        usemap="usemap",
    )
    assert (
        c.to_html(format=False)
        == '<img alt="alt" crossorigin="anonymous" decoding="sync" elementtiming="elementtiming" fetchpriority="high" height="height" ismap loading="loading" referrerpolicy="no-referrer" sizes="size one, size two" src="src" srcset="source one, source two" width="width" usemap="usemap">test</img>'
    )


def test_ins():
    c = e.Ins(["test"], cite="Smart person", datetime="2023-01-01")
    assert c.to_html(format=False) == '<ins cite="Smart person" datetime="2023-01-01">test</ins>'


def test_kbd():
    c = e.Kbd(["test"])
    assert c.to_html(format=False) == "<kbd>test</kbd>"


def test_label():
    c = e.Label(["test"], for_="here")
    assert c.to_html(format=False) == '<label for="here">test</label>'


def test_legend():
    c = e.Legend(["test"])
    assert c.to_html(format=False) == "<legend>test</legend>"


def test_li():
    c = e.Li(["test"], value=1)
    assert c.to_html(format=False) == '<li value="1">test</li>'


def test_main():
    c = e.Main(["test"])
    assert c.to_html(format=False) == "<main>test</main>"


def test_map():
    c = e.Map(["test"], name="Wollishollis")
    assert c.to_html(format=False) == '<map name="Wollishollis">test</map>'


def test_mark():
    c = e.Mark(["test"])
    assert c.to_html(format=False) == "<mark>test</mark>"


def test_menu():
    c = e.Menu(["test"])
    assert c.to_html(format=False) == "<menu>test</menu>"


def test_meter():
    c = e.Meter(
        ["test"],
        value=5.5,
        min=5.5,
        max=5.5,
        low=5.5,
        high=5.5,
        optimum=5.5,
        form="test",
    )
    assert (
        c.to_html(format=False)
        == '<meter value="5.5" min="5.5" max="5.5" low="5.5" high="5.5" optimum="5.5" form="test">test</meter>'
    )


def test_nav():
    c = e.Nav(["test"])
    assert c.to_html(format=False) == "<nav>test</nav>"


def test_noscript():
    c = e.Noscript(["test"])
    assert c.to_html(format=False) == "<noscript>test</noscript>"


def test_object():
    c = e.Object(
        ["test"],
        data="data",
        form="form",
        height="height",
        name="name",
        type="type",
        width="width",
    )
    assert (
        c.to_html(format=False)
        == '<object data="data" form="form" height="height" name="name" type="type" width="width">test</object>'
    )


def test_ol():
    c = e.Ol(["test"], reversed=True, start=1, type="a")
    assert c.to_html(format=False) == '<ol reversed start="1" type="a">test</ol>'


def test_optgroup():
    c = e.Optgroup(["test"], disabled=True, label="label")
    assert c.to_html(format=False) == '<optgroup disabled label="label">test</optgroup>'


def test_option():
    c = e.Option(["test"], disabled=True, label="label", selected=True, value="value")
    assert c.to_html(format=False) == '<option disabled label="label" selected value="value">test</option>'


def test_output():
    c = e.Output(["test"], for_=["for", "something"], form="form", name="name")
    assert c.to_html(format=False) == '<output for="for something" form="form" name="name">test</output>'


def test_p():
    c = e.P(["test"])
    assert c.to_html(format=False) == "<p>test</p>"


def test_picture():
    c = e.Picture(["test"])
    assert c.to_html(format=False) == "<picture>test</picture>"


def test_portal():
    c = e.Portal(["test"], referrerpolicy="no-referrer", src="src")
    assert c.to_html(format=False) == '<portal referrerpolicy="no-referrer" src="src">test</portal>'


def test_pre():
    c = e.Pre(["test"])
    assert c.to_html(format=False) == "<pre>test</pre>"


def test_progress():
    c = e.Progress(["test"], max=101.1, value=99.9)
    assert c.to_html(format=False) == '<progress max="101.1" value="99.9">test</progress>'


def test_q():
    c = e.Q(["test"], cite="Someone smart")
    assert c.to_html(format=False) == '<q cite="Someone smart">test</q>'


def test_rp():
    c = e.Rp(["test"])
    assert c.to_html(format=False) == "<rp>test</rp>"


def test_rt():
    c = e.Rt(["test"])
    assert c.to_html(format=False) == "<rt>test</rt>"


def test_ruby():
    c = e.Ruby(["test"])
    assert c.to_html(format=False) == "<ruby>test</ruby>"


def test_s():
    c = e.S(["test"])
    assert c.to_html(format=False) == "<s>test</s>"


def test_samp():
    c = e.Samp(["test"])
    assert c.to_html(format=False) == "<samp>test</samp>"


def test_script():
    c = e.Script(
        ["test"],
        async_=True,
        blocking=["render", "everything"],
        crossorigin="anonymous",
        defer=True,
        fetchpriority="high",
        integrity="integrity",
        nomodule=True,
        referrerpolicy="no-referrer",
        src="src",
        type="module",
    )
    assert (
        c.to_html(format=False)
        == '<script async blocking="render everything" crossorigin="anonymous" defer fetchpriority="high" integrity="integrity" nomodule referrerpolicy="no-referrer" src="src" type="module">test</script>'
    )


def test_search():
    c = e.Search(["test"])
    assert c.to_html(format=False) == "<search>test</search>"


def test_section():
    c = e.Section(["test"])
    assert c.to_html(format=False) == "<section>test</section>"


def test_select():
    c = e.Select(
        ["test"],
        autocomplete="on",
        disabled=True,
        form="form",
        multiple=True,
        name="name",
        required=True,
        size=5,
    )
    assert (
        c.to_html(format=False)
        == '<select autocomplete="on" disabled form="form" multiple name="name" required size="5">test</select>'
    )


def test_slot():
    c = e.Slot(["test"], name="name")
    assert c.to_html(format=False) == '<slot name="name">test</slot>'


def test_small():
    c = e.Small(["test"])
    assert c.to_html(format=False) == "<small>test</small>"


def test_span():
    c = e.Span(["test"])
    assert c.to_html(format=False) == "<span>test</span>"


def test_strong():
    c = e.Strong(["test"])
    assert c.to_html(format=False) == "<strong>test</strong>"


def test_style():
    c = e.Style(["test"], blocking="render", media="media")
    assert c.to_html(format=False) == '<style blocking="render" media="media">test</style>'


def test_sub():
    c = e.Sub(["test"])
    assert c.to_html(format=False) == "<sub>test</sub>"


def test_summary():
    c = e.Summary(["test"])
    assert c.to_html(format=False) == "<summary>test</summary>"


def test_sup():
    c = e.Sup(["test"])
    assert c.to_html(format=False) == "<sup>test</sup>"


def test_table():
    c = e.Table(["test"])
    assert c.to_html(format=False) == "<table>test</table>"


def test_tbody():
    c = e.Tbody(["test"])
    assert c.to_html(format=False) == "<tbody>test</tbody>"


def test_td():
    c = e.Td(
        ["test"],
        colspan=5,
        headers=["one", "two"],
        rowspan=4,
    )
    assert c.to_html(format=False) == '<td colspan="5" headers="one two" rowspan="4">test</td>'


def test_template():
    c = e.Template(["test"], shadowrootmode="open")
    assert c.to_html(format=False) == '<template shadowrootmode="open">test</template>'


def test_textarea():
    c = e.Textarea(
        ["test"],
        autocapitalize="none",
        autocomplete="on",
        cols=5,
        dirname="dirname",
        disabled=True,
        form="form",
        maxlength=20,
        minlength=5,
        name="name",
        placeholder="placeholder",
        readonly=True,
        required=True,
        rows=30,
        wrap="wrap",
    )  # TODO
    assert (
        c.to_html(format=False)
        == '<textarea autocapitalize="none" autocomplete="on" cols="5" dirname="dirname" disabled form="form" maxlength="20" minlength="5" name="name" placeholder="placeholder" readonly required rows="30" wrap="wrap">test</textarea>'
    )


def test_tfoot():
    c = e.Tfoot(["test"])
    assert c.to_html(format=False) == "<tfoot>test</tfoot>"


def test_th():
    c = e.Th(["test"], abbr="abbr", colspan=5, headers=["one", "two"], rowspan=5, scope="row")
    assert c.to_html(format=False) == '<th abbr="abbr" colspan="5" headers="one two" rowspan="5" scope="row">test</th>'


def test_thead():
    c = e.Thead(["test"])
    assert c.to_html(format=False) == "<thead>test</thead>"


def test_time():
    c = e.Time(["test"], datetime="2023-01-01")
    assert c.to_html(format=False) == '<time datetime="2023-01-01">test</time>'


def test_title():
    c = e.Title(["test"])
    assert c.to_html(format=False) == "<title>test</title>"


def test_tr():
    c = e.Tr(["test"])
    assert c.to_html(format=False) == "<tr>test</tr>"


def test_u():
    c = e.U(["test"])
    assert c.to_html(format=False) == "<u>test</u>"


def test_ul():
    c = e.Ul(["test"])
    assert c.to_html(format=False) == "<ul>test</ul>"


def test_var():
    c = e.Var(["test"])
    assert c.to_html(format=False) == "<var>test</var>"


def test_video():
    c = e.Video(
        ["test"],
        autoplay=True,
        controls="controls",
        controlslist=["nofullscreen", "noremoteplayback"],
        crossorigin="anonymous",
        disablepictureinpicture=True,
        disableremoteplayback=True,
        height="height",
        loop=True,
        muted=True,
        playsinline=True,
        poster="poster",
        preload="none",
        src="src",
        width="width",
    )
    assert (
        c.to_html(format=False)
        == '<video autoplay controls="controls" controlslist="nofullscreen noremoteplayback" crossorigin="anonymous" disablepictureinpicture disableremoteplayback height="height" loop muted playsinline poster="poster" preload="none" src="src" width="width">test</video>'
    )


def test_area():
    c = e.Area()
    assert c.to_html(format=False) == "<area />"


def test_base():
    c = e.Base(href="href", target="_self")
    assert c.to_html(format=False) == '<base href="href" target="_self" />'


def test_br():
    c = e.Br()
    assert c.to_html(format=False) == "<br />"


def test_col():
    c = e.Col(span=5)
    assert c.to_html(format=False) == '<col span="5" />'


def test_embed():
    c = e.Embed(height="height", src="src", type="type", width="width")
    assert c.to_html(format=False) == '<embed height="height" src="src" type="type" width="width" />'


def test_hr():
    c = e.Hr()
    assert c.to_html(format=False) == "<hr />"


def test_iframe():
    c = e.Iframe(
        allow="allow",
        allowfullscreen="true",
        height="height",
        loading="eager",
        name="name",
        referrerpolicy="no-referrer",
        sandbox=["allow-downloads", "allow-forms"],
        src="src",
        srcdoc="srcdoc",
        width="width",
    )
    assert (
        c.to_html(format=False)
        == '<iframe allow="allow" allowfullscreen="true" height="height" loading="eager" name="name" referrerpolicy="no-referrer" sandbox="allow-downloads allow-forms" src="src" srcdoc="srcdoc" width="width"></iframe>'
    )


def test_input():
    c = e.Input(
        accept="accept",
        alt="alt",
        autocomplete="on",
        capture="capture",
        checked=True,
        dirname="dirname",
        disabled=True,
        form="form",
        formaction="formaction",
        formenctype="formenctype",
        formmethod="formmethod",
        formnovalidate="formnovalidate",
        formtarget="formtarget",
        height="height",
        list="list",
        max=5,
        maxlength=5,
        min=5,
        minlength=5,
        multiple=True,
        name="name",
        pattern="pattern",
        placeholder="placeholder",
        popovertarget="popovertarget",
        popovertargetaction="hide",
        readonly=True,
        required=True,
        size=5,
        src="src",
        step=1,
        type="button",
        value="value",
        width="width",
    )
    assert (
        c.to_html(format=False)
        == '<input accept="accept" alt="alt" autocomplete="on" capture="capture" checked dirname="dirname" disabled form="form" formaction="formaction" formenctype="formenctype" formmethod="formmethod" formnovalidate="formnovalidate" formtarget="formtarget" height="height" list="list" max="5" maxlength="5" min="5" minlength="5" multiple name="name" pattern="pattern" placeholder="placeholder" popovertarget="popovertarget" popovertargetaction="hide" readonly required size="5" src="src" step="1" type="button" value="value" width="width" />'
    )


def test_link():
    c = e.Link(
        as_="as",
        crossorigin="anonymous",
        fetchpriority="high",
        href="href",
        hreflang="hreflang",
        imagesizes=["one", "two"],
        imagesrcset=["one", "two"],
        integrity="integrity",
        media="media",
        referrerpolicy="no-referrer",
        rel=["one", "two"],
        sizes=["one", "two"],
        type="type",
    )
    assert (
        c.to_html(format=False)
        == '<link as="as" crossorigin="anonymous" fetchpriority="high" href="href" hreflang="hreflang" imagesizes="one, two" imagesrcset="one, two" integrity="integrity" media="media" referrerpolicy="no-referrer" rel="one two" sizes="one two" type="type" />'
    )


def test_meta():
    c = e.Meta(charset="charset", content="content", http_equiv="http", name="name")
    assert c.to_html(format=False) == '<meta charset="charset" content="content" http-equiv="http" name="name" />'


def test_source():
    c = e.Source(
        type="type",
        src="src",
        srcset=["one", "two"],
        sizes=["one", "two"],
        media="media",
        height="height",
        width="width",
    )
    assert (
        c.to_html(format=False)
        == '<source type="type" src="src" srcset="one, two" sizes="one, two" media="media" height="height" width="width" />'
    )


def test_track():
    c = e.Track(default=True, kind="subtitles", label="label", src="src", srclang="srclang")
    assert c.to_html(format=False) == '<track default kind="subtitles" label="label" src="src" srclang="srclang" />'


def test_wbr():
    c = e.Wbr()
    assert c.to_html(format=False) == "<wbr />"
