from abc import ABC
from typing import Any

import pytest
from html_elements.base import BaseHtmlComponent, HtmlAttribute


class AbstractElement(BaseHtmlComponent, ABC):
    string: str | None = HtmlAttribute(default=None)
    integer: int | None = HtmlAttribute(default=None)
    floating: float | None = HtmlAttribute(default=None)
    boolean: bool | None = HtmlAttribute(default=None)
    dictionary: dict[str, str] = HtmlAttribute(
        default_factory=dict,
        transformer=lambda x: "; ".join(f"{k}={v}" for k, v in x.items()),
    )
    array: list[str] = HtmlAttribute(
        default_factory=list, transformer=lambda x: ", ".join(x)
    )
    multi_attribute: dict[str, Any] | None = HtmlAttribute(
        default_factory=dict, multi_attribute=True, html_attribute="multi"
    )
    multi_attribute_int: dict[str, int] | None = HtmlAttribute(
        default_factory=dict,
        multi_attribute=True,
        html_attribute="multint",
        transformer=lambda x: f"{x * 10}",
    )
    transformer: int | None = HtmlAttribute(default=None, transformer=lambda x: x * 10)


class InitTest(BaseHtmlComponent, tag="init"):
    non_kw: str = HtmlAttribute(kw_only=False)
    non_kw_two: str | None = HtmlAttribute(default=None, kw_only=False)
    non_kw_three: str = HtmlAttribute(default_factory=lambda: "test", kw_only=False)
    kw: str = HtmlAttribute(kw_only=True)
    kw_two: str = HtmlAttribute(kw_only=True, default="two")
    kw_three: str = HtmlAttribute(
        default_factory=lambda: "three",
    )
    other: str


class SimpleToHtmlComponent(BaseHtmlComponent, tag="easy"):
    children: list[str | BaseHtmlComponent] = HtmlAttribute(
        attribute_type="child", kw_only=False, default_factory=list
    )


class ToHtmlComponent(AbstractElement, tag="to-html"):
    children: list[str | BaseHtmlComponent] = HtmlAttribute(
        attribute_type="child", kw_only=False, default_factory=list
    )
    children_two: str = HtmlAttribute(
        attribute_type="child", kw_only=False, default=None
    )
    children_three: float = HtmlAttribute(
        attribute_type="child",
        kw_only=True,
        default=0,
        transformer=lambda x: f"{x:.2f}",
    )
    bla: str = ""


class NoTagOmission(BaseHtmlComponent, tag="no-omis", tag_omission=False):
    field: str = HtmlAttribute(attribute_type="attribute", default=None)


class TagOmission(BaseHtmlComponent, tag="omis", tag_omission=True):
    field: str = HtmlAttribute(attribute_type="attribute", default=None)


class TagOmissionWithChildren(BaseHtmlComponent, tag="omis-c", tag_omission=True):
    field: str = HtmlAttribute(attribute_type="attribute", default=None)
    children: str = HtmlAttribute(attribute_type="child", default="")


def double(x: str) -> str:
    return 2 * x


def test_basic_setup():
    class BaseElement(BaseHtmlComponent, tag="base"):
        string: str = HtmlAttribute(default=None)

    base = BaseElement(string="test")
    assert base.__html_attributes__ == {"string": HtmlAttribute(default=None)}
    assert base.__html_config__ == {"tag_omission": False, "tag": "base"}
    assert not hasattr(BaseElement, "string")
    assert BaseElement in BaseHtmlComponent.__html_subclasses__
    assert base.to_html(format=False) == '<base string="test"></base>'


def test_inheritance():
    """Elements can be inherited and overwritten"""

    class DerivedElement(AbstractElement, tag="derived"):
        new_field: str = HtmlAttribute(default=None)
        string: str = HtmlAttribute(
            default="blabla", transformer=double, html_attribute="not-string"
        )

    derived = DerivedElement(string="test", integer=5, dictionary={"this": "here"})

    assert derived.__html_attributes__["string"] == HtmlAttribute(
        default="blabla", transformer=double, html_attribute="not-string"
    )
    assert derived.__html_config__ == {"tag_omission": False, "tag": "derived"}
    assert DerivedElement in BaseHtmlComponent.__html_subclasses__
    assert (
        derived.to_html(format=False)
        == '<derived not-string="testtest" integer="5" dictionary="this=here"></derived>'
    )


