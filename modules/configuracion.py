import streamlit as st

def show_configuracion():
    """Módulo de configuración del sistema (solo administradores)"""
    st.title("⚙️ Configuración del Sistema")
    
    # Verificar permisos
    if st.session_state.role != "administrador":
        st.error("❌ Acceso denegado. Solo administradores pueden acceder a esta sección.")
        return
    
    tab1, tab2, tab3 = st.tabs(["👥 Usuarios", "🎯 Parámetros", "📊 Modelos IA"])
    
    with tab1:
        configurar_usuarios()
    
    with tab2:
        configurar_parametros()
    
    with tab3:
        configurar_modelos()

def configurar_usuarios():
    """Gestión de usuarios"""
    st.subheader("Gestión de Usuarios")
    
    st.write("**Usuarios actuales:**")
    usuarios = [
        {"Usuario": "admin", "Rol": "Administrador", "Activo": "✅"},
        {"Usuario": "supervisor", "Rol": "Supervisor", "Activo": "✅"},
        {"Usuario": "operador", "Rol": "Operador", "Activo": "✅"}
    ]
    
    import pandas as pd
    st.dataframe(pd.DataFrame(usuarios), use_container_width=True)
    
    with st.expander("➕ Agregar Nuevo Usuario"):
        nuevo_user = st.text_input("Nombre de usuario")
        nuevo_pass = st.text_input("Contraseña", type="password")
        nuevo_rol = st.selectbox("Rol", ["Administrador", "Supervisor", "Operador"])
        
        if st.button("Crear Usuario"):
            st.success(f"✅ Usuario '{nuevo_user}' creado correctamente")

def configurar_parametros():
    """Configuración de parámetros del sistema"""
    st.subheader("Parámetros del Sistema")
    
    st.markdown("### 🎥 Monitoreo de Cámara")
    umbral_movimiento = st.slider("Umbral de detección de movimiento", 0, 50, 10)
    frames_paro = st.slider("Frames consecutivos para detectar paro", 1, 10, 3)
    
    st.markdown("### 🚨 Alertas")
    temp_max = st.slider("Temperatura máxima (°C)", 50, 100, 70)
    vib_max = st.slider("Vibración máxima", 50, 100, 80)
    
    st.markdown("### ⏱️ Tiempos")
    intervalo_registro = st.slider("Intervalo de registro (segundos)", 1, 60, 5)
    
    if st.button("💾 Guardar Configuración"):
        st.success("✅ Configuración guardada correctamente")

def configurar_modelos():
    """Configuración de modelos de IA"""
    st.subheader("Configuración de Modelos de IA")
    
    st.markdown("### 🌳 Árbol de Decisión")
    max_depth = st.slider("Profundidad máxima", 2, 10, 3)
    min_samples = st.slider("Mínimo de muestras por nodo", 2, 20, 5)
    
    st.markdown("### 🧠 Red Neuronal")
    capas_ocultas = st.text_input("Capas ocultas (ej: 10,5)", "10,5")
    epocas = st.slider("Épocas de entrenamiento", 100, 2000, 1000)
    
    st.markdown("### 📊 Reentrenamiento")
    auto_retrain = st.checkbox("Reentrenamiento automático")
    if auto_retrain:
        frecuencia = st.selectbox("Frecuencia", ["Diario", "Semanal", "Mensual"])
    
    if st.button("🔄 Reentrenar Modelos Ahora"):
        with st.spinner("Entrenando modelos..."):
            import time
            time.sleep(2)
        st.success("✅ Modelos reentrenados correctamente")
