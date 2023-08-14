from reactpy import component, html

from src.pages.Home import Home


@component
def App():
    return html.main(Home())
