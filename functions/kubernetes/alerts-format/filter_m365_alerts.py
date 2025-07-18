import json

# 1. Obtener el JSON del nodo anterior (Webhook)
raw = r"""$create_startnode"""
data = json.loads(raw)

# 2. Leer campos clave
rule_id = int(data.get("rule.id", 0))
rule_level = int(data.get("rule.level", 0))


# 3. Filtrar por regla M365
if rule_id == 91556:
    delivery_action = data.get("data.office365.DeliveryAction", "").lower()
    delivery_location = data.get("data.office365.LatestDeliveryLocation", "").lower()

    # Lista de valores que queremos descartar (en minúsculas para evitar errores de mayúsculas)
    acciones_ruido = ["blocked", "deliveredasspam"]
    ubicaciones_ruido = ["quarantine", "junkfolder"]

    if delivery_action in acciones_ruido or delivery_location in ubicaciones_ruido:
        print("Descartado: M365 con DeliveryAction o LatestDeliveryLocation que no implica riesgo.")
        exit()

# 4. Si pasó los filtros, continuar
print(json.dumps({"alerta_valida": True}))
