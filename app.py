import streamlit as st
import sys
from pathlib import Path

# Agregar el directorio actual al path
sys.path.append(str(Path(__file__).parent))

from modules.auth import check_auth, login_page
from modules.dashboard import show_dashboard
from modules.monitor import show_monitor
from modules.reportes import show_reportes
from modules.configuracion import show_configuracion
from modules.datos_historicos import show_datos_historicos

st.set_page_config(
    page_title="Sistema de Monitoreo de Producción", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar estado de sesión
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'user' not in st.session_state:
    st.session_state.user = None
if 'role' not in st.session_state:
    st.session_state.role = None

# Verificar autenticación
if not st.session_state.authenticated:
    login_page()
else:
    # Sidebar con menu
    st.sidebar.title(f"Usuario: {st.session_state.user}")
    st.sidebar.caption(f"Rol: {st.session_state.role}")
    
    menu_options = [
        "Dashboard",
        "Monitor en Tiempo Real",
        "Reportes",
        "Datos Historicos",
        "Configuracion"
    ]
    
    # Filtrar opciones segun rol
    if st.session_state.role == "operador":
        menu_options = ["Dashboard", "Monitor en Tiempo Real"]
    
    menu = st.sidebar.selectbox("Navegacion", menu_options)
    
    if st.sidebar.button("Cerrar Sesion"):
        st.session_state.authenticated = False
        st.session_state.user = None
        st.session_state.role = None
        st.rerun()
    
    # Mostrar pagina segun seleccion
    if menu == "Dashboard":
        show_dashboard()
    elif menu == "Monitor en Tiempo Real":
        show_monitor()
    elif menu == "Reportes":
        show_reportes()
    elif menu == "Datos Historicos":
        show_datos_historicos()
    elif menu == "Configuracion":
        show_configuracion()

