# Base de datos SQLite para el sistema
import sqlite3
from datetime import datetime
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'produccion.db')

def init_database():
    """Inicializa la base de datos con las tablas necesarias"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Tabla de eventos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS eventos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            tipo TEXT NOT NULL,
            causa TEXT,
            duracion_minutos INTEGER,
            turno TEXT,
            descripcion TEXT
        )
    ''')
    
    # Tabla de métricas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metricas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            piezas_hora INTEGER,
            temperatura REAL,
            vibracion REAL,
            eficiencia REAL
        )
    ''')
    
    # Tabla de predicciones
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predicciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            tipo_prediccion TEXT,
            probabilidad REAL,
            accion_recomendada TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def insertar_evento(tipo, causa, duracion, turno, descripcion=''):
    """Inserta un nuevo evento en la base de datos"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO eventos (tipo, causa, duracion_minutos, turno, descripcion)
        VALUES (?, ?, ?, ?, ?)
    ''', (tipo, causa, duracion, turno, descripcion))
    
    conn.commit()
    conn.close()

def obtener_eventos(limite=100):
    """Obtiene los últimos eventos de la base de datos"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM eventos 
        ORDER BY timestamp DESC 
        LIMIT ?
    ''', (limite,))
    
    eventos = cursor.fetchall()
    conn.close()
    
    return eventos

# Inicializar la base de datos al importar el módulo
if not os.path.exists(DB_PATH):
    init_database()
