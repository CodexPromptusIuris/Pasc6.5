#!/bin/bash

PROJECT_NAME="auditoria-app"

mkdir -p $PROJECT_NAME/{app,data,tests}

touch $PROJECT_NAME/app/{__init__.py,main.py,auth.py,validations.py,mapping.py,log_auditor.py}
touch $PROJECT_NAME/data/audit_demo.json
touch $PROJECT_NAME/tests/test_validations.py
touch $PROJECT_NAME/{README.md,requirements.txt,LICENSE,run.sh,.gitignore}

echo "Repositorio $PROJECT_NAME creado correctamente ✅"