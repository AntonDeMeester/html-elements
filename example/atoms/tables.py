import sys
from typing import Any, Callable, Literal, TypedDict, TypeVar
from urllib.parse import parse_qs, urlencode, urlparse

from example.atoms import basics
from fastapi.datastructures import URL
from reactish import components as c
from reactish.base import BaseComponent

T = TypeVar("T")


class Sort(TypedDict):
    field: str
    direction: Literal["asc", "desc"]


def get_field_or_key(obj: Any, key: str) -> Any:
    try:
        return getattr(obj, key)
    except AttributeError:
        pass
    try:
        return obj[key]
    except (KeyError, TypeError):
        return None


class ColumnDef(TypedDict, total=False):
    label: str | c.BaseComponent
    attr: str
    value_generator: Callable[[Any, int], str | BaseComponent]
    width: str


def BasicTable(
    items: list[T],
    columns: list[ColumnDef[T]],
    on_row_click: Callable[[T, int], str] | None = None,
    sortable: bool = False,
    active_sort: Sort | None = None,
    current_url: URL | None = None,
) -> BaseComponent:
    header_cells: list[c.BaseComponent] = []
    for col in columns:
        hx = {}
        header_classes = ""
        col_text = (
            c.Span(col["label"]) if isinstance(col["label"], str) else col["label"]
        )
        style ={
                    "white-space": "nowrap"
                }
        if width := col.get("width", None):
            style["min-width"] = width
            style["max-width"] = width
        if sortable and "attr" in col:
            if not current_url:
                raise ValueError("Need a current URL to enable sorting")
            new_url = current_url.include_query_params(
                sort_by=col["attr"], sort_order="asc"
            )
            if active_sort and active_sort["field"] == col["attr"]:
                if active_sort["direction"] == "asc":
                    new_url = new_url.include_query_params(sort_order="desc")
                # Allow for resetting of sorting
                elif active_sort["direction"] == "desc":
                    new_url = new_url.remove_query_params(["sort_by", "sort_order"])
            hx = {
                "hx_get": str(new_url),
                "hx_push_url": "true",
            }
            header_classes = "pointer-on-hover"
            if active_sort and active_sort["field"] == col["attr"]:
                col_text = c.Span(
                    c.Span(col["label"]),
                    basics.Icon(
                        "arrow-up"
                        if active_sort["direction"] == "asc"
                        else "arrow-down",
                        "solid is-small has-text-grey",
                    ),
                    class_name="icon-text is-small",
                    style={"flex-wrap": "nowrap"},
                )

        header_cells.append(
            c.Th(
                col_text,
                style=style,
                class_name=header_classes,
                **hx,
            )
        )
    rows: list[c.Tr] = []
    for i, item in enumerate(items):
        cells: list[c.Td] = []
        for col in columns:
            if attr := col.get("attr", None):
                value = get_field_or_key(item, attr)
            elif gen := col.get("value_generator", None):
                value = gen(item, i)
            else:
                raise ValueError("Needs either Attr or Value Generator")
            cells.append(c.Td(value, style={"white-space": "nowrap"}))
        if on_row_click:
            on_click = on_row_click(item, i)
            classes = "pointer-on-hover"
        else:
            on_click = None
            classes = None
        rows.append(c.Tr(*cells, onclick=on_click, class_name=classes))
    return c.Div(
        c.Table(
            c.Thead(
                *header_cells,
                style={
                    "position": "sticky",
                    "top": "0px",
                    "background": "white",
                    "z-index": "5",
                },
            ),
            c.Tbody(*rows),
            class_name=["table", "is-fullwidth", "is-hoverable"],
            id="table",
        ),
        class_name=["table-container"],
        style={"overflow": "unset"},
    )


PAGE = "/invoices"


def Pagination(
    *,
    show_first: bool = True,
    show_last=True,
    last: int | None = None,
    current: int = 1,
    number_of_pages_around_current: int = 1,
    page_url: URL | None = None,
) -> BaseComponent:
    next_prev = []
    if current > 1:
        next_prev.append(
            c.A(
                "Previous",
                class_name="pagination-previous",
                href=page_url.include_query_params(page=str(current - 1)),
            )
        )
    if last and current < last:
        next_prev.append(
            c.A(
                "Next",
                class_name="pagination-next",
                href=page_url.include_query_params(page=str(current + 1)),
            )
        )
    pages: list[BaseComponent] = []

    start_range = max(1, current - number_of_pages_around_current)
    end_range = min(last or sys.maxsize, current + number_of_pages_around_current)

    if show_first and start_range > 1:
        pages.append(
            c.Li(
                c.A(
                    "1",
                    class_name="pagination-link",
                    aria={"label": "Go to page 1"},
                    href=page_url.include_query_params(page=str(1)),
                ),
            )
        )

    # Add ... for fanciness
    if start_range > 2:
        pages.append(c.Li(c.Span("&hellip;", class_name="pagination-ellipsis")))
    for page_number in range(start_range, end_range + 1):
        if page_number == current:
            pages.append(
                c.Li(
                    c.A(
                        str(page_number),
                        class_name=["pagination-link", "is-current"],
                        aria={"label": f"Page {page_number}", "current": "page"},
                        href=page_url.include_query_params(page=str(page_number)),
                    )
                )
            )
        else:
            pages.append(
                c.Li(
                    c.A(
                        str(page_number),
                        class_name="pagination-link",
                        aria={"label": f"Go to page {page_number}"},
                        href=page_url.include_query_params(page=str(page_number)),
                    )
                )
            )

    if show_last:
        if last is None:
            raise ValueError("Show last was provided but no last page was set")
        if last > page_number + 1:
            pages.append(c.Li(c.Span("&hellip;", class_name="pagination-ellipsis")))
        if last > end_range:
            pages.append(
                c.Li(
                    c.A(
                        str(last),
                        class_name="pagination-link",
                        aria={"label": f"Go to page {last}"},
                        href=page_url.include_query_params(page=str(last)),
                    )
                )
            )

    page_list = c.Ul(*pages, class_name="pagination-list")
    return c.Nav(
        *next_prev,
        page_list,
        # role="navigation",
        aria={"label": "pagination"},
        class_name="pagination",
    )
