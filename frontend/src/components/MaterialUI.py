from reactpy import web, component

mui = web.module_from_template(
    "react@^18.0.0",
    "@material-ui/core@5.14.4",
    fallback="⌛",
)


Table = web.export(mui, "Table")
TableBody = web.export(mui, "TableBody")
TableCell = web.export(mui, "TableCell")
TableContainer = web.export(mui, "TableContainer")
TableHead = web.export(mui, "TableHead") 
TableRow = web.export(mui, "TableRow")
Paper = web.export(mui, "Paper")

Button = web.export(mui, "Button")


@component
def PrimaryBtn(content, handle_click):
    return Button({
        "color": "primary",
        "variant": "contained",
        "on_click": handle_click,
    }, content)

