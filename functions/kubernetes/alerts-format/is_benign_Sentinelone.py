import json

# 1) Input crudo del nodo inicial
raw = r"""$create_startnode"""

# 2) Parseamos a un dict de Python
data = json.loads(raw)

# 3) Extraemos el mensaje
log_msg = data.get("all_fields", {}).get("data", {}).get("log_message1", "").strip()

# 4) Frases de alertas ya mitigadas (sin pasar a lower())
benign_phrases = [
    "Kill performed successfully",
    "Quarantine performed successfully",
    "Threat Killed By Policy",
    "User Issued Kill Command",
    "Network quarantine performed successfully"
]

# 5) Evaluación (match exacto)
if log_msg in benign_phrases:
    print(json.dumps({"continue_flow": False}))
else:
    print(json.dumps({"continue_flow": True}))