def test_inheritance_is_left_to_right_priority():
    class One(BaseHtmlComponent, ABC):
        field: str = HtmlAttribute(default="one")
        one: str = HtmlAttribute(default=None)

    class Two(BaseHtmlComponent, ABC):
        field: str = HtmlAttribute(default="two")
        two: str = HtmlAttribute(default=None)

    class Three(One, Two, tag="three"):
        three: str = HtmlAttribute(default=None)

    assert Three.__html_attributes__ == {
        "field": HtmlAttribute(default="one"),
        "one": HtmlAttribute(default=None),
        "two": HtmlAttribute(default=None),
        "three": HtmlAttribute(default=None),
    }
    assert Three().to_html(format=False) == '<three field="one"></three>'


def test_non_html_attribute_is_ignored():
    class DerivedElement(AbstractElement, tag="derived"):
        new_field: str = ""

    derived = DerivedElement(new_field="hello")

    assert "new_field" not in derived.__html_attributes__
    assert derived.to_html(format=False) == "<derived></derived>"


def test_tag_required():
    with pytest.raises(TypeError):

        class Derived(BaseHtmlComponent):  # type: ignore
            pass


def test_tag_not_required_if_abc():
    class Derived(BaseHtmlComponent, ABC):  # type: ignore
        pass


def test_init_non_kw_provide_all_args():
    b = InitTest(
        "one",
        "two",
        "three",
        kw="hello",
        kw_two="--two",
        kw_three="--three",
        other="Hello",
    )
    assert b.non_kw == "one"
    assert b.non_kw_two == "two"
    assert b.non_kw_three == "three"
    assert b.kw == "hello"
    assert b.kw_two == "--two"
    assert b.kw_three == "--three"
    assert b.other == "Hello"


def test_init_non_kw_provide_least():
    b = InitTest("one", kw="hello", other="Hello")
    assert b.non_kw == "one"
    assert b.non_kw_two is None
    assert b.non_kw_three == "test"
    assert b.kw == "hello"
    assert b.kw_two == "two"
    assert b.kw_three == "three"
    assert b.other == "Hello"


def test_init_non_kw_provide_all_kw():
    b = InitTest(
        non_kw="one",
        non_kw_two="two",
        non_kw_three="three",
        kw="hello",
        kw_two="--two",
        kw_three="--three",
        other="Hello",
    )
    assert b.non_kw == "one"
    assert b.non_kw_two == "two"
    assert b.non_kw_three == "three"
    assert b.kw == "hello"
    assert b.kw_two == "--two"
    assert b.kw_three == "--three"
    assert b.other == "Hello"


def test_init_non_kw_provide_provide_too_little():
    with pytest.raises(TypeError) as e:
        InitTest(kw="hello", other="Hello")  # type: ignore
        assert (
            e.value.args[0]
            == "InitTest() missing 1 required positional arguments: 'non_kw'"
        )


def test_init_non_kw_provide_provide_too_many():
    with pytest.raises(TypeError) as e:
        InitTest("one", "two", "three", "four", kw="hello", other="Hello")  # type: ignore
        assert e.value.args[0] == "InitTest() takes 1 to 3 arguments but 4 were given"


def test_init_kw_missing():
    with pytest.raises(TypeError) as e:
        InitTest("one")  # type: ignore
        assert (
            e.value.args[0]
            == "InitTest() missing 1 required keyword-only arguments: 'kw'"
        )


def test_init_random_other_kw():
    b = InitTest("one", kw="hello", other="bliebla", foo="bar")  # type: ignore
    assert b.foo == "bar"  # type: ignore


def test_init_random_missing_other_fields():
    # We allow for non-html fields to be missing. The type checker should find this anyway
    b = InitTest("one", kw="hello")  # type: ignore
    assert not hasattr(b, "other")


def test_to_html_empty():
    c = ToHtmlComponent()
    assert c.to_html(format=False) == "<to-html></to-html>"


