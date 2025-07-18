import json

# Cargamos el JSON original del nodo inicial
raw = r"""$create_startnode"""
data = json.loads(raw)

# Accedemos a all_fields como en el primer filtro
fields = data.get("all_fields", {})

# Extraemos los campos de interés
sender = fields.get("data", {}).get("office365", {}).get("P2Sender", "").strip().lower()
subject = fields.get("data", {}).get("office365", {}).get("Subject", "").strip().lower()

# Lista blanca de remitentes
allowed_senders = [
    "workflow@jabbroadband.local",
    "no-reply@secure-directory.net-link-secure.com",
    "emily.h@hrsoftwares-finder.online",
    "news@virtualization-online.org",
    "a.rusetskaya@softteco.info"
]

# Palabras clave de campañas legítimas o simulaciones
subject_keywords_to_skip = [
    "gift card",
    "keep training",
    "free meal coupon",
    "exclusive offers",
    "maximize",
    "softteco",
    "reply with",
    "webinar",
    "cloud",
    "postgre",
    "training"
]

# Evaluar si se debe descartar
if sender in allowed_senders:
    print(json.dumps({
        "skip_alert": True
    }))
    exit()

if any(keyword in subject for keyword in subject_keywords_to_skip):
    print(json.dumps({
        "skip_alert": True
    }))
    exit()

# Caso no descartado
print(json.dumps({
    "skip_alert": False
}))
