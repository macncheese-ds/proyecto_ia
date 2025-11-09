import streamlit as st
import bcrypt

# Usuarios de ejemplo (en producción esto estaría en BD)
USERS = {
    "admin": {
        "password": bcrypt.hashpw("admin123".encode(), bcrypt.gensalt()),
        "role": "administrador"
    },
    "supervisor": {
        "password": bcrypt.hashpw("super123".encode(), bcrypt.gensalt()),
        "role": "supervisor"
    },
    "operador": {
        "password": bcrypt.hashpw("oper123".encode(), bcrypt.gensalt()),
        "role": "operador"
    }
}

def check_auth(username, password):
    """Verifica las credenciales del usuario"""
    if username in USERS:
        if bcrypt.checkpw(password.encode(), USERS[username]["password"]):
            return True, USERS[username]["role"]
    return False, None

def login_page():
    """Página de login"""
    st.title("🔐 Sistema de Monitoreo de Producción")
    st.subheader("Inicio de Sesión")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        with st.form("login_form"):
            username = st.text_input("Usuario")
            password = st.text_input("Contraseña", type="password")
            submit = st.form_submit_button("Iniciar Sesión")
            
            if submit:
                authenticated, role = check_auth(username, password)
                if authenticated:
                    st.session_state.authenticated = True
                    st.session_state.user = username
                    st.session_state.role = role
                    st.success("✅ Inicio de sesión exitoso")
                    st.rerun()
                else:
                    st.error("❌ Usuario o contraseña incorrectos")
        
        st.info("""
        **Usuarios de prueba:**
        - admin / admin123 (Administrador)
        - supervisor / super123 (Supervisor)
        - operador / oper123 (Operador)
        """)
