import base64


def svg_to_html(svg_string: str) -> str:
    b64 = base64.b64encode(svg_string.encode("utf-8")).decode("utf-8")
    css_justify = "center"
    css = '<p style="text-align:center; display: flex; flex-direction: column; justify-content: {};">'.format(
        css_justify
    )
    html = r'{}<img src="data:image/svg+xml;base64,{}"/>'.format(css, b64)
    return html


def invert_hex_color(content):
    text = content.lower()
    code = {}
    l1 = "#;0123456789abcdef"
    l2 = "#;fedcba9876543210"
    for i in range(len(l1)):
        code[l1[i]] = l2[i]
    inverted = ""
    for j in text:
        inverted += code[j]
    return inverted
