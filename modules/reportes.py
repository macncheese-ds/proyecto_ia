import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt

def show_reportes():
    """Módulo de reportes y análisis con IA"""
    st.title("📈 Reportes y Análisis Inteligente")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Reportes Generales", 
        "🌳 Árbol de Decisión", 
        "🧠 Red Neuronal",
        "📉 Análisis Predictivo"
    ])
    
    with tab1:
        mostrar_reportes_generales()
    
    with tab2:
        mostrar_arbol_decision()
    
    with tab3:
        mostrar_red_neuronal()
    
    with tab4:
        mostrar_analisis_predictivo()

def mostrar_reportes_generales():
    """Reportes generales del sistema"""
    st.subheader("Resumen de Operaciones")
    
    # Selector de rango de fechas
    col1, col2 = st.columns(2)
    with col1:
        fecha_inicio = st.date_input("Fecha Inicio", datetime.now() - timedelta(days=7))
    with col2:
        fecha_fin = st.date_input("Fecha Fin", datetime.now())
    
    # Generar datos de ejemplo
    datos = generar_datos_reportes()
    
    # Tabla de resumen
    st.subheader("📋 Tiempos Muertos Registrados")
    st.dataframe(datos, use_container_width=True)
    
    # Gráfico de barras
    st.subheader("📊 Tiempos Muertos por Causa")
    fig = px.bar(datos, x='Causa', y='Duración (min)', 
                 title='Distribución de Tiempos Muertos',
                 color='Causa')
    st.plotly_chart(fig, use_container_width=True)
    
    # Botón de descarga
    csv = datos.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar Reporte CSV",
        data=csv,
        file_name=f'reporte_{fecha_inicio}_{fecha_fin}.csv',
        mime='text/csv',
    )

def mostrar_arbol_decision():
    """Sistema de clasificación con árbol de decisión"""
    st.subheader("🌳 Clasificación de Causas con Árbol de Decisión")
    
    st.write("""
    **Objetivo:** Clasificar automáticamente la causa de un tiempo muerto basado en:
    - Duración del paro
    - Hora del día
    - Temperatura de máquina
    - Vibración detectada
    """)
    
    # Entrenar modelo
    X, y, feature_names, class_names = generar_dataset_clasificacion()
    
    clf = DecisionTreeClassifier(max_depth=3, random_state=42)
    clf.fit(X, y)
    
    # Visualizar árbol
    fig, ax = plt.subplots(figsize=(15, 8))
    plot_tree(clf, ax=ax, feature_names=feature_names, 
             class_names=class_names, filled=True, fontsize=10)
    st.pyplot(fig)
    
    # Predicción interactiva
    st.subheader("🔮 Predicción de Causa")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        duracion = st.slider("Duración (min)", 1, 60, 15)
    with col2:
        hora = st.slider("Hora del día", 0, 23, 12)
    with col3:
        temperatura = st.slider("Temperatura (°C)", 20, 80, 45)
    with col4:
        vibracion = st.slider("Vibración", 0, 100, 30)
    
    # Predecir
    entrada = [[duracion, hora, temperatura, vibracion]]
    prediccion = clf.predict(entrada)[0]
    probabilidad = clf.predict_proba(entrada)[0]
    
    st.success(f"**Causa predicha:** {class_names[prediccion]}")
    st.write("**Probabilidades:**")
    for i, clase in enumerate(class_names):
        st.write(f"- {clase}: {probabilidad[i]*100:.2f}%")

def mostrar_red_neuronal():
    """Sistema de predicción con red neuronal"""
    st.subheader("🧠 Predicción de Fallas con Red Neuronal")
    
    st.write("""
    **Objetivo:** Predecir si habrá una falla en las próximas horas basado en:
    - Patrón de producción
    - Histórico de mantenimiento
    - Sensores de máquina
    """)
    
    # Entrenar modelo
    X_train, y_train = generar_dataset_prediccion()
    
    mlp = MLPClassifier(hidden_layer_sizes=(10, 5), max_iter=1000, random_state=42)
    mlp.fit(X_train, y_train)
    
    st.success(f"✅ Modelo entrenado - Precisión: {mlp.score(X_train, y_train)*100:.2f}%")
    
    # Visualizar arquitectura
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.write("**Arquitectura de la Red:**")
        st.write("- Capa de entrada: 4 neuronas")
        st.write("- Capa oculta 1: 10 neuronas")
        st.write("- Capa oculta 2: 5 neuronas")
        st.write("- Capa de salida: 2 neuronas (Falla/Normal)")
    
    with col2:
        # Predicción en tiempo real
        st.write("**Predicción en Tiempo Real:**")
        
        prod_actual = st.slider("Producción actual (%)", 0, 100, 85)
        dias_mantenimiento = st.slider("Días desde mantenimiento", 0, 30, 10)
        temp_motor = st.slider("Temperatura motor (°C)", 30, 90, 55)
        horas_uso = st.slider("Horas de uso continuo", 0, 24, 8)
        
        entrada = [[prod_actual/100, dias_mantenimiento/30, temp_motor/100, horas_uso/24]]
        pred = mlp.predict(entrada)[0]
        prob = mlp.predict_proba(entrada)[0]
        
        if pred == 1:
            st.error(f"⚠️ **RIESGO DE FALLA** ({prob[1]*100:.1f}% probabilidad)")
            st.warning("Recomendación: Mantenimiento preventivo inmediato")
        else:
            st.success(f"✅ **OPERACIÓN NORMAL** ({prob[0]*100:.1f}% probabilidad)")

