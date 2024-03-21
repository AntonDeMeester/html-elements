from abc import ABC, ABCMeta
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Dict, List, Literal, Tuple, Type, TypedDict, Union

from typing_extensions import dataclass_transform

Undefined = object()
HtmlAttributeType = Literal["attribute", "content"]


class HtmlAttributeInfo:
    def __init__(
        self,
        *,
        html_attribute: Union[str, None] = None,
        transformer: Union[Callable[[Any], str], None] = None,
        # For aria / dicts which needs their own attributes but are grouped together. Needs to be a dict
        multi_attribute: bool = False,
        attribute_type: HtmlAttributeType = "attribute",
        # Field specifiers https://typing.readthedocs.io/en/latest/spec/dataclasses.html#field-specifiers
        default: Any = Undefined,
        default_factory: Union[Callable[[], Any], None] = None,
        init: bool = True,
        kw_only: bool = True,
    ):
        self.html_attribute = html_attribute
        self.transformer = transformer
        self.multi_attribute = multi_attribute
        self.attribute_type = attribute_type
        self.init = init
        self.default = default
        self.default_factory = default_factory
        self.kw_only = kw_only

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        fields = (
            "html_attribute",
            "transformer",
            "multi_attribute",
            "attribute_type",
            "init",
            "default",
            "default_factory",
            "kw_only",
        )
        for f in fields:
            if getattr(self, f) != getattr(other, f):
                return False
        return True

    def has_default(self) -> bool:
        return self.default is not Undefined or self.default_factory is not None


def HtmlAttribute(
    *,
    html_attribute: Union[str, None] = None,
    transformer: Union[Callable[[Any], str], None] = None,
    # For aria / dicts which needs their own attributes but are grouped together. Needs to be a dict
    multi_attribute: bool = False,
    attribute_type: HtmlAttributeType = "attribute",
    # Field specifiers https://typing.readthedocs.io/en/latest/spec/dataclasses.html#field-specifiers
    default: Any = Undefined,
    default_factory: Union[Callable[[], Any], None] = None,
    init: bool = True,
    kw_only: bool = True,
) -> Any:
    """
    Creates a new HTML Attribute to include in the output HTML values
    """
    if default is not Undefined and default_factory is not None:
        raise ValueError("Cannot set both default and default factory on an HTML Attribute")
    return HtmlAttributeInfo(
        html_attribute=html_attribute,
        transformer=transformer,
        multi_attribute=multi_attribute,
        attribute_type=attribute_type,
        init=init,
        default=default,
        default_factory=default_factory,
        kw_only=kw_only,
    )


@dataclass_transform(
    field_specifiers=(HtmlAttribute, HtmlAttributeInfo),
    kw_only_default=True,
    eq_default=False,
    order_default=False,
)
class HtmlMetaClass(ABCMeta):
    def __new__(
        cls,
        cls_name: str,
        bases: Tuple[Type[Any], ...],
        namespace: Dict[str, Any],
        **kwargs: Any,
    ) -> type:
        attributes: Dict[str, HtmlAttributeInfo] = {}
        config: HtmlElementConfig = {
            "tag_omission": False,
            "tag": "",
        }
        tag = kwargs.pop("tag", None)
        for base in reversed(bases):
            attributes.update(getattr(base, "__html_attributes__", {}))
        for key, value in namespace.items():
            if key.endswith("__") and key.startswith("__"):
                continue
            if not isinstance(value, HtmlAttributeInfo):
                continue
            attributes[key] = value
        if not tag and ABC not in bases:
            raise TypeError("Cannot create a HTML component without a tag")
        if tag:
            config["tag"] = tag
        if "tag_omission" in kwargs:
            config["tag_omission"] = kwargs.pop("tag_omission")

        new_namespace = {
            "__html_attributes__": attributes,
            "__html_config__": config,
            **{key: value for key, value in namespace.items() if key not in attributes},
        }

        new_cls = super().__new__(cls, cls_name, bases, new_namespace, **kwargs)
        return new_cls


class HtmlElementConfig(TypedDict):
    tag_omission: bool
    tag: str


