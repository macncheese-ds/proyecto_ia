import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import numpy as np

def show_dashboard():
    """Dashboard principal con métricas y gráficos"""
    st.title("Dashboard de Producción")

    # Usar historial real de paros detectados
    stops_log = st.session_state.get('stops_log', [])
    num_paros = len(stops_log)
    ultimos_eventos = [
        {
            'Hora': stop['timestamp'].strftime('%H:%M'),
            'Evento': 'Paro detectado',
            'Duración': '-'  # Si tienes duración real, cámbialo aquí
        }
        for stop in reversed(stops_log[-10:])
    ]

    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Tiempo Productivo",
            value="85.2%",
            delta="2.3%"
        )

    with col2:
        st.metric(
            label="Tiempos Muertos",
            value="14.8%",
            delta="-2.3%"
        )

    with col3:
        st.metric(
            label="Piezas Procesadas",
            value="1,247",
            delta="156"
        )

    with col4:
        st.metric(
            label="Paros Detectados",
            value=str(num_paros),
            delta=""
        )

    # Gráfico de tendencia (puedes conectar a datos reales si los tienes)
    st.subheader("Tendencia de Producción")
    datos = generar_datos_ejemplo()
    fig = px.line(datos, x='timestamp', y='piezas_hora',
                  title='Piezas por Hora',
                  labels={'piezas_hora': 'Piezas/Hora', 'timestamp': 'Tiempo'})
    st.plotly_chart(fig, use_container_width=True)

    # Distribución de causas de paros (puedes conectar a datos reales si los tienes)
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Causas de Tiempos Muertos")
        causas = pd.DataFrame({
            'Causa': ['Falta de Material', 'Falla Mecánica', 'Cambio de Producto', 'Mantenimiento', 'Otros'],
            'Porcentaje': [35, 25, 20, 15, 5]
        })
        fig_pie = px.pie(causas, values='Porcentaje', names='Causa',
                         title='Distribución de Causas')
        st.plotly_chart(fig_pie, use_container_width=True)

    with col2:
        st.subheader("Predicciones del Modelo")
        st.info("Próxima falla predicha: En 2.5 horas")
        st.warning("Tipo probable: Falla Mecánica (75% confianza)")
        st.success("Recomendación: Mantenimiento preventivo")

        # Tabla de últimos eventos reales
        st.subheader("Últimos Eventos")
        if ultimos_eventos:
            eventos_df = pd.DataFrame(ultimos_eventos)
            st.dataframe(eventos_df, width='stretch')
        else:
            st.info("No hay eventos registrados en esta sesión.")

def generar_datos_ejemplo():
    """Genera datos de ejemplo para el dashboard"""
    horas = 24
    timestamps = [datetime.now() - timedelta(hours=h) for h in range(horas, 0, -1)]
    piezas = np.random.randint(40, 60, horas) + np.sin(np.linspace(0, 4*np.pi, horas)) * 10
    
    return pd.DataFrame({
        'timestamp': timestamps,
        'piezas_hora': piezas.astype(int)
    })
