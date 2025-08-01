import json

# 1. Tomamos el JSON crudo desde el nodo anterior
raw = r"""$create_startnode"""
data = json.loads(raw)

# 2. Accedemos a all_fields
fields = data.get("all_fields", {})

rule_id = int(fields.get("rule", {}).get("id", 0))
rule_level = int(fields.get("rule", {}).get("level", 0))
rule_description = fields.get("rule", {}).get("description", "").strip()

# Nuevo filtro: Descartar si rule.description contiene el texto específico
if rule_description == "Office 365: Quarantine events.":
    print("invalid_alert")
    exit()

# 3. Verificamos si es una alerta M365 sin riesgo
if rule_id == 91556:
    delivery_action = fields.get("data", {}).get("office365", {}).get("DeliveryAction", "").lower()
    delivery_location = fields.get("data", {}).get("office365", {}).get("LatestDeliveryLocation", "").lower()

    acciones_ruido = ["blocked", "deliveredasspam"]
    ubicaciones_ruido = ["quarantine", "junkfolder"]

    if delivery_action in acciones_ruido or delivery_location in ubicaciones_ruido:
        print("invalid_alert")
        exit()

# 4. Si no fue descartado, seguir el flujo
print(json.dumps({"valid_alert": True}))
