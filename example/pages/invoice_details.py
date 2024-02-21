from example.app import db
from example.atoms import basics, flexbox, forms, pages, tables
from fastapi.datastructures import URL
from reactish import components as c


def _get_top_bar(invoice: dict) -> c.BaseComponent:
    return c.Div(
        c.Div(
            c.Div(basics.Icon("arrow-left", "solid"), class_name=["level-item"]),
            c.H(
                f"Invoice {invoice['invoiceNumber']}",
                level=2,
                class_name=["title", "is-2"],
                style={
                    "white-space": "nowrap",
                    "overflow": "hidden",
                },
            ),
            class_name=["level-left"],
            style={"width": "0px", "flex-grow": "1", "margin-right": "1.5rem"},
        ),
        c.Div(
            c.Div(
                c.Button(
                    "Save", class_name=["button", "is-primary", "is-light", "is-small"], hx_patch=f"/invoice/{invoice['id']}"
                ),
                class_name=["level-item"],
            ),
            c.Div(
                c.Button(
                    "Reject",type="button",
                    class_name=["button", "is-primary", "is-warning", "is-small"],
                ),
                class_name=["level-item"],
            ),
            c.Div(
                c.Button("Submit", type="button", class_name=["button", "is-primary", "is-small"]),
                class_name=["level-item"],
            ),
            class_name=["level-right"],
        ),
        class_name=["level", "block"],
    )


def _get_invoice_details(invoice: dict) -> c.BaseComponent:
    origin = "Origin: anton.demeester@yokoy.ai | Company: Anton Company" # TODO
    return c.Div(
        flexbox.Columns(
            c.Div(c.H(f"Invoice Overview", level=2), basics.Tag(invoice['status'], color="green")),
            basics.Tooltip(c.P(origin), tooltip_text=origin),
        ),
        forms.FormField(
            type="text",
            label="Invoice Number",
            name="invoiceNumber",
            placeholder="Invoice Number",
            value=invoice["invoiceNumber"],
        ),
        forms.FormSelect(
            options=[{"label": s["name"], "value": s["id"]} for s in db.suppliers],
            label="Supplier",
            selected=invoice["supplierId"],
        ),
        forms.FormSelect(
            options=[
                {"label": s["name"], "value": s["id"]}
                for s in db.purchase_orders
                if s["supplierId"] == invoice["supplierId"]
            ],
            label="Purchase Order",
            selected="1",
        ),
        forms.CombinedFormField(
            forms.FormSelect(options=db.currencies, selected=invoice["currency"]),
            forms.FormField(type="number", value=invoice["totalClaim"]),
            label="Total Claim",
        ),
        forms.FormField(
            type="date",
            label="Issue Date",
            name="issueDate",
            placeholder="Issue Date",
            value=invoice["issueDate"],
        ),
        forms.FormField(
            type="date",
            label="Due Date",
            name="dueDate",
            placeholder="Due Date",
            value=invoice["dueDate"],
        ),
        forms.FormMultiSelect(
            label="Submitters",
            name="submitters",
            options=[{"label": u["name"], "value": u["id"]} for u in db.users],
            selected=invoice.get("submitter", []),
        ),
        forms.TextAreaFormField(
            label="Comment",
            name="comment",
            placeholder="Comment",
            value="Blabla comment with newline.\nSomething new",
        ),
    )


def _get_invoice_details_wide(invoice: dict) -> c.BaseComponent:
    return flexbox.Columns(
        c.Div(
            c.Object(
                c.P("Could not display PDF"),
                data="/static/pdf/test.pdf", # TODO from invoice
                type="application/pdf",
                style={"width": "100%", "height": "100%"},
            ),
            class_name="is-half",
            style={"height": "100%"},
        ),
        c.Div(
            _get_invoice_details(invoice=invoice),
            class_name="is-half",
            style={
                "height": "100%",
                "overflow-y": "scroll",
                "overflow-x": "hidden",
                "padding-right": "0.75rem",
            },
        ),
        style={"height": "calc(50vh - 54px)"},
    )


