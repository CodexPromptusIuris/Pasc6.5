import streamlit as st

USUARIO = "admin"
PASSWORD = "admin123"

def login():
    with st.sidebar:
        user = st.text_input("Usuario")
        pwd = st.text_input("Contraseña", type="password")
        if st.button("Ingresar"):
            if user == USUARIO and pwd == PASSWORD:
                return True
            else:
                st.error("Credenciales incorrectas")
    return False