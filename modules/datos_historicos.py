import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

def show_datos_historicos():
    """Módulo de datos históricos y base de conocimiento"""
    st.title("📚 Datos Históricos y Base de Conocimiento")
    
    tab1, tab2 = st.tabs(["📊 Histórico de Eventos", "🧠 Base de Conocimiento"])
    
    with tab1:
        mostrar_historico()
    
    with tab2:
        mostrar_base_conocimiento()

def mostrar_historico():
    """Muestra histórico de eventos"""
    st.subheader("Registro Histórico de Eventos")
    
    # Filtros
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fecha_inicio = st.date_input("Desde", datetime.now() - timedelta(days=30))
    with col2:
        fecha_fin = st.date_input("Hasta", datetime.now())
    with col3:
        tipo_evento = st.selectbox("Tipo de Evento", 
                                   ["Todos", "Paro", "Falla", "Mantenimiento", "Normal"])
    
    # Generar datos históricos
    datos = generar_historico()
    
    # Aplicar filtros
    if tipo_evento != "Todos":
        datos = datos[datos['Tipo'] == tipo_evento]
    
    st.write(f"**Total de registros:** {len(datos)}")
    st.dataframe(datos, use_container_width=True)
    
    # Estadísticas
    st.subheader("📊 Estadísticas")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Paros", len(datos[datos['Tipo'] == 'Paro']))
    with col2:
        st.metric("Tiempo Total Paros (h)", 
                 f"{datos[datos['Tipo'] == 'Paro']['Duración (min)'].sum() / 60:.1f}")
    with col3:
        st.metric("MTBF (h)", "12.5")  # Mean Time Between Failures

def mostrar_base_conocimiento():
    """Muestra la base de conocimiento del sistema"""
    st.subheader("🧠 Base de Conocimiento - Sistema Experto")
    
    st.write("""
    El sistema utiliza una **representación lógica del conocimiento** para clasificar 
    y diagnosticar problemas en la línea de producción.
    """)
    
    # Hechos
    st.markdown("### 📋 Hechos del Sistema")
    hechos = {
        "temperatura_alta": "Temperatura > 70°C",
        "vibración_anormal": "Vibración > 80",
        "producción_baja": "Piezas/hora < 40",
        "material_disponible": "Nivel material > 20%",
        "mantenimiento_reciente": "Días desde mantto < 7"
    }
    
    for hecho, descripcion in hechos.items():
        st.code(f"{hecho}: {descripcion}", language='text')
    
    # Reglas de inferencia
    st.markdown("### 🔍 Reglas de Inferencia")
    
    reglas = [
        {
            "id": "R1",
            "condicion": "temperatura_alta AND vibración_anormal",
            "conclusion": "falla_mecánica_inminente",
            "accion": "Detener máquina y realizar mantenimiento"
        },
        {
            "id": "R2",
            "condicion": "producción_baja AND NOT material_disponible",
            "conclusion": "falta_material",
            "accion": "Notificar al supervisor para reponer material"
        },
        {
            "id": "R3",
            "condicion": "producción_baja AND material_disponible",
            "conclusion": "problema_mecánico",
            "accion": "Revisar componentes mecánicos"
        },
        {
            "id": "R4",
            "condicion": "NOT mantenimiento_reciente AND temperatura_alta",
            "conclusion": "mantenimiento_preventivo_requerido",
            "accion": "Programar mantenimiento"
        }
    ]
    
    for regla in reglas:
        with st.expander(f"**{regla['id']}**: {regla['conclusion']}"):
            st.write(f"**SI:** {regla['condicion']}")
            st.write(f"**ENTONCES:** {regla['conclusion']}")
            st.info(f"**Acción:** {regla['accion']}")
    
    # Motor de inferencia simulado
    st.markdown("### ⚙️ Motor de Inferencia en Acción")
    
    st.write("**Estado actual del sistema:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        temp_alta = st.checkbox("Temperatura alta detectada")
        vib_anormal = st.checkbox("Vibración anormal detectada")
        prod_baja = st.checkbox("Producción baja")
    
    with col2:
        material_ok = st.checkbox("Material disponible")
        mant_reciente = st.checkbox("Mantenimiento reciente")
    
    if st.button("🔍 Ejecutar Inferencia"):
        conclusiones = []
        
        # Evaluar reglas
        if temp_alta and vib_anormal:
            conclusiones.append(("🚨 CRÍTICO", reglas[0]))
        
        if prod_baja and not material_ok:
            conclusiones.append(("⚠️ ALERTA", reglas[1]))
        
        if prod_baja and material_ok:
            conclusiones.append(("⚠️ ALERTA", reglas[2]))
        
        if not mant_reciente and temp_alta:
            conclusiones.append(("ℹ️ INFO", reglas[3]))
        
        if conclusiones:
            st.write("**Conclusiones del sistema:**")
            for nivel, regla in conclusiones:
                if "CRÍTICO" in nivel:
                    st.error(f"{nivel}: {regla['conclusion']}")
                elif "ALERTA" in nivel:
                    st.warning(f"{nivel}: {regla['conclusion']}")
                else:
                    st.info(f"{nivel}: {regla['conclusion']}")
                st.write(f"→ {regla['accion']}")
        else:
            st.success("✅ Sistema operando normalmente")
    
    # Patrones aprendidos
    st.markdown("### 📚 Patrones Aprendidos (Aprendizaje Inductivo)")
    
    patrones = pd.DataFrame({
        'Patrón': [
            'Paro largo seguido de temperatura alta',
            'Múltiples paros cortos consecutivos',
            'Baja producción en turno noche',
            'Vibración aumenta gradualmente'
        ],
        'Frecuencia': [15, 23, 8, 12],
        'Causa Asociada': [
            'Sobrecalentamiento',
            'Falta de material',
            'Fatiga operador',
            'Desgaste rodamiento'
        ],
        'Confianza': ['85%', '92%', '78%', '88%']
    })
    
    st.dataframe(patrones, use_container_width=True)

def generar_historico():
    """Genera datos históricos de ejemplo"""
    np.random.seed(42)
    n_eventos = 50
    
    timestamps = [datetime.now() - timedelta(hours=i*2) for i in range(n_eventos)]
    tipos = np.random.choice(['Paro', 'Falla', 'Mantenimiento', 'Normal'], n_eventos, p=[0.3, 0.2, 0.1, 0.4])
    duraciones = np.random.randint(1, 60, n_eventos)
    causas = []
    
    for tipo in tipos:
        if tipo == 'Paro':
            causas.append(np.random.choice(['Falta Material', 'Cambio Producto', 'Ajuste']))
        elif tipo == 'Falla':
            causas.append(np.random.choice(['Mecánica', 'Eléctrica', 'Neumática']))
        elif tipo == 'Mantenimiento':
            causas.append('Preventivo')
        else:
            causas.append('-')
    
    return pd.DataFrame({
        'Timestamp': timestamps,
        'Tipo': tipos,
        'Causa': causas,
        'Duración (min)': duraciones,
        'Turno': np.random.choice(['Mañana', 'Tarde', 'Noche'], n_eventos)
    }).sort_values('Timestamp', ascending=False)
