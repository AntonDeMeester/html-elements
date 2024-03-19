# Basic Reference

## Class `BaseHtmlElement`

The basic class with methods which all HTML Elements will use. It does not have any attributes. The `__init__` parameters will be defined by the subclasses and its defined `HtmlAttribute`s.

### Method `to_html`

```python
def to_html(self, indent: int = 0, indent_step: int = 2, format: bool = True) -> str:
    ...
```

Format the element in an HTML string. 

| Parameter     | Type   | Default | Documentation                                                                                                                                       |
| ------------- | ------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `format`      | `bool` | `False` | `True`: Formats the HTML in multiple lines, with the children in different lines.<br>`False`: Formats the HTML element and its children in one line |
| `indent`      | `int`  | 0       | How many spaces to add for each line as a baseline                                                                                                  |
| `indent_step` | `int`  | 2       | How much spaces each indentation step should add                                                                                                    |

### Method `__str__`

Returns the `to_html` method with the default values.

### Class method `get_config_value`

```python
@classmethod
def get_config_value(cls, value: Literal["tag_omission", "tag"]) -> Any:
    ...
```

Returns the class configuration value for the provided type.


| Parameter | Type                             | Default | Documentation                 |
| --------- | -------------------------------- | ------- | ----------------------------- |
| `value`   | `Literal["tag_omission", "tag"]` | \       | Which configuration to return |


## Function `HtmlAttribute`

Wrapper class around `HtmlAttributeInfo`. Used for static typers to create correct class signatures.

See `HtmlAttributeInfo` class for more information.

## Class `HtmlAttributeInfo`

```python
HtmlAttributeInfo(
    *,
    html_attribute: Union[str, None] = None,
    transformer: Union[Callable[[Any], str], None] = None,
    multi_attribute: bool = False,
    attribute_type: HtmlAttributeType = "attribute",
    init: bool = True,
    default: Any = Undefined,
    default_factory: Union[Callable[[], Any], None] = None,
    kw_only: bool = True,
)
```

Class to define which values are present on the HTML element and how to format them in the `to_html` method.

| Parameter       | Type                              | Default       | Documentation                                                                                                                                                                                                                                                                                                                                                             |
| --------------- | --------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| html_attribute  | `str`                             | `None`        | The name of the HTML attribute to provide. When not provided, it will be defaulted to the attribute on the class. Useful for when the real attribute is a Python keyword such as `for`. <br>For example `for_ = HtmlAttributeInfo(html_attribute="for")`                                                                                                                  |
| transformer     | `Callable[[Any], str]`            | `None`        | A function called in the `to_html` method. It operates on the input value to return a string to include in the HTML string. <br>For example `classes: list[str] = HtmlAttributeInfo(transformer=lambda items: ", ".join(items))`                                                                                                                                          |
| multi_attribute | `bool`                            | `False`       | A flag to indicate that there are multiple individual HTML attributes linked to this value. If this flag is true, it must be linked to a `dict` structure.<br>For example `aria: dict[str, str] = HtmlAttributeInfo(multi_attribute=True)`<br>`Element(aria={"label": "test", "type": "button"})` would be rendered as `<element aria-label="test" aria-type="button" />` |
| attribute_type  | `Literal["attribute", "content"]` | `"attribute"` | What type of HTML content this is. This is to distinguish which class attributes need to be rendered as children and which ones are attributes. Normally, there is only one children attribute, but in theory there could be multiple. Both lists and non-lists are supported.                                                                                            |
| default         | `Any`                             | `Undefined`   | The default for this field. Only one of `default` or `default_factory` can be defined at the same time.                                                                                                                                                                                                                                                                   |
| default_factory | `Callable[[], Any]`               | `None`        | `None`                                                                                                                                                                                                                                                                                                                                                                    | The default for this field if it needs to be initialised. Only one of `default` or `default_factory` can be defined at the same time. |
| init            | `bool`                            | `True`        | Whether to add this field in the `__init__` method for static typecheckers. This will actually **not** be enforced in the runtime logic, only in the static typing. See the [dataclass_transform](https://typing.readthedocs.io/en/latest/spec/dataclasses.html#dataclass-transform) documentation for more information.                                                  |
| kw_only         | `bool`                            | `True`        | Whether this field can only be provided as a keyword and not positionally in the class initialisation. This will actually **not** be enforced in the runtime logic, only in the static typing. See the [dataclass_transform](https://typing.readthedocs.io/en/latest/spec/dataclasses.html#dataclass-transform) documentation for more information.                       |