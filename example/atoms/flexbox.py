from typing import Any

from reactish import components as c
from reactish.base import BaseComponent


def Columns(*columns: BaseComponent, weights: list[int] | None = None, **kwargs: Any) -> BaseComponent:
    """Creates columns with Bulma. Note, mutates the class list of each component"""
    html_columns: list[BaseComponent] = []
    for i, col in enumerate(columns):
        weight = None
        if weights:
            weight = weights[i]
        html_columns.append(
            c.Div(
                col,
                class_name=["column", "block"],
                style={"flex-grow": str(weight)} if weight is not None else None,
            )
        )
    return c.Div(*html_columns, class_name="columns", **kwargs)


def Rows(
    *rows: BaseComponent, weights: list[int] | None = None, style: dict[str, str] | None = None, **kwargs: Any
) -> BaseComponent:
    """Creates rows with Bulma. Note, mutates the class list of each component"""
    html_rows: list[BaseComponent] = []
    for i, row in enumerate(rows):
        weight = None
        if weights:
            weight = weights[i]
        html_rows.append(
            c.Div(
                row,
                class_name=["row", "block"],
                style={"flex-grow": str(weight)} if weight is not None else None,
            )
        )
    return c.Div(*html_rows, class_name="rows", style={"width": "100%", **(style or {})}, **kwargs)