def _get_line_item_table(invoice: dict) -> c.BaseComponent:
    return tables.BasicTable(
        invoice['lineItems'],
        [
            {
                "label": c.Input(type="checkbox"),
                "value_generator": lambda _, __: c.Input(type="checkbox"),
            },
            {
                "label": "Description",
                "value_generator": lambda item, i: forms.FormField(
                    type="text",
                    value=item["description"],
                    name=f"lineItems.{i}.description",
                    style={"border": "none", "box-shadow": "none"}
                ),
                "width": "200px",
            },
            {
                "label": "Category",
                "value_generator": lambda item, i: forms.FormSelect(
                    [{"label": c["name"], "value": c["id"]} for c in db.categories],
                    selected=[item.get("categoryId", None)],
                    name=f"lineItems.{i}.categoryId",
                    style={"border": "none", "box-shadow": "none"}
                ),
                "width": "200px",
            },
            {
                "label": "Cost Object",
                "value_generator": lambda item, i: forms.FormSelect(
                    [{"label": c["name"], "value": c["id"]} for c in db.cost_objects],
                    selected=[item.get("costObjectId", None)],
                    name=f"lineItems.{i}.costObjectId",
                    style={"border": "none", "box-shadow": "none"}
                ),
                "width": "200px",
            },
            {
                "label": "Quantity",
                "value_generator": lambda item, i: forms.FormField(
                    type="number",
                    value=item["quantity"],
                    name=f"lineItems.{i}.quantity",
                    style={"border": "none", "box-shadow": "none"}
                ),
                "width": "100px",
            },
            {
                "label": "Tax Rate",
                "value_generator": lambda item, i: forms.FormSelect(
                    [{"label": c["name"], "value": c["id"]} for c in db.tax_rates],
                    selected=[item.get("taxRateId", None)],
                    name=f"lineItems.{i}.taxRateId",
                    style={"border": "none", "box-shadow": "none"}
                ),
                "width": "200px",
            },
            {
                "label": "Net",
                "value_generator": lambda item, i: forms.FormField(
                    type="number",
                    value=item["net"],
                    name=f"lineItems.{i}.net",
                    style={"border": "none", "box-shadow": "none"}
                ),
                "width": "100px",
            },
            {
                "label": "Gross",
                "value_generator": lambda item, i: forms.FormField(
                    type="number",
                    value=item["gross"],
                    name=f"lineItems.{i}.gross",
                    style={"border": "none", "box-shadow": "none"}
                ),
                "width": "100px",
            },
            {
                "label": "",
                "value_generator": lambda _, __: c.Div(
                    basics.Icon("copy", "regular"),
                    basics.Icon("trash", "solid", color="danger"),
                ),
            },
        ],
    )


def _get_line_item_tab(invoice: dict) -> c.BaseComponent:
    return c.Div(
        c.Div( # TODO from invoice
            basics.Notification(
                c.Span(
                    c.Strong("Warning 64.85 CHF"),
                    "Mismatch between total and sum of line items",
                ),
                icon="bell",
                icon_group="solid",
                has_delete=False,
                color="is-warning",
                is_light=True,
            ),
            basics.Notification(
                c.Span(
                    c.Strong("Smart coding"),
                    "Cost object, category and tag selection suggested by Yokoy AI",
                ),
                icon="check",
                icon_group="solid",
                has_delete=False,
                color="is-success",
                is_light=True,
            ),
            # class_name=["row", "is-narrow"]
        ),
        c.Div(_get_line_item_table(invoice=invoice), class_name=["row"], style={"overflow": "auto"}),
        style={"display": "flex", "flex-flow": "column", "height": "100%"},
    )


def _get_history_tab(invoice: dict) -> c.BaseComponent:
    data = invoice["history"]
    elements: list[c.BaseComponent] = []
    for item in data:
        elements.append(
            c.Div(
                c.Div(
                    c.P(f"{item['user']} - {item['created']}"),
                    c.P(c.Strong(f"{item['type']}"), f"{item['text'] or ''}"),
                ),
                class_name="box",
            )
        )
    return c.Div(*elements, style={"overflow": "auto", "height": "calc(100% - 100px)"})


def _get_tab_data(invoice: dict, selected: str = "") -> c.BaseComponent:
    match selected:
        case "lineItems":
            return _get_line_item_tab(invoice)
        case "history":
            return _get_history_tab(invoice)
        case _:
            return _get_line_item_tab(invoice)


def get_line_item_section(invoice: dict, selected: str = "") -> c.BaseComponent:
    return c.Div(
        basics.Tabs(
            [
                {"label": "Line Items", "value": "lineItems"},
                {"label": "History", "value": "history"},
                {"label": "Approver", "value": "approver"},
                {"label": "Documents", "value": "documents"},
                {"label": "Related Invoice", "value": "relatedInvoices"},
            ],
            base=URL(f"/invoices/{invoice['id']}/tabs"),
            hx_target="#line-item-section",
            hx_push_url="false",
            selected=selected or "lineItems",
        ),
        c.Div(
            _get_tab_data(invoice=invoice, selected=selected),
            id="invoiceTabData",
            style={"height": "calc(100% - 30px - 1.5rem)"}
            # class_name=["rows", "row"],
        ),
        id="line-item-section",
        style={
            "height": "calc(50vh - 30px)",
            "border-top": "1px solid lightgrey",
        },
        # class_name=["rows"]
    )


def get_invoice_detail_page(invoice: dict) -> c.BaseComponent:
    page = pages.BasePage(
        flexbox.Rows(
            c.Form(
                c.Div(
                    _get_top_bar(invoice=invoice),
                    _get_invoice_details_wide(invoice=invoice),
                ),
                c.Div(get_line_item_section(invoice=invoice)),
            ),
        ),
        selected="invoices",
    )
    return page
