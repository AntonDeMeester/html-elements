from reactish import components as c

from example.atoms import flexbox, forms, pages, tables

statuses = [
    {"label": "Draft", "value": "draft"},
    {"label": "New", "value": "new"},
    {"label": "Needs revision", "value": "needsRevision"},
    {"label": "In Approval", "value": "inApproval"},
    {"label": "In Review", "value": "inReview"},
    {"label": "Ready for Export", "value": "readyForExport"},
    {"label": "Exported", "value": "exported"},
    {"label": "Rejected", "value": "rejected"},
]
pagination = tables.Pagination(
    current=5,
    show_first=True,
    show_last=True,
    last=11,
    number_of_pages_around_current=1,
)

invoices = [
    {
        "warning": False,
        "supplier": "Supplier 1",
        "supplierId": "1234",
        "totalClaim": 100,
        "currency": "CHF",
        "invoiceNumber": "INVOICE 1",
        "issueDate": "01/01/2023",
        "dueDate": "01/03/2023",
        "submitter": ["Anton De Meester"],
        "approver": ["Katarina Kostic"],
        "status": "inApproval",
    },
    {
        "warning": True,
        "supplier": "Supplier 2",
        "supplierId": "1232",
        "totalClaim": 77.5,
        "currency": "EUR",
        "invoiceNumber": "INVOICE 2",
        "issueDate": "02/01/2023",
        "dueDate": "01/05/2023",
        "submitter": ["Arnold Schumacher"],
        "approver": None,
        "status": "draft",
    },
    {
        "warning": False,
        "supplier": "Supplier 4",
        "supplierId": "1235",
        "totalClaim": 99,
        "currency": "CHF",
        "invoiceNumber": "INVOICE 3",
        "issueDate": "31/01/2023",
        "dueDate": "01/03/2023",
        "submitter": ["Benedikt Cucumber"],
        "approver": ["Devis The Boss"],
        "status": "inReview",
    },
    {
        "warning": False,
        "supplier": "Supplier 2",
        "supplierId": "1232",
        "totalClaim": 901,
        "currency": "CHF",
        "invoiceNumber": "INVOICE 100",
        "issueDate": "29/02/2024",
        "dueDate": "01/05/2025",
        "submitter": ["Robert Not of Hear-o"],
        "approver": ["Devis The Boss"],
        "status": "inReview",
    },
    {
        "warning": True,
        "supplier": "Supplier 3",
        "supplierId": "1239",
        "totalClaim": 400,
        "currency": "EUR",
        "invoiceNumber": "INVOICE -1",
        "issueDate": "02/09/1993",
        "dueDate": "01/03/1995",
        "submitter": ["That guy from Hamilton"],
        "approver": ["Mike The Sub-boss"],
        "status": "exported",
    },
    {
        "warning": True,
        "supplier": "Supplier 1",
        "supplierId": "1234",
        "totalClaim": 401.123,
        "currency": "CHF",
        "invoiceNumber": "SOMETHING",
        "issueDate": "06/07/1992",
        "dueDate": "01/03/1993",
        "submitter": ["Tomis Cruising"],
        "approver": None,
        "status": "readyForExport",
    },
    {
        "warning": False,
        "supplier": "Supplier 0",
        "supplierId": "000",
        "totalClaim": 231,
        "currency": "CHF",
        "invoiceNumber": "Hello",
        "issueDate": "01/01/2000",
        "dueDate": "01/03/2001",
        "submitter": ["Ikea Matata"],
        "approver": None,
        "status": "new",
    },
    {
        "warning": True,
        "supplier": "Supplier 11",
        "supplierId": "fjewifw",
        "totalClaim": 99,
        "currency": "USD",
        "invoiceNumber": "woops",
        "issueDate": "01/01/2023",
        "dueDate": "01/03/2023",
        "submitter": ["Yokoy Bot"],
        "approver": ["Phil the Real Boss"],
        "status": "new",
    },
]

table = tables.BasicTable(
    invoices,
    [
        {"label": "Warning", "attr": "warning"},
        {"label": "Supplier", "attr": "supplier"},
        {"label": "Supplier ID", "attr": "supplierId"},
        {
            "label": "Total Claim",
            "value_generator": lambda item: f"{item['currency']} {item['totalClaim']:.2f}",
        },
        {"label": "Currency", "attr": "currency"},
        {"label": "Invoice No.", "attr": "invoiceNumber"},
        {
            "label": "Issue Date",
            "attr": "issueDate",
            # "value_generator": lambda item: f"{item['issueDate']:%Y/%m/%d}",
        },
        {
            "label": "Due Date",
            "attr": "dueDate",
            # "value_generator": lambda item: f"{item['dueDate']:%Y/%m/%d}",
        },
        {
            "label": "Submitter",
            "value_generator": lambda item: ", ".join(
                item["submitter"] if item["submitter"] is not None else []
            ),
        },
        {
            "label": "Current Approver",
            "value_generator": lambda item: ", ".join(
                item["approver"] if item["approver"] is not None else []
            ),
        },
        {"label": "Status", "attr": "status"},
    ],
)


content = flexbox.Rows(
    c.H("Invoices", level=1),
    forms.FormSelect(label="Status", options=statuses, multiple=True),
    c.Div(pagination, table, style={"overflow": "auto", "display": "block"}),
)
page = pages.BasePage(content, selected="invoices")

with open("test_atoms.html", "w") as f:
    f.write(page.to_html())