def test_to_html_expansive():
    c = ToHtmlComponent(
        ["test", SimpleToHtmlComponent(["something"])],
        "Hello world",
        children_three=50.5999,
        string="Hello",
        integer=5,
        floating=5.5,
        boolean=True,
        dictionary={"foo": "bar"},
        array=["one", "two", "three"],
    )
    assert (
        c.to_html()
        == """<to-html string="Hello" integer="5" floating="5.5" boolean dictionary="foo=bar" array="one, two, three">
  test
  <easy>
    something
  </easy>
  Hello world
  50.60
</to-html>
"""
    )


def test_to_html_no_format():
    c = ToHtmlComponent(
        ["test", SimpleToHtmlComponent(["something"])],
        "Hello world",
        children_three=50.5999,
        string="Hello",
        integer=5,
        floating=5.5,
        boolean=True,
        dictionary={"foo": "bar"},
        array=["one", "two", "three"],
    )
    assert (
        c.to_html(format=False, indent=4, indent_step=4)
        == """<to-html string="Hello" integer="5" floating="5.5" boolean dictionary="foo=bar" array="one, two, three">test<easy>something</easy>Hello world50.60</to-html>"""
    )


def test_to_html_indent_step():
    c = ToHtmlComponent(
        ["test", SimpleToHtmlComponent(["something"])],
        "Hello world",
        children_three=50.5999,
        string="Hello",
        integer=5,
        floating=5.5,
        boolean=True,
        dictionary={"foo": "bar"},
        array=["one", "two", "three"],
    )
    assert (
        c.to_html(indent_step=4)
        == """<to-html string="Hello" integer="5" floating="5.5" boolean dictionary="foo=bar" array="one, two, three">
    test
    <easy>
        something
    </easy>
    Hello world
    50.60
</to-html>
"""
    )


def test_to_html_indent():
    c = ToHtmlComponent(
        ["test", SimpleToHtmlComponent(["something"])],
        "Hello world",
        children_three=50.5999,
        string="Hello",
        integer=5,
        floating=5.5,
        boolean=True,
        dictionary={"foo": "bar"},
        array=["one", "two", "three"],
    )
    assert (
        c.to_html(indent=4)
        == """    <to-html string="Hello" integer="5" floating="5.5" boolean dictionary="foo=bar" array="one, two, three">
      test
      <easy>
        something
      </easy>
      Hello world
      50.60
    </to-html>
"""
    )


def test_to_html_indent_and_step_zero():
    c = ToHtmlComponent(
        ["test", SimpleToHtmlComponent(["something"])],
        "Hello world",
        children_three=50.5999,
        string="Hello",
        integer=5,
        floating=5.5,
        boolean=True,
        dictionary={"foo": "bar"},
        array=["one", "two", "three"],
    )
    assert (
        c.to_html(indent=0, indent_step=0, format=True)
        == """<to-html string="Hello" integer="5" floating="5.5" boolean dictionary="foo=bar" array="one, two, three">
test
<easy>
something
</easy>
Hello world
50.60
</to-html>
"""
    )


def test_to_html_dict():
    c = ToHtmlComponent(dictionary={"foo": "bar", "one": "two", "three": "four"})
    assert (
        c.to_html(format=False)
        == '<to-html dictionary="foo=bar; one=two; three=four"></to-html>'
    )


def test_to_html_list():
    c = ToHtmlComponent(array=["1", "2", "", "None"])
    assert c.to_html(format=False) == '<to-html array="1, 2, , None"></to-html>'


def test_to_html_empty_string():
    c = ToHtmlComponent(string="")
    assert c.to_html(format=False) == "<to-html></to-html>"


def test_to_html_boolean_true():
    c = ToHtmlComponent(boolean=True)
    assert c.to_html(format=False) == "<to-html boolean></to-html>"


def test_to_html_boolean_false():
    c = ToHtmlComponent(boolean=False)
    assert c.to_html(format=False) == "<to-html></to-html>"


def test_to_html_boolean_none():
    c = ToHtmlComponent(boolean=None)
    assert c.to_html(format=False) == "<to-html></to-html>"


def test_to_html_transformer():
    c = ToHtmlComponent(transformer=10)
    assert c.to_html(format=False) == '<to-html transformer="100"></to-html>'


def test_to_html_multi_attribute():
    c = ToHtmlComponent(
        multi_attribute={
            "foo": "bar",
            "one": "two",
            "None": None,
            "empty": "",
            "true": True,
            "false": False,
        }
    )
    assert (
        c.to_html(format=False)
        == '<to-html multi-foo="bar" multi-one="two" multi-true></to-html>'
    )


