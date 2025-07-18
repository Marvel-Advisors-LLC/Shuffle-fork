import json
import html

# 1) Verificamos si la ejecución fue exitosa
status_raw = r"""$deep_seek_email_generator_for_m365.success"""
if status_raw.lower() != "true":
    # Timeout o error de conexión
    print("API for deepSeek model  has failed when creating the email. Please write it manually and deny the email sending clicking the red button at the bottom.")
else:
    # 2) Recibe el contenido generado por la IA como raw string
    raw = r"""$deep_seek_email_generator_for_m365.body.choices.#0.message.content"""

    # 3) Limpieza básica del bloque ```html ... ```
    def clean_content(text):
        if not isinstance(text, str):
            return "N/A"

        # Quitar delimitadores ```html al principio y ``` al final, si existen
        text = text.strip()
        if text.startswith("```html"):
            text = text[7:].lstrip()
        if text.endswith("```"):
            text = text[:-3].rstrip()

        # Reemplaza \n literales por saltos de línea reales
        text = text.replace("\\n", "\n")  
        
        return text

 

    # 4) Genera el resultado limpio
    cleaned = clean_content(raw)

    # 5) Resultado que se puede usar en el email final
    print(cleaned)
