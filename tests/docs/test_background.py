import pytest


def test_input_one():
    from docs_code.background import input

    assert (
        input.Input("text", "name").to_html()
        == """<div class="field">
  <label class="label">
    name
  </label>
  <div class="control">
    <input class="input" name="name" placeholder="name" type="text" />
  </div>
</div>
"""
    )


def test_input_two():
    from docs_code.background import input

    assert (
        input.InputTwo("text", "name", classes=["better-control"]).to_html()
        == """<div class="field">
  <label class="label">
    Name
  </label>
  <div class="better-control">
    <input class="input" name="name" placeholder="Name" type="text" />
  </div>
</div>
"""
    )


def test_table():
    from docs_code.background import table

    assert (
        table.raw
        == """<table class="table">
  <thead>
    <tr>
      <th>
        id
      </th>
      <th>
        name
      </th>
      <th>
        email
      </th>
    </tr>
  </thead>
  <tr>
    <td>
      1
    </td>
    <td>
      Bobby Greenfield
    </td>
    <td>
      bobby@greenfield.com
    </td>
  </tr>
  <tr>
    <td>
      2
    </td>
    <td>
      Johnny Smith
    </td>
    <td>
      johhnySmith@gmail.com
    </td>
  </tr>
  <tr>
    <td>
      3
    </td>
    <td>
      Faith Dogman
    </td>
    <td>
      faith.dogman@hotmail.com
    </td>
  </tr>
  <tr>
    <td>
      4
    </td>
    <td>
      Gregory House
    </td>
    <td>
      greg.house@on.tv
    </td>
  </tr>
</table>
"""
    )


def test_error():
    from docs_code.background import table

    with pytest.raises(TypeError):
        table.test_error()
