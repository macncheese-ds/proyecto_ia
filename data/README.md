# Dataset de ejemplo para entrenamiento de modelos

Este directorio contiene datos sintéticos para demostración del sistema.

## Estructura de datos

### eventos.csv
Registro de eventos de la línea de producción:
- timestamp
- tipo (Paro, Falla, Mantenimiento, Normal)
- causa
- duracion_minutos
- turno

### metricas.csv
Métricas de sensores:
- timestamp
- piezas_hora
- temperatura
- vibracion
- eficiencia

## Uso

Los datos se generan automáticamente al ejecutar el sistema.
Para datos reales, reemplazar con archivos CSV del formato especificado.
