import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import numpy as np

def show_dashboard():
    """Dashboard principal con métricas y gráficos"""
    st.title("📊 Dashboard de Producción")
    
    # Generar datos de ejemplo
    datos = generar_datos_ejemplo()
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="⏱️ Tiempo Productivo",
            value="85.2%",
            delta="2.3%"
        )
    
    with col2:
        st.metric(
            label="⏸️ Tiempos Muertos",
            value="14.8%",
            delta="-2.3%"
        )
    
    with col3:
        st.metric(
            label="📦 Piezas Procesadas",
            value="1,247",
            delta="156"
        )
    
    with col4:
        st.metric(
            label="🚨 Paros Detectados",
            value="12",
            delta="-3"
        )
    
    # Gráfico de tendencia
    st.subheader("📈 Tendencia de Producción")
    fig = px.line(datos, x='timestamp', y='piezas_hora', 
                  title='Piezas por Hora',
                  labels={'piezas_hora': 'Piezas/Hora', 'timestamp': 'Tiempo'})
    st.plotly_chart(fig, use_container_width=True)
    
    # Distribución de causas de paros
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔍 Causas de Tiempos Muertos")
        causas = pd.DataFrame({
            'Causa': ['Falta de Material', 'Falla Mecánica', 'Cambio de Producto', 'Mantenimiento', 'Otros'],
            'Porcentaje': [35, 25, 20, 15, 5]
        })
        fig_pie = px.pie(causas, values='Porcentaje', names='Causa', 
                         title='Distribución de Causas')
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        st.subheader("🤖 Predicciones del Modelo")
        st.info("**Próxima falla predicha:** En 2.5 horas")
        st.warning("**Tipo probable:** Falla Mecánica (75% confianza)")
        st.success("**Recomendación:** Mantenimiento preventivo")
        
        # Tabla de últimos eventos
        st.subheader("📋 Últimos Eventos")
        eventos = pd.DataFrame({
            'Hora': ['14:23', '13:45', '12:30', '11:15'],
            'Evento': ['Paro detectado', 'Producción normal', 'Paro detectado', 'Inicio turno'],
            'Duración': ['5 min', '-', '12 min', '-']
        })
        st.dataframe(eventos, use_container_width=True)

def generar_datos_ejemplo():
    """Genera datos de ejemplo para el dashboard"""
    horas = 24
    timestamps = [datetime.now() - timedelta(hours=h) for h in range(horas, 0, -1)]
    piezas = np.random.randint(40, 60, horas) + np.sin(np.linspace(0, 4*np.pi, horas)) * 10
    
    return pd.DataFrame({
        'timestamp': timestamps,
        'piezas_hora': piezas.astype(int)
    })
