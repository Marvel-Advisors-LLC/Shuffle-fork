import json
import html
# 1) Recibe el contenido generado por la IA como raw string
raw = r"""$http_1.body.choices.#0.message.content"""

# 2) Limpieza básica del bloque ```html ... ```
def clean_content(text):
    if not isinstance(text, str):
        return "N/A"
    
    # Quitar delimitadores ```html al principio y ``` al final, si existen
    text = text.strip()
    if text.startswith("```html"):
        text = text[7:].lstrip()  # quita "```html" y espacios
    if text.endswith("```"):
        text = text[:-3].rstrip()  # quita "```" del final

    return text

# 3) Genera el resultado limpio
cleaned = clean_content(raw)

# 4) Resultado que se puede usar en el email final
print(cleaned)