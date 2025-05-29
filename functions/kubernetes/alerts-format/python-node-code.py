import json

def check_val(val):
    if val in [None, "", "null"]:
        return "N/A"
    if isinstance(val, str):
        # Escape each "\" → "\\"
        return val.replace("\\", "\\\\")
    return val

# 1) Take the entire JSON that Shuffle injects into create_startnode as a RAW STRING
raw = r"""$create_startnode"""

# 2) Convert it to a Python dict (true/false → True/False)
data = json.loads(raw)

# 3) Extract each field using .get() on the dict
file_hash = data.get("all_fields", {}).get("data", {}).get("file_hash")
endpoint  = data.get("all_fields", {}).get("data", {}).get("endpoint")
hostname  = data.get("all_fields", {}).get("predecoder", {}).get("hostname")
timestamp = data.get("all_fields", {}).get("predecoder", {}).get("timestamp")
rule_description = data.get("all_fields", {}).get("rule", {}).get("description")
rule_level = data.get("all_fields", {}).get("rule", {}).get("level")
title     = data.get("title")
file_path = data.get("all_fields", {}).get("data", {}).get("file_path")

# 4) Normalize and escape backslashes
result = {
    "file_hash_normalized_for_iris":    check_val(file_hash),
    "endpoint_normalized_for_iris":     check_val(endpoint),
    "hostname_normalized_for_iris":     check_val(hostname),
    "timestamp_normalized_for_iris":    check_val(timestamp),
    "rule_description_normalized_for_iris": check_val(rule_description),
    "rule_level_normalized_for_iris":   check_val(rule_level),
    "title_normalized_for_iris":        check_val(title),
    "file_path_normalized_for_iris":    check_val(file_path),
    "success": True
}

# 5) Print the resulting JSON so that Shuffle captures it
print(json.dumps(result))