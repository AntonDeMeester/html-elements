def test_example():
    from docs_code.index import index

    with open("docs_code/index/index.html", "r") as f:
        assert index.raw == f.read()
