from typing import Any

import pytest
from html_elements.base import HtmlAttribute, HtmlAttributeInfo, Undefined


def test_html_attributes_values():
    attr = HtmlAttribute(
        html_attribute="test",
        transformer=lambda x: x + "bla",
        multi_attribute=True,
        attribute_type="attribute",
        init=False,
        default=None,
        default_factory=None,
        kw_only=False,
    )
    assert attr.html_attribute == "test"
    assert attr.transformer("test") == "testbla"
    assert attr.multi_attribute is True
    assert attr.attribute_type == "attribute"
    assert attr.init is False
    assert attr.default is None
    assert attr.default_factory is None
    assert attr.kw_only is False


def test_html_attribute_info_values():
    attr = HtmlAttributeInfo(
        html_attribute="test",
        transformer=lambda x: x + "bla",
        multi_attribute=True,
        attribute_type="child",
        init=False,
        default=None,
        default_factory=None,
        kw_only=False,
    )
    assert attr.html_attribute == "test"
    assert attr.transformer is not None
    assert attr.transformer("test") == "testbla"
    assert attr.multi_attribute is True
    assert attr.attribute_type == "child"
    assert attr.init is False
    assert attr.default is None
    assert attr.default_factory is None
    assert attr.kw_only is False


def test_html_attributes_defaults():
    attr = HtmlAttribute()
    assert attr.html_attribute is None
    assert attr.transformer is None
    assert attr.multi_attribute is False
    assert attr.attribute_type == "attribute"
    assert attr.init is True
    assert attr.default is Undefined
    assert attr.default_factory is None
    assert attr.kw_only is True


def test_html_attribute_info_defaults():
    attr = HtmlAttributeInfo()
    assert attr.html_attribute is None
    assert attr.transformer is None
    assert attr.multi_attribute is False
    assert attr.attribute_type == "attribute"
    assert attr.init is True
    assert attr.default is Undefined
    assert attr.default_factory is None
    assert attr.kw_only is True


def test_html_attribute_default_plus_factory_raises():
    with pytest.raises(ValueError):
        HtmlAttribute(default=None, default_factory=lambda: "test")


def test_html_attribute_has_default_false_defaults():
    attr = HtmlAttributeInfo()
    assert attr.has_default() is False


def test_html_attribute_has_default_false_not_defaults():
    attr = HtmlAttributeInfo(default=Undefined, default_factory=None)
    assert attr.has_default() is False


def test_html_attribute_has_default_true_value():
    attr = HtmlAttributeInfo(default="value")
    assert attr.has_default() is True


@pytest.mark.parametrize("value", [0, "", False, None, -0, [], {}])
def test_html_attribute_has_default_true_falsish_value(value: Any):
    attr = HtmlAttributeInfo(default=value)
    assert attr.has_default() is True


def test_html_attribute_has_default_factory():
    attr = HtmlAttributeInfo(default=lambda: 5)
    assert attr.has_default() is True


def test_html_attribute_has_default_factory_list():
    attr = HtmlAttributeInfo(default=dict)
    assert attr.has_default() is True

def test_comparison_true():
    a = HtmlAttribute()
    b = HtmlAttribute()
    assert a == b

def test_comparison_false():
    a = HtmlAttribute(default="B")
    b = HtmlAttribute(default="A")
    assert a != b

def test_comparison_different_class():
    a = HtmlAttribute(default="B")
    b = object()
    assert a != b
