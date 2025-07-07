import json
import re
import codecs

raw_outer = r"""$receive_raw_information.information"""

# Paso 1: Reemplazar saltos de línea/carriage return crudos que están dentro del JSON
cleaned_raw = raw_outer.replace('\r', '').replace('\n', '\\n')

# Paso 2: Decodificar escapes (por si vienen dobles escapes)
try:
    cleaned_raw = codecs.decode(cleaned_raw, 'unicode_escape')
except Exception:
    pass

# Paso 3: Reemplazar cualquier caracter de control inválido con espacio o nada (opcional)
cleaned_raw = re.sub(r'[\x00-\x1f\x7f]', '', cleaned_raw)

# Paso 4: Intentar parsear JSON limpio
try:
    data = json.loads(cleaned_raw)
except Exception as e:
    data = {}
    error = str(e)
else:
    error = None

html_info = data.get("information", "No information provided.")

# Si no viene emailSender o viene vacío o null, lo dejamos vacío string
email_sender = data.get("emailSender")
if not email_sender:
    email_sender = ""

# Lo mismo para emailReceiver
email_receiver = data.get("emailReceiver")
if not email_receiver:
    email_receiver = ""

result = {
    "html": html_info,
    "emailSender": email_sender,
    "emailReceiver": email_receiver,
    "error": error
}

print(json.dumps(result))