def mostrar_analisis_predictivo():
    """Análisis predictivo y búsqueda de patrones"""
    st.subheader("📉 Análisis Predictivo y Búsqueda de Patrones")
    
    st.write("""
    **Algoritmos de Búsqueda aplicados:**
    - Búsqueda de patrones en series temporales
    - Identificación de anomalías
    - Correlación entre variables
    """)
    
    # Generar serie temporal
    datos_tiempo = generar_serie_temporal()
    
    # Gráfico de serie temporal con anomalías
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=datos_tiempo['timestamp'],
        y=datos_tiempo['produccion'],
        mode='lines',
        name='Producción',
        line=dict(color='blue')
    ))
    
    # Marcar anomalías
    anomalias = datos_tiempo[datos_tiempo['anomalia'] == 1]
    fig.add_trace(go.Scatter(
        x=anomalias['timestamp'],
        y=anomalias['produccion'],
        mode='markers',
        name='Anomalías Detectadas',
        marker=dict(color='red', size=10, symbol='x')
    ))
    
    fig.update_layout(title='Detección de Anomalías en Producción',
                     xaxis_title='Tiempo',
                     yaxis_title='Piezas/Hora')
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Sistema basado en reglas
    st.subheader("📜 Sistema Basado en Reglas")
    
    reglas = [
        "SI producción < 40 piezas/hora ENTONCES alerta_baja_producción",
        "SI temperatura > 70°C ENTONCES alerta_sobrecalentamiento",
        "SI vibración > 80 Y temperatura > 60 ENTONCES mantenimiento_urgente",
        "SI paros > 5 en 1 hora ENTONCES revisar_material"
    ]
    
    for regla in reglas:
        st.code(regla, language='text')
    
    st.info("💡 Estas reglas son evaluadas constantemente por el sistema de agentes inteligentes")

def generar_datos_reportes():
    """Genera datos de ejemplo para reportes"""
    return pd.DataFrame({
        'Timestamp': pd.date_range(start=datetime.now() - timedelta(hours=24), periods=10, freq='2H'),
        'Causa': np.random.choice(['Falta Material', 'Falla Mecánica', 'Cambio Producto', 'Mantenimiento'], 10),
        'Duración (min)': np.random.randint(5, 45, 10),
        'Turno': np.random.choice(['Mañana', 'Tarde', 'Noche'], 10)
    })

def generar_dataset_clasificacion():
    """Genera dataset para árbol de decisión"""
    np.random.seed(42)
    n_samples = 100
    
    X = np.random.rand(n_samples, 4) * [60, 24, 80, 100]
    
    # Simular clasificación basada en reglas
    y = []
    for muestra in X:
        duracion, hora, temp, vib = muestra
        if vib > 70:
            y.append(0)  # Falla Mecánica
        elif temp > 60:
            y.append(1)  # Sobrecalentamiento
        elif duracion > 30:
            y.append(2)  # Falta Material
        else:
            y.append(3)  # Otros
    
    feature_names = ['Duración', 'Hora', 'Temperatura', 'Vibración']
    class_names = ['Falla Mecánica', 'Sobrecalentamiento', 'Falta Material', 'Otros']
    
    return X, np.array(y), feature_names, class_names

def generar_dataset_prediccion():
    """Genera dataset para red neuronal"""
    np.random.seed(42)
    n_samples = 200
    
    X = np.random.rand(n_samples, 4)
    
    # Generar etiquetas basadas en combinación de features
    y = ((X[:, 0] < 0.7) | (X[:, 1] > 0.6) | (X[:, 2] > 0.7)).astype(int)
    
    return X, y

def generar_serie_temporal():
    """Genera serie temporal con anomalías"""
    n_points = 100
    timestamps = pd.date_range(start=datetime.now() - timedelta(hours=n_points), periods=n_points, freq='H')
    
    # Generar patrón base
    produccion = 50 + 10 * np.sin(np.linspace(0, 4*np.pi, n_points)) + np.random.randn(n_points) * 3
    
    # Insertar anomalías
    anomalias = np.zeros(n_points)
    indices_anomalias = np.random.choice(n_points, 5, replace=False)
    produccion[indices_anomalias] -= 20
    anomalias[indices_anomalias] = 1
    
    return pd.DataFrame({
        'timestamp': timestamps,
        'produccion': produccion,
        'anomalia': anomalias
    })
