import json

# Cargamos el JSON original del nodo inicial
raw = r"""$create_startnode"""
data = json.loads(raw)

# Accedemos a all_fields como en el primer filtro
fields = data.get("all_fields", {})

# Extraemos los campos de interés
sender = fields.get("data", {}).get("office365", {}).get("P2Sender", "").strip().lower()
subject = fields.get("data", {}).get("office365", {}).get("Subject", "").strip().lower()
# Primero intenta con RecipientEmailAddress
recipient = fields.get("data", {}).get("office365", {}).get("RecipientEmailAddress", "")
# Si está vacío, intenta con el primer elemento de la lista Recipients
if not recipient:
    recipients_list = fields.get("data", {}).get("office365", {}).get("Recipients", [])
    recipient = recipients_list[0].strip().lower() if recipients_list else ""
else:
    recipient = recipient.strip().lower()

# Lista blanca de remitentes
allowed_senders = [
    "workflow@jabbroadband.local",
    "no-reply@secure-directory.net-link-secure.com",
    "emily.h@hrsoftwares-finder.online",
    "news@virtualization-online.org",
    "a.rusetskaya@softteco.info",
    "workout@onlineportalsignin.drive-signin.org",
    "no-reply@onlineportalsignin.drive-signin.org",
    "no-reply@secure-directory.net-link-secure.com",
    "j.burns@blue-skycapitalstrategiesllc.co",
    "no-reply@online-ops.mypasschange.com",
    "info@culliganquench.com"
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

# Dominio confiable
trusted_domain = "dal1-imap.risebroadband.com"

# Destinatarios explícitamente confiables
trusted_recipients_known = ["support"]
trusted_recipients_potential = ["info", "billing", "copyright", "enterprisesupport"]

# Evaluar si se debe descartar
if sender in allowed_senders:
    print(json.dumps({
        "skip_alert": True,
        "debug_recipient": recipient
    }))
    exit()

if any(keyword in subject for keyword in subject_keywords_to_skip):
    print(json.dumps({
        "skip_alert": True,
        "debug_recipient": recipient
    }))
    exit()


# Validar destinatario
if recipient.endswith(f"@{trusted_domain}"):
    local_part = recipient.split("@")[0]
    if any(local_part.startswith(p) for p in trusted_recipients_known + trusted_recipients_potential):
        print(json.dumps({
            "skip_alert": True,
            "debug_recipient": recipient
        }))
        exit()

print(json.dumps({
    "skip_alert": False,
    "debug_recipient": recipient
}))
