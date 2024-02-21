from reactish import components as c

from example.atoms import flexbox, forms, pages

content = pages.BasePage(
    c.Section(
        c.Div(
            flexbox.Columns(
                c.Div(
                    c.A(
                        "Back",
                        class_name="button",
                        href="https://opulent-rotary-phone-rrrrg74gpxf5xx5-8000.app.github.dev/snapshots",
                    ),
                    class_name="is-narrow",
                ),
                c.Div(c.H("New snapshot", level=1, class_name="title")),
            ),
            forms.ComplexForm(
                forms.FormField(
                    type="number",
                    label="Version",
                    name="name",
                    value=1,
                    placeholder="Version",
                ),
                forms.FormField(
                    type="text",
                    label="Name",
                    name="name",
                    value="Hello World",
                    placeholder="Name",
                ),
                forms.LabeledField(label="Status", value="Active"),
            ),
            class_name=["block", "container"],
        ),
        class_name="section",
    ),
    selected="invoices",
)

with open("test_atoms.html", "w") as f:
    f.write(content.to_html())