class BaseHtmlElement(ABC, metaclass=HtmlMetaClass):
    __html_subclasses__: ClassVar[List[Type["BaseHtmlElement"]]] = []

    # Defined on Metaclass
    if TYPE_CHECKING:
        __html_attributes__: ClassVar[Dict[str, HtmlAttributeInfo]]
        __html_config__: ClassVar[HtmlElementConfig]

    def __init_subclass__(cls, *_args: Any, **_kwargs: Any):
        super().__init_subclass__()
        cls.__html_subclasses__.append(cls)

    def __init__(self, *args: Any, **kwargs: Any):
        # yes, this is basically reimplementing dataclasses __init__ but dataclass_transform doesn't work well if it has @dataclass
        non_kw_attributes = [k for k, v in self.__html_attributes__.items() if v.kw_only is False]
        non_kw_attributes_without_default = [
            k for k, v in self.__html_attributes__.items() if v.kw_only is False and not v.has_default()
        ]
        i = -1
        for i, value in enumerate(args):
            try:
                field = non_kw_attributes[i]
            except IndexError:
                min_args = len(non_kw_attributes_without_default)
                max_args = len(non_kw_attributes)
                raise TypeError(
                    f"{self.__class__.__name__}() takes {min_args} to {max_args} arguments but {len(args)} were given"
                )
            if field in kwargs:
                raise TypeError(f"Got multiple values for argument '{field}'")
            kwargs[field] = value

        not_provided_args = [v for v in non_kw_attributes_without_default if v not in kwargs]
        if (missing := len(not_provided_args) - len(args)) > 0:
            raise TypeError(
                f"{self.__class__.__name__}() missing {missing} required positional arguments: "
                + ", ".join(non_kw_attributes_without_default[len(args) :])
            )

        errors: List[str] = []
        for field, attribute in self.__html_attributes__.items():
            if field in kwargs:
                setattr(self, field, kwargs.pop(field))
            elif attribute.default is not Undefined:
                setattr(self, field, attribute.default)
            elif attribute.default_factory is not None:
                setattr(self, field, attribute.default_factory())
            else:
                errors.append(field)
        if errors:
            raise TypeError(
                f"{self.__class__.__name__}() missing {len(errors)} required keyword-only arguments: "
                + " and ".join(f"'{f}'" for f in errors)
            )
        # Random other kwargs
        for field, value in kwargs.items():
            setattr(self, field, value)

    def to_html(self, indent: int = 0, indent_step: int = 2, format: bool = True) -> str:
        # https://github.com/justpy-org/justpy/blob/master/justpy/htmlcomponents.py#L459C5-L474C17
        block_indent = " " * indent if format else ""
        endline = "\n" if format else ""
        html_tag = self.get_config_value("tag")
        html_string = f"{block_indent}<{html_tag}"

        for key, attribute in self.__html_attributes__.items():
            if attribute.attribute_type != "attribute":
                continue
            value = getattr(self, key, None)
            new_attribute = format_attribute(key, value, attribute)
            if new_attribute:
                html_string += f" {new_attribute}"

        content: List[Tuple[Union[str, "BaseHtmlElement", Any], HtmlAttributeInfo]] = []
        for key, attribute in self.__html_attributes__.items():
            if attribute.attribute_type != "content":
                continue
            child = getattr(self, key, None)
            if not child:
                continue
            # Add lists/iterables properly, but make sure not to just add strings as a list
            if isinstance(child, str) or not hasattr(child, "__iter__"):
                content.append((child, attribute))
            else:
                content.extend((c, attribute) for c in child)

        if content:
            html_string += f">{endline}"
            new_indent_amount = indent + indent_step if format else 0
            for c, attribute in content:
                if isinstance(c, BaseHtmlElement):
                    html_string += c.to_html(indent=new_indent_amount, indent_step=indent_step, format=format)
                else:
                    if attribute.transformer:
                        value = attribute.transformer(c)
                    else:
                        value = str(c)
                    new_indent = " " * new_indent_amount
                    html_string += f"{new_indent}{value}{endline}"

            html_string += f"{block_indent}</{html_tag}>{endline}"
        else:
            if self.get_config_value("tag_omission"):
                html_string += f" />{endline}"
            else:
                html_string += f"></{html_tag}>{endline}"

        return html_string

    @classmethod
    def get_config_value(cls, value: Literal["tag_omission", "tag"]) -> Any:
        return cls.__html_config__[value]

    def __str__(self) -> str:
        return self.to_html()

    def __repr__(self) -> str:
        return f"<{self.__html_config__['tag']}> field"


def format_attribute(key: str, value: Any, attribute: HtmlAttributeInfo, inner_multi: bool = False) -> str:
    """
    Formats the attribute to add to the html attributes.
    Depending on the value and attribute config, this can add zero, one or more attributes
    Returns the attribute to add e.g. `selected`, `type="button"` or `aria-type="button" aria-checked="false"`
    """
    html_attribute = attribute.html_attribute or key if not inner_multi else key
    if value is None:
        return ""
    if not inner_multi and attribute.multi_attribute:
        # For an aria dict, treat each value as
        formatted = [
            format_attribute(f"{html_attribute}-{sub_key}", sub_value, attribute, inner_multi=True)
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
    if value == "":
        return ""
    return f'{html_attribute}="{value}"'
