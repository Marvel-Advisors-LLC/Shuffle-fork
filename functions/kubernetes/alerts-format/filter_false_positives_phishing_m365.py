import json
import re
import unicodedata

# Cargamos el JSON original del nodo inicial
raw = r"""$create_startnode"""
data = json.loads(raw)

def clean_text(s):
    """Quita espacios extremos, normaliza unicode y elimina caracteres de control invisibles."""
    if s is None:
        return ""
    # Normalizar (NFKC) y convertir a str
    t = str(s)
    t = unicodedata.normalize("NFKC", t)
    # eliminar caracteres de control excepto \n\r\t si hubiera (opcionales)
    t = re.sub(r'[\x00-\x1f\x7f]', '', t)
    return t.strip()

# Accedemos a all_fields
fields = data.get("all_fields", {})

# Campos principales de Office365
office365_data = fields.get("data", {}).get("office365", {})

# Campos importantes
sender = clean_text(fields.get("data", {}).get("office365", {}).get("P2Sender", "")).lower()
subject = clean_text(fields.get("data", {}).get("office365", {}).get("Subject", "")).lower()

# Intentamos distintas keys posibles para destinatarios
recipient_field = (
    fields.get("data", {}).get("office365", {}).get("RecipientEmailAddress")
    or fields.get("data", {}).get("office365", {}).get("Recipients")
    or fields.get("data", {}).get("office365", {}).get("Recipient_List")
    or ""
)

# Si es lista, unimos con coma para procesar; si no, convertimos a string
if isinstance(recipient_field, list):
    recipient_raw = ", ".join(str(x) for x in recipient_field)
else:
    recipient_raw = str(recipient_field)

recipient_raw = clean_text(recipient_raw).lower()

# Extraer todas las direcciones de email con regex robusta
emails = re.findall(r'([A-Za-z0-9!#$%&\'*+\-/=?^_`{|}~\.]+@[A-Za-z0-9\.\-]+\.[A-Za-z]{2,})', recipient_raw)

# Si no extrajimos nada, intentamos limpiar caracteres comunes y volver a intentar
if not emails and recipient_raw:
    fallback = re.sub(r'[<>"\[\]\(\)]', '', recipient_raw)
    emails = re.findall(r'([A-Za-z0-9!#$%&\'*+\-/=?^_`{|}~\.]+@[A-Za-z0-9\.\-]+\.[A-Za-z]{2,})', fallback)


# === extraer AuthDetails si existen ===
auth_details_raw = office365_data.get("AuthDetails", [])
auth_details = {}
if isinstance(auth_details_raw, list):
    for item in auth_details_raw:
        name = item.get("Name")
        value = item.get("Value")
        if name:
            auth_details[clean_text(name)] = clean_text(value)



# Reglas / listas
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

subject_keywords_to_skip = [
    "gift card","keep training","free meal coupon","exclusive offers",
    "maximize","softteco","reply with","webinar","cloud","postgre","training"
]

trusted_domain = "dal1-imap.risebroadband.com"
trusted_recipients_known = ["support"]
trusted_recipients_potential = ["info","billing","copyright","enterprisesupport"]

# Debug inicial para ver qué está llegando (usa repr para ver caracteres invisibles)
debug = {
    "recipient_field_raw_repr": repr(recipient_field),
    "recipient_raw_repr": repr(recipient_raw),
    "emails_extracted": emails,
    "sender": sender,
    "subject": subject,
    "auth_details": auth_details,
    "UserKey": clean_text(office365_data.get("UserKey", "")),
    "ObjectId": clean_text(office365_data.get("ObjectId", "")),
    "Operation": clean_text(office365_data.get("Operation", "")),
    "Workload": clean_text(office365_data.get("Workload", "")),
    "ResultStatus": clean_text(office365_data.get("ResultStatus", "")),
    "RecordType": clean_text(office365_data.get("RecordType", "")),
    "CreationTime": clean_text(office365_data.get("CreationTime", "")),
    "Id": clean_text(office365_data.get("Id", ""))
}

# 1) Sender en whitelist
if sender and sender in allowed_senders:
    debug["reason"] = "allowed_sender"
    print(json.dumps({"skip_alert": True, "debug": debug}))
    exit()

# 2) Subject contiene keywords a saltar
if subject and any(k in subject for k in subject_keywords_to_skip):
    debug["reason"] = "subject_keyword"
    print(json.dumps({"skip_alert": True, "debug": debug}))
    exit()

# 3) Evaluar cada email extraído
trusted_domain_clean = clean_text(trusted_domain).lower()
for e in emails:
    e_clean = clean_text(e).lower()
    if "@" not in e_clean:
        continue
    local_part, domain = e_clean.split("@", 1)
    domain_clean = domain.strip().lower().rstrip(".")

    debug["testing_email"] = e_clean
    debug["domain_clean"] = domain_clean
    debug["trusted_domain_clean"] = trusted_domain_clean

    if trusted_domain_clean in domain_clean:
        debug.update({
            "matched_email": e_clean,
            "local_part": local_part,
            "domain": domain_clean,
            "reason": "domain_match_any_localpart"
        })
        print(json.dumps({"skip_alert": True, "debug": debug}))
        exit()


# No se descartó
debug["reason"] = "not_matched"
print(json.dumps({"skip_alert": False, "debug": debug}))
