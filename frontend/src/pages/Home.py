from reactpy import component, html
from src.utils import api 
from src.components import MaterialUI as mui


@component
def ProductItem(product):
    return html.tr(
        html.td(
            html.a({"href": product['url']},f"{product['name']}")
        ),
        html.td(f"{product['description']}"),
        html.td(f"{product['price']}"),
    )

@component
def Products(products):
    products_items = [ProductItem(product) for product in products]
    return html.table(
        html.thead(
            html.tr(
                html.td("Name"),
                html.td("Description"),
                html.td("Price")
            )
        ),
        html.tbody(
            products_items
        )
    )


@component
def Home():
    products = api.get_products()
    
    return html.section(
        html.h2("Product List"),

        Products(products)
    )