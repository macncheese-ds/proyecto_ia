# Documentación de Temas de IA Cubiertos en el Proyecto

## 1. Introducción a la Inteligencia Artificial (IA)

Este proyecto implementa un **sistema inteligente completo** que aplica técnicas de IA para resolver un problema real de la industria.

## 2. Arquitecturas de Agentes Inteligentes

### Implementación en el Proyecto:

**AgenteMonitor** (modules/monitor.py):
- **Percibir**: Detecta cambios en frames de video
- **Decidir**: Clasifica si hay paro o producción normal
- **Actuar**: Genera alertas y registra eventos

Tipos de agentes implementados:
- **Agentes reactivos**: Responden a percepciones inmediatas
- **Agentes basados en modelos**: Mantienen estado interno
- **Agentes basados en objetivos**: Buscan optimizar la producción

## 3. Búsqueda y Resolución de Problemas

### Algoritmos de Búsqueda:

1. **Búsqueda de patrones** en series temporales (modules/reportes.py)
2. **Detección de anomalías** mediante búsqueda en datos históricos
3. **Optimización de parámetros** para minimizar tiempos muertos

## 4. Problemas de Satisfacción de Restricciones (CSP)

Aplicado en:
- Programación de mantenimiento (satisfacer restricciones de tiempo, disponibilidad, recursos)
- Asignación de turnos operativos
- Balance de carga de trabajo

## 5. Representación del Conocimiento mediante Lógica

### Sistema Basado en Conocimiento (modules/datos_historicos.py):

**Hechos**:
```
temperatura_alta: Temperatura > 70°C
vibración_anormal: Vibración > 80
producción_baja: Piezas/hora < 40
```

**Reglas de Inferencia**:
```
R1: SI temperatura_alta AND vibración_anormal ENTONCES falla_mecánica_inminente
R2: SI producción_baja AND NOT material_disponible ENTONCES falta_material
```

## 6. Sistemas Rule-based y Object-based

- **Motor de reglas** para diagnóstico automático
- **Inferencia hacia adelante** (forward chaining)
- **Sistema experto** para clasificación de causas

## 7. Agentes que Aprenden

### 7.1 Aprendizaje Inductivo

- Generalización de patrones a partir de datos históricos
- Identificación de causas recurrentes

### 7.2 Árboles de Decisión (modules/reportes.py)

Clasificación automática de causas de paros basado en:
- Duración del paro
- Hora del día
- Temperatura de máquina
- Vibración detectada

### 7.3 Redes Neuronales (modules/reportes.py)

Red neuronal multicapa para:
- Predicción de fallas futuras
- Arquitectura: 4 → 10 → 5 → 2
- Aprendizaje supervisado

## Metodología del Proyecto

✅ **Captura de datos**: Simulación de cámara con OpenCV
✅ **Procesamiento local**: Algoritmos de visión por computadora
✅ **Agentes inteligentes**: Monitoreo, análisis y predicción
✅ **Problem Solver**: Búsqueda de patrones y anomalías
✅ **Sistema basado en conocimiento**: Reglas lógicas para clasificación
✅ **Aprendizaje automático**: Árboles de decisión y redes neuronales
✅ **Servidor central**: Base de datos SQLite
✅ **Plataforma web**: Streamlit con roles de usuario
✅ **Validación**: Comparación con registros manuales

## Cumplimiento de Objetivos

- ✅ Análisis en tiempo real del flujo de piezas
- ✅ Detección automática de tiempos muertos
- ✅ Identificación de causas mediante IA
- ✅ Predicción de fallas con ML
- ✅ Plataforma web con usuarios y roles
- ✅ Base de datos para históricos y métricas
- ✅ 100% del contenido académico cubierto