def test_to_html_multi_attribute_with_transformer():
    c = ToHtmlComponent(multi_attribute_int={"foo": 1, "bar": 5, "zero": 0})
    assert (
        c.to_html(format=False)
        == '<to-html multint-foo="10" multint-bar="50" multint-zero="0"></to-html>'
    )


def test_to_html_ignore_non_html_attributes():
    c = ToHtmlComponent(bla="hahah")
    assert c.to_html(format=False) == "<to-html></to-html>"
    assert c.bla == "hahah"


def test_to_html_children_list_string_no_format():
    c = ToHtmlComponent(children=["foo", "bar", "one", "two"])
    assert c.to_html(format=False) == "<to-html>foobaronetwo</to-html>"


def test_to_html_children_list_string_format():
    c = ToHtmlComponent(children=["foo", "bar", "one", "two"])
    assert (
        c.to_html(format=True)
        == """<to-html>
  foo
  bar
  one
  two
</to-html>
"""
    )


def test_to_html_children_list_components_format():
    c = ToHtmlComponent(
        children=[SimpleToHtmlComponent(["test"]), SimpleToHtmlComponent(["other"])]
    )
    assert (
        c.to_html(format=True)
        == """<to-html>
  <easy>
    test
  </easy>
  <easy>
    other
  </easy>
</to-html>
"""
    )


def test_to_html_children_list_components_no_format():
    c = ToHtmlComponent(
        children=[SimpleToHtmlComponent(["test"]), SimpleToHtmlComponent(["other"])]
    )
    assert (
        c.to_html(format=False)
        == """<to-html><easy>test</easy><easy>other</easy></to-html>"""
    )


def test_to_html_children_list_combined_format():
    c = ToHtmlComponent(children=[SimpleToHtmlComponent(["test"]), "other"])
    assert (
        c.to_html(format=True)
        == """<to-html>
  <easy>
    test
  </easy>
  other
</to-html>
"""
    )


def test_to_html_children_str():
    c = ToHtmlComponent(children_two="Hello")
    assert c.to_html(format=False) == """<to-html>Hello</to-html>"""


def test_to_html_children_no_list_or_str():
    c = ToHtmlComponent(children_three=50.456)
    assert c.to_html(format=False) == """<to-html>50.46</to-html>"""


def test_to_html_children_transformer():
    c = ToHtmlComponent(children_three=50.456)
    assert c.to_html(format=False) == """<to-html>50.46</to-html>"""


def test_to_html_children_combined():
    c = ToHtmlComponent(
        children=["one", "two", SimpleToHtmlComponent(["Three"]), "four"],
        children_two="Hello world",
        children_three=50.456,
    )
    assert (
        c.to_html(format=True)
        == """<to-html>
  one
  two
  <easy>
    Three
  </easy>
  four
  Hello world
  50.46
</to-html>
"""
    )


def test_to_html_tag_omission_no_children_empty():
    c = TagOmission()
    assert c.to_html(format=False) == "<omis />"


def test_to_html_tag_omission_no_children_attribute():
    c = TagOmission(field="test")
    assert c.to_html(format=False) == '<omis field="test" />'


def test_to_html_no_tag_omission_no_children_empty():
    c = NoTagOmission()
    assert c.to_html(format=False) == "<no-omis></no-omis>"


def test_to_html_no_tag_omission_no_children_attribute():
    c = NoTagOmission(field="test")
    assert c.to_html(format=False) == '<no-omis field="test"></no-omis>'


def test_to_html_tag_omission_children_optional_empty():
    c = TagOmissionWithChildren()
    assert c.to_html(format=False) == "<omis-c />"


def test_to_html_tag_omission_children_attribute_empty():
    c = TagOmissionWithChildren(field="test")
    assert c.to_html(format=False) == '<omis-c field="test" />'


def test_to_html_tag_omission_children_optional_children():
    c = TagOmissionWithChildren(children="Hello")
    assert c.to_html(format=False) == "<omis-c>Hello</omis-c>"


def test_to_html_tag_omission_children_attribute_children():
    c = TagOmissionWithChildren(children="Hello", field="test")
    assert c.to_html(format=False) == '<omis-c field="test">Hello</omis-c>'
