from typing import Annotated

from fastapi import Depends, Header, Request


def is_htmx(request: Request) -> bool:
    return bool(request.headers.get("HX-Request", False))


def _is_htmx_dependency(hx_request: Annotated[str, Header()] = "") -> bool:
    return hx_request == "true"


is_htmx_dependency = Annotated[bool, Depends(_is_htmx_dependency)]
