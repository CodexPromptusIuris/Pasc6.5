import json
from datetime import datetime

def registrar_evento(evento):
    log = {
        "evento": evento,
        "timestamp": datetime.utcnow().isoformat()
    }

    with open("data/audit_demo.json", "a") as f:
        f.write(json.dumps(log) + "\n")