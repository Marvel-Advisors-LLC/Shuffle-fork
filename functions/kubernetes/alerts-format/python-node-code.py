import json

def check_val(val):
    if val in [None, "", "null"]:
        return "N/A"
    if isinstance(val, str):
        return val.replace("\\", "\\\\")
    return val

def sanitize_for_deepseek(val):
    if val in [None, "", "null"]:
        return "N/A"
    if isinstance(val, str):
        # Reemplaza backslashes por forward slashes
        return val.replace("\\", "/")
    return val

# 1) Coge el JSON inyectado por Shuffle como raw string
raw = r"""$create_startnode"""

# 2) Lo parseamos a un dict de Python
data = json.loads(raw)

# 3) Extraemos los campos necesarios
file_hash        = data.get("all_fields", {}).get("data", {}).get("file_hash")
endpoint         = data.get("all_fields", {}).get("data", {}).get("endpoint")
hostname         = data.get("all_fields", {}).get("predecoder", {}).get("hostname")
timestamp        = data.get("all_fields", {}).get("predecoder", {}).get("timestamp")
rule_description = data.get("all_fields", {}).get("rule", {}).get("description")
rule_level       = data.get("all_fields", {}).get("rule", {}).get("level")
title            = data.get("title")
file_path        = data.get("all_fields", {}).get("data", {}).get("file_path")
full_log         = data.get("all_fields", {}).get("full_log")
log_message1     = data.get("all_fields", {}).get("data", {}).get("log_message1")
log_message2     = data.get("all_fields", {}).get("data", {}).get("log_message2")

# 4) Creamos el output normalizado
result = {
    # Para IRIS
    "file_hash_normalized_for_iris":     check_val(file_hash),
    "endpoint_normalized_for_iris":      check_val(endpoint),
    "hostname_normalized_for_iris":      check_val(hostname),
    "timestamp_normalized_for_iris":     check_val(timestamp),
    "rule_description_normalized_for_iris": check_val(rule_description),
    "rule_level_normalized_for_iris":    check_val(rule_level),
    "title_normalized_for_iris":         check_val(title),
    "file_path_normalized_for_iris":     check_val(file_path),
    "log_message1_normalized_for_iris":  check_val(log_message1),
    "log_message2_normalized_for_iris":  check_val(log_message2),

    # Para DeepSeek (sin backslashes conflictivos)
    "file_path_for_deepseek":            sanitize_for_deepseek(file_path),
    "full_log_for_deepseek":             sanitize_for_deepseek(full_log),
    "rule_description_for_deepseek":    sanitize_for_deepseek(rule_description),
    "title_for_deepseek":                sanitize_for_deepseek(title),


    "success": True
}

# 5) Imprimimos el output para que lo capture Shuffle
print(json.dumps(result))
