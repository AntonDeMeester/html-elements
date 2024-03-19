# HTML Elements

HTML Elements allows you to write HTML website while staying completely in Python. This will allow you to create SPA-like components, but keep your presentation layer in Python.

Because it is in pure Python, it allows to use all the Python goodies such as functions, linting, type checking.

To create this form (made with [Bulma](https://bulma.io/))

```html
<form>
    <div class="field">
        <label class="label">Name</label>
        <div class="control">
            <input class="input" type="text" placeholder="Name" name="name">
        </div>
    </div>
    <div class="field">
        <label class="label">email</label>
        <div class="control">
            <input class="input" type="emaiil" placeholder="Email" name="email">
        </div>
    </div>
    <button class="button" type="submit">Submit</button>
</form>
```

You write

```python
from html_elements import elements as e

def Input(type: str, label: str) -> e.BaseHtmlElement:
    display = label.title()
    return e.Div([
        e.Label([display], classes=["label"]),
        e.Div([
            e.Input(classes=["input", type="type", placeholder=display, name=label]),
            classes=["control"]
        ])
    ])

html = e.Form([
    Input("text", "name"),
    Input("email", "email"),
    e.Button("Submit", classes=["button"], type="submit")
])

print(html.to_html())
```