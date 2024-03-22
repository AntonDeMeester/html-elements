# HTML Elements

HTML Elements allows you to write HTML website while staying completely in Python. This will allow you to create SPA-like components, but keep your presentation layer in Python.

Because it is in pure Python, it allows to use all the Python goodies such as functions, linting, type checking.

Check out the complete documentation [here](https://antondemeester.github.io/html-elements/)

## Example 

To create this form (made with [Bulma](https://bulma.io/))

```html
<form>
  <div class="field">
    <label class="label">
      Name
    </label>
    <div class="control">
      <input class="input" name="name" placeholder="Name" type="text" />
    </div>
  </div>
  <div class="field">
    <label class="label">
      Email
    </label>
    <div class="control">
      <input class="input" name="email" placeholder="Email" type="email" />
    </div>
  </div>
  <button class="button" type="submit">
    Submit
  </button>
</form>
```

You write

```python
from html_elements import elements as e


def Input(type: str, label: str) -> e.BaseHtmlElement:
    display = label.title()
    return e.Div(
        [
            e.Label([display], classes=["label"]),
            e.Div(
                [e.Input(classes=["input"], type=type, placeholder=display, name=label)],
                classes=["control"]
            )
        ],
        classes=["field"]
    )

html = e.Form([
    Input("text", "name"),
    Input("email", "email"),
    e.Button(["Submit"], classes=["button"], type="submit")
])

raw = html.to_html(indent_step=2)
```