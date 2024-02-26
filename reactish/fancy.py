from abc import ABC, ABCMeta
from typing import TYPE_CHECKING, Any, Callable, ClassVar, TypedDict, Union

from typing_extensions import dataclass_transform

Undefined = object()


class HtmlAttribute:
    def __init__(
        self,
        *,
        html_attribute: str | None = None,
        transformer: Callable[[Any], str] | None = None,
        # For aria / dicts which needs their own attributes but are grouped together. Needs to be a dict
        multi_attribute: bool = False,
        # Field specifiers https://typing.readthedocs.io/en/latest/spec/dataclasses.html#field-specifiers
        init: bool = True,
        default: Any = Undefined,
        default_factory: Callable[[], Any] | None = None,
        kw_only: bool = True,
    ):
        self.html_attribute = html_attribute
        self.transformer = transformer
        self.multi_attribute = multi_attribute
        self.init = init
        self.default = default
        self.default_factory = default_factory
        self.kw_only = kw_only


@dataclass_transform(
    field_specifiers=(HtmlAttribute,),
    kw_only_default=True,
    eq_default=False,
    order_default=False,
)
class HtmlMetaClass(ABCMeta):
    def __new__(
        mcs,
        cls_name: str,
        bases: tuple[type[Any], ...],
        namespace: dict[str, Any],
        **kwargs: Any,
    ):
        attributes: dict[str, HtmlAttribute] = {}
        config: HtmlElementConfig = {
            "tag_omission": False,
            "tag": "",
        }
        tag = kwargs.pop("tag", None)
        cls = super().__new__(
            mcs, name=cls_name, bases=bases, namespace=namespace, **kwargs
        )
        for base in reversed(bases):
            attributes.update(getattr(base, "__html_attributes__", {}))
        for key, value in namespace.items():
            if key.endswith("__") and key.startswith("__"):
                continue
            if not isinstance(value, HtmlAttribute):
                continue
            attributes[key] = value
        if not tag and ABC not in bases:
            raise TypeError("Cannot create a HTML component without a tag")
        if tag:
            config["tag"] = tag
        if "tag_omission" in kwargs:
            config["tag_omission"] = kwargs.pop("tag_omission")

        with_defaults: dict[str, Any] = {}
        for key in namespace.get("__annotations__", {}):
            value = namespace.get(key, Undefined)
            if value is Undefined or not isinstance(value, HtmlAttribute):
                continue
            if value.default_factory is None and value.default is not Undefined:
                with_defaults[key] = value.default

        new_namespace = {
            "__html_attributes__": attributes,
            "__html_config__": config,
            **with_defaults,
            **{key: value for key, value in namespace.items() if key not in attributes},
        }

        cls = super().__new__(
            mcs, name=cls_name, bases=bases, namespace=new_namespace, **kwargs
        )
        return cls


class HtmlElementConfig(TypedDict):
    tag_omission: bool
    tag: str


class BaseHtmlComponent(ABC, metaclass=HtmlMetaClass):
    __html_subclasses__: ClassVar[list[type["BaseHtmlComponent"]]] = []

    # Defined on Metaclass
    if TYPE_CHECKING:
        __html_attributes__: ClassVar[dict[str, HtmlAttribute]]
        __html_config__: ClassVar[HtmlElementConfig]

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__html_subclasses__.append(cls)

    def __init__(self, *components: Union[str, "BaseHtmlComponent"], **kwargs: Any):
        self.components = components
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_html(self, indent=0, indent_step=2, format=True) -> str:
        # https://github.com/justpy-org/justpy/blob/master/justpy/htmlcomponents.py#L459C5-L474C17
        block_indent = " " * indent if format else ""
        endline = "\n" if format else ""
        html_tag = self.get_config_value("tag")
        html_string = f"{block_indent}<{html_tag}"

        for key, attribute in self.__html_attributes__.items():
            value = getattr(self, key, None)
            new_attribute = format_attribute(key, value, attribute)
            if new_attribute:
                html_string += f" {new_attribute}"

        if components := getattr(self, "components", None):
            html_string += f">{endline}"
            new_indent_amount = indent + indent_step
            for c in components:
                if isinstance(c, BaseHtmlComponent):
                    html_string += c.to_html(
                        indent=new_indent_amount, indent_step=indent_step, format=format
                    )
                else:
                    new_indent = " " * new_indent_amount
                    html_string += f"{new_indent}{c}{endline}"
            html_string += f"{block_indent}</{html_tag}>{endline}"
        else:
            if self.get_config_value("tag_omission"):
                html_string += f" />{endline}"
            else:
                html_string += f"></{html_tag}>{endline}"

        return html_string

    @classmethod
    def get_config_value(cls, value: str) -> Any:
        return cls.__html_config__[value]

    def __str__(self) -> str:
        return self.to_html()


def format_attribute(key: str, value: Any, attribute: HtmlAttribute) -> str:
    """
    Formats the attribute to add to the html attributes.
    Depending on the value and attribute config, this can add zero, one or more attributes
    Returns the attribute to add e.g. `selected`, `type="button"` or `aria-type="button" aria-checked="false"`
    """
    html_attribute = attribute.html_attribute or key
    if value is None:
        return ""
    if attribute.multi_attribute:
        # For an aria dict, treat each value as
        formatted = [
            format_attribute(f"{html_attribute}-{sub_key}", sub_value, attribute)
            for sub_key, sub_value in value.items()
        ]
        # Don't add empty attributes
        return " ".join(i for i in formatted if i)
    if isinstance(value, bool):
        # for e.g. disabled. Only set if true
        if value:
            return f"{html_attribute}"
        return ""
    if attribute.transformer:
        value = attribute.transformer(value)
    return f'{html_attribute}="{value}"'
