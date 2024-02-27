from typing import Literal

from example.atoms import basics, flexbox, forms, pages, tables
from fastapi.datastructures import URL
from reactish import components as c


def get_invoice_table(
    invoices: list[dict],
    url: URL,
    page: int = 1,
    max_pages: int | None = None,
    sort_by: str | None = None,
    sort_order: Literal["asc", "desc"] | None = None,
) -> c.BaseComponent:
    pagination = tables.Pagination(
        current=page,
        show_first=True,
        show_last=max_pages is not None,
        last=max_pages,
        number_of_pages_around_current=1,
        page_url=url,
    )
    base_url = url.path

    table = tables.BasicTable(
        invoices,
        [
            {
                "label": "Warning",
                "value_generator": lambda item, _: (
                    basics.Tooltip(basics.Icon("bell", "solid"), "This is a warning") if item["warning"] else ""
                ),
            },
            {"label": "Supplier", "attr": "supplier"},
            {"label": "Supplier ID", "attr": "supplierId"},
            {
                "label": "Total Claim",
                "value_generator": lambda item, _: f"{item['currency']} {item['totalClaim']:.2f}",
            },
            {"label": "Currency", "attr": "currency"},
            {"label": "Invoice No.", "attr": "invoiceNumber"},
            {
                "label": "Issue Date",
                "attr": "issueDate",
                # "value_generator": lambda item, _: f"{item['issueDate']:%Y/%m/%d}",
            },
            {
                "label": "Due Date",
                "attr": "dueDate",
                # "value_generator": lambda item, _: f"{item['dueDate']:%Y/%m/%d}",
            },
            {
                "label": "Submitter",
                "value_generator": lambda item, _: ", ".join(item["submitter"] if item["submitter"] is not None else []),
            },
            {
                "label": "Current Approver",
                "value_generator": lambda item, _: ", ".join(item["approver"] if item["approver"] is not None else []),
            },
            {
                "label": "Status",
                "value_generator": lambda item, _: basics.Tag(item["status"], "primary"),
            },
            {
                "label": "Actions",
                "value_generator": lambda item, _: basics.Icon(
                    "trash",
                    "solid",
                    hx_delete=f"{base_url}/{item['id']}",
                    hx_target="closest tr",
                ),
            },
        ],
        on_row_click=lambda item, _: f"window.location = '{url.path}/{item['id']}'",
        sortable=True,
        current_url=url,
        active_sort=({"direction": sort_order or "asc", "field": sort_by} if sort_by else None),
    )

    return c.Div(
        pagination,
        table,
        id="invoice-table-container",
    )


def get_invoice_filters(
    url: URL,
    statuses: list[dict] | None = None,
    entities: list[dict] | None = None,
    selected: dict[str, list[str]] | None = None,
) -> c.BaseComponent:
    selected = selected or {}
    return c.Div(
        flexbox.Columns(
            forms.FormMultiSelect(
                label="Status",
                options=statuses or [],
                name="status",
                hx_get=url.path,
                selected=selected.get("status", []),
                allow_none=True,
            ),
            forms.FormSelect(
                label="Legal Entity",
                options=[{"label": ent["name"], "value": ent["id"]} for ent in (entities or [])],
                name="entity",
                hx_get=url.path,
                selected=selected.get("entity", []),
                allow_none=True,
            ),
            forms.FormField(
                "text",
                label="Invoice Number",
                name="invoiceNumber",
                placeholder="Invoice Number",
                value=selected.get("invoiceNumber", None),
                hx_trigger="input changed delay:500ms, search",
                hx_get=url.path,
            ),
        ),
        hx_include="[name='status'], [name='entity'], [name='invoiceNumber']",
        hx_replace_url="true",
    )


def get_invoice_table_page(
    *args,
    url: URL,
    statuses: list[dict] | None = None,
    entities: list[dict] | None = None,
    selected: dict[str, list[str]] | None = None,
    **kwargs,
) -> c.BaseComponent:
    page = pages.BasePage(
        flexbox.Rows(
            c.H("Invoices", level=1, class_name="title is-1"),
            get_invoice_filters(statuses=statuses, entities=entities, selected=selected, url=url),
            get_invoice_table(*args, url=url, **kwargs),
            hx_target="#invoice-table-container",
        ),
        selected="invoices",
    )
    return page
