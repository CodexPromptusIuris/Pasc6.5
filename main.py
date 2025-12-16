import streamlit as st
from auth import login
from log_auditor import registrar_evento

st.set_page_config(page_title="Auditoría Digital", layout="centered")

st.title("🛡️ Plataforma de Auditoría Digital")

if login():
    st.success("Acceso autorizado")

    accion = st.selectbox(
        "Selecciona acción",
        ["Revisar auditoría", "Generar auditoría ficticia"]
    )

    if accion == "Generar auditoría ficticia":
        registrar_evento("Auditoría ficticia generada")
        st.json({
            "empresa": "Demo SPA",
            "estado": "Cumple",
            "riesgos": "Bajo",
            "fecha": "2025-01-01"
        })