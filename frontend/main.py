from reactpy import component, html, run
from src.App import App


@component
def Main():
    return App()

run(Main, host="fracat-think.local", port=8000)
