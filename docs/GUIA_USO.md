# Guía de Uso del Sistema

## Instalación

1. **Instalar Python 3.10 o superior**

2. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

3. **Ejecutar la aplicación**:
```bash
streamlit run app.py
```

4. **Abrir en el navegador**: 
   - La aplicación se abrirá automáticamente en `http://localhost:8501`

## Usuarios de Prueba

| Usuario | Contraseña | Rol | Permisos |
|---------|-----------|-----|----------|
| admin | admin123 | Administrador | Acceso total |
| supervisor | super123 | Supervisor | Dashboard, Monitor, Reportes, Datos |
| operador | oper123 | Operador | Dashboard, Monitor |

## Funcionalidades por Módulo

### 📊 Dashboard
- Métricas en tiempo real
- Gráficos de tendencias
- Resumen de eventos

### 🎥 Monitor en Tiempo Real
- Simulación de línea de producción
- Agente inteligente de detección
- Alertas automáticas

### 📈 Reportes
- **Reportes Generales**: Análisis de tiempos muertos
- **Árbol de Decisión**: Clasificación de causas
- **Red Neuronal**: Predicción de fallas
- **Análisis Predictivo**: Detección de anomalías

### 📚 Datos Históricos
- Consulta de eventos pasados
- Base de conocimiento del sistema
- Patrones aprendidos

### ⚙️ Configuración (Solo Administrador)
- Gestión de usuarios
- Parámetros del sistema
- Reentrenamiento de modelos

## Demostraciones de IA

### 1. Agentes Inteligentes
- Ve a "Monitor en Tiempo Real"
- Click en "Iniciar Simulación"
- Observa cómo el agente detecta paros automáticamente

### 2. Árbol de Decisión
- Ve a "Reportes" → "Árbol de Decisión"
- Ajusta los sliders para ver predicciones
- Observa la visualización del árbol

### 3. Red Neuronal
- Ve a "Reportes" → "Red Neuronal"
- Modifica los parámetros de entrada
- Ve la predicción de fallas en tiempo real

### 4. Sistema Basado en Reglas
- Ve a "Datos Históricos" → "Base de Conocimiento"
- Selecciona condiciones del sistema
- Click en "Ejecutar Inferencia"
- Observa las conclusiones del sistema experto

## Troubleshooting

**Error: Module not found**
```bash
pip install -r requirements.txt
```

**Error: Port already in use**
```bash
streamlit run app.py --server.port 8502
```

**Problemas con OpenCV en Windows**
```bash
pip install opencv-python-headless
```
