from abc import ABC, ABCMeta
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Literal, Type, TypedDict

from typing_extensions import dataclass_transform

Undefined = object()


class HtmlAttributeInfo:
    def __init__(
        self,
        *,
        html_attribute: str | None = None,
        transformer: Callable[[Any], str] | None = None,
        # For aria / dicts which needs their own attributes but are grouped together. Needs to be a dict
        multi_attribute: bool = False,
        is_attribute: bool = True,
        # Field specifiers https://typing.readthedocs.io/en/latest/spec/dataclasses.html#field-specifiers
        init: bool = True,
        default: Any = Undefined,
        default_factory: Callable[[], Any] | None = None,
        kw_only: bool = True,
    ):
        self.html_attribute = html_attribute
        self.transformer = transformer
        self.multi_attribute = multi_attribute
        self.is_attribute = is_attribute
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
            "is_attribute",
            "init",
            "default",
            "default_factory",
            "kw_only",
        )
        for f in fields:
            if getattr(self, f) != getattr(other, f):
                return False
        return True


def HtmlAttribute(
    *,
    html_attribute: str | None = None,
    transformer: Callable[[Any], str] | None = None,
    # For aria / dicts which needs their own attributes but are grouped together. Needs to be a dict
    multi_attribute: bool = False,
    is_attribute: bool = True,
    # Field specifiers https://typing.readthedocs.io/en/latest/spec/dataclasses.html#field-specifiers
    init: bool = True,
    default: Any = Undefined,
    default_factory: Callable[[], Any] | None = None,
    kw_only: bool = True,
) -> Any:
    """
    Creates a new HTML Attribute to include in the output HTML values
    """
    if default is not Undefined and default_factory is not None:
        raise ValueError(
            "Cannot set both default and default factory on an HTML Attribute"
        )
    return HtmlAttributeInfo(
        html_attribute=html_attribute,
        transformer=transformer,
        multi_attribute=multi_attribute,
        init=init,
        default=default,
        default_factory=default_factory,
        kw_only=kw_only,
        is_attribute=is_attribute,
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
        bases: tuple[type[Any], ...],
        namespace: dict[str, Any],
        **kwargs: Any,
    ) -> type:
        attributes: dict[str, HtmlAttributeInfo] = {}
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


class BaseHtmlComponent(ABC, metaclass=HtmlMetaClass):
    __html_subclasses__: ClassVar[list[type["BaseHtmlComponent"]]] = []

    # Defined on Metaclass
    if TYPE_CHECKING:
        __html_attributes__: ClassVar[dict[str, HtmlAttributeInfo]]
        __html_config__: ClassVar[HtmlElementConfig]

    def __init_subclass__(cls, *_args: Any, **_kwargs: Any):
        super().__init_subclass__()
        cls.__html_subclasses__.append(cls)

    def __init__(self, *args: Any, **kwargs: Any):
        args_index = 0
        if args:
            # Set correct args
            for field, attribute in self.__html_attributes__.items():
                # Skip Keyword only values
                if attribute.kw_only is True:
                    continue
                # Skip if the field is present with a keyword
                if field in kwargs:
                    continue
                if args_index >= len(args):
                    raise TypeError(
                        "Too many arguments combined with keyword arguments"
                    )
                kwargs[field] = args[args_index]
                args_index += 1

        for field, attribute in self.__html_attributes__.items():
            if field in kwargs:
                setattr(self, field, kwargs.pop(field))
            elif attribute.default is not Undefined:
                setattr(self, field, attribute.default)
            elif attribute.default_factory is not None:
                setattr(self, field, attribute.default_factory())
        # Random other kwargs
        for field, value in kwargs.items():
            setattr(self, field, value)

    def to_html(
        self, indent: int = 0, indent_step: int = 2, format: bool = True
    ) -> str:
        # https://github.com/justpy-org/justpy/blob/master/justpy/htmlcomponents.py#L459C5-L474C17
        block_indent = " " * indent if format else ""
        endline = "\n" if format else ""
        html_tag = self.get_config_value("tag")
        html_string = f"{block_indent}<{html_tag}"

        for key, attribute in self.__html_attributes__.items():
            if not attribute.is_attribute:
                continue
            value = getattr(self, key, None)
            new_attribute = format_attribute(key, value, attribute)
            if new_attribute:
                html_string += f" {new_attribute}"

        if components := getattr(self, "components", None):
            html_string += f">{endline}"
            new_indent_amount = indent + indent_step if format else 0
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
    def get_config_value(cls, value: Literal["tag_omission", "tag"]) -> Any:
        return cls.__html_config__[value]

    def __str__(self) -> str:
        return self.to_html()

    def __repr__(self) -> str:
        return f"<{self.__html_config__['tag']}> field"

    @classmethod
    def add_extension(cls, extension: Type["BaseHtmlComponent"]) -> None:
        """
        Adds the HTML attributes of this extension to all subclasses so that they are included
        This allows more than the MDN attributes to be included in the output HTML
        #TODO Allow for proper typing of extensions
        """
        for subcls in cls.__html_subclasses__:
            subcls.__html_attributes__ |= extension.__html_attributes__


def format_attribute(key: str, value: Any, attribute: HtmlAttributeInfo) -> str:
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
    if value == "":
        return ""
    return f'{html_attribute}="{value}"'
