import math
from typing import Annotated, Literal

from example.app import db, htmx
from example.pages import invoice_details, invoices_table
from fastapi import Depends, FastAPI, Query, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="example/static"), name="static")
INVOICES_PER_PAGE = 5


def _get_query_params_as_lists(request: Request) -> dict[str, list[str]]:
    result = {}
    for key, value in request.query_params.multi_items():
        if key in result:
            result[key].append(value)
        else:
            result[key] = [value]
    return result


QueryParams = Annotated[dict[str, list[str]], Depends(_get_query_params_as_lists)]


@app.get("/invoices")
def get_invoices_request(
    request: Request,
    is_htmx: htmx.is_htmx_dependency = False,
    page: int = 1,
    status: list[str] = Query([]),
    invoiceNumber: str | None = None,
    entity: str | None = None,
    sort_by: str | None = None,
    sort_order: str | None = None,
) -> HTMLResponse:
    if any(not s for s in status):
        status = []
    invoices = get_all_invoices(status=status, invoiceNumber=invoiceNumber, entity=entity)
    total_invoices = len(invoices)
    max_pages = math.ceil(total_invoices / INVOICES_PER_PAGE)
    relevant_invoices = get_relevant_invoices(invoices, page, INVOICES_PER_PAGE, sort_by=sort_by, sort_order=sort_order)
    if is_htmx:
        html_page = invoices_table.get_invoice_table(
            invoices=relevant_invoices,
            page=page or 1,
            max_pages=max_pages,
            url=request.url,
            sort_by=sort_by,
            sort_order=sort_order,
        )
    else:
        html_page = invoices_table.get_invoice_table_page(
            statuses=db.statuses,
            entities=db.entities,
            invoices=relevant_invoices,
            page=page or 1,
            max_pages=max_pages,
            url=request.url,
            selected={
                "status": status,
                "entity": entity,
                "invoiceNumber": invoiceNumber,
            },
            sort_by=sort_by,
            sort_order=sort_order,
        )
    return HTMLResponse(html_page.to_html())


@app.delete("/invoices/{id}")
def delete_invoices_request(id: str) -> HTMLResponse:
    return Response("", status_code=200)


@app.get("/invoices/{id}")
def get_details_invoices_request(id: str) -> HTMLResponse:
    inv = get_invoice(id)
    if inv is None:
        return Response("Not Found", status_code=404)
    return HTMLResponse(invoice_details.get_invoice_detail_page(inv).to_html(), status_code=200)


@app.get("/invoices/{id}/tabs/{tab}")
def get_details_invoices_request(
    id: str,
    tab: str | None = None,
) -> HTMLResponse:
    inv = get_invoice(id)
    if inv is None:
        return Response("Not Found", status_code=404)
    return HTMLResponse(
        invoice_details.get_line_item_section(invoice=inv, selected=tab).to_html(),
        status_code=200,
    )


@app.post("/invoices/{id}/supplier/{supplierId}")
def get_details_invoice_change_supplier(supplierId: str):
    inv = get_invoice(id)
    if inv is None:
        return Response("Not Found", status_code=404)


def get_invoice(id: str) -> dict:
    inv = list(filter(lambda x: x["id"] == id, db.invoices))
    return inv[0] if inv else None


def get_all_invoices(
    status: list[str] | None = None,
    invoiceNumber: str | None = None,
    entity: str | None = None,
    remove: str | None = None,
) -> list[dict]:
    filtered_invoices = db.invoices
    if status:
        filtered_invoices = [inv for inv in filtered_invoices if inv["status"] in status]
    if entity:
        filtered_invoices = [inv for inv in filtered_invoices if entity == inv["entity"]]
    if invoiceNumber:
        filtered_invoices = [inv for inv in filtered_invoices if invoiceNumber.lower() in inv["invoiceNumber"].lower()]
    if remove:
        filtered_invoices = [inv for inv in filtered_invoices if remove != inv["id"]]
    return filtered_invoices


def get_relevant_invoices(
    invoices: list[dict],
    page: int,
    page_size: int,
    sort_by: str | None = None,
    sort_order: Literal["asc", "desc"] | None = None,
) -> list[dict]:
    if sort_by:
        is_descending = sort_order == "desc"
        invoices = sorted(invoices, key=lambda x: x.get(sort_by, None), reverse=is_descending)
    return invoices[(page - 1) * page_size : page * page_size]
