# Sistema Inteligente de Monitoreo de Línea de Producción

## Objetivo General
Diseñar e implementar un sistema inteligente para analizar en tiempo real el flujo de piezas en una línea de producción, detectar y registrar automáticamente los tiempos muertos, gestionando la información mediante una plataforma web con usuarios y roles.

## Objetivos Específicos
1. Simular captura del flujo de piezas (simulando cámara)
2. Desarrollar agentes inteligentes que detecten interrupciones en el movimiento de piezas
3. Diseñar algoritmos de búsqueda y clasificación de problemas en el flujo de producción
4. Implementar un sistema basado en conocimiento que identifique las causas de tiempos muertos
5. Entrenar modelos de aprendizaje automático (árboles de decisión y redes neuronales) para la predicción de fallas recurrentes
6. Implementar una plataforma web para la visualización de reportes, con usuarios y roles diferenciados (administrador, supervisor, operador)
7. Integrar base de datos para almacenamiento histórico y generación de métricas

## Requisitos
- Python 3.10+
- Instalar dependencias: `pip install -r requirements.txt`

## Estructura del Proyecto
- `app.py`: Aplicación web principal
- `modules/`: Módulos del sistema
  - Agentes inteligentes de monitoreo
  - Simulador de línea de producción
  - Modelos de aprendizaje automático
  - Sistema de reglas y conocimiento
- `database/`: Gestión de base de datos
- `data/`: Datos históricos y datasets

## Cómo ejecutar
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Relación con la Materia de Inteligencia Artificial
1. **Agentes Inteligentes**: Arquitectura de agentes que monitorean y actúan sobre la producción
2. **Problem Solver Agents**: Uso de algoritmos de búsqueda para detectar interrupciones
3. **Agentes Basados en Conocimiento**: Representación lógica y reglas para clasificar causas de paros
4. **Agentes de Aprendizaje**: Modelos inductivos, árboles de decisión y redes neuronales para predecir fallas
