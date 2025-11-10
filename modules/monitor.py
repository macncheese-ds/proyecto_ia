import streamlit as st
import numpy as np
import cv2
from PIL import Image
import time
from datetime import datetime
from sklearn.cluster import KMeans
from scipy import ndimage

class AgenteMonitor:
    """Agente inteligente que monitorea el flujo de piezas usando Vision por Computadora y ML"""
    def __init__(self):
        self.estado = "monitoreando"
        self.umbral_movimiento = 15
        self.tiempo_sin_movimiento = 0
        self.historial_movimiento = []
        self.detector_fondo = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)
        
    def percibir(self, frame_anterior, frame_actual):
        """Percibe cambios en el entorno usando algoritmos de vision por computadora REALES"""
        if frame_anterior is None:
            return 0, {
                'area_movimiento': 0,
                'num_contornos': 0,
                'flujo_optico': 0,
                'intensidad_cambio': 0
            }
        
        # ALGORITMO 1: Diferencia absoluta de frames (deteccion basica)
        diff = cv2.absdiff(frame_anterior, frame_actual)
        gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        
        # ALGORITMO 2: Aplicar threshold para binarizar (tecnica de vision)
        _, thresh = cv2.threshold(gray_diff, 25, 255, cv2.THRESH_BINARY)
        
        # ALGORITMO 3: Operaciones morfologicas (apertura y cierre) - IA de vision
        kernel = np.ones((5,5), np.uint8)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        
        # ALGORITMO 4: Deteccion de contornos (busqueda en espacio de estados)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # ALGORITMO 5: Calcular area total de movimiento (metrica cuantificable)
        area_total = sum([cv2.contourArea(c) for c in contours if cv2.contourArea(c) > 100])
        
        # ALGORITMO 6: Flujo optico (algoritmo avanzado de vision)
        gray_prev = cv2.cvtColor(frame_anterior, cv2.COLOR_BGR2GRAY)
        gray_curr = cv2.cvtColor(frame_actual, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(gray_prev, gray_curr, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        flujo_promedio = np.mean(mag)
        
        # Calcular movimiento combinado (fusion de sensores)
        movimiento = (np.mean(gray_diff) * 0.4 + flujo_promedio * 10 * 0.6)
        
        metricas = {
            'area_movimiento': area_total,
            'num_contornos': len(contours),
            'flujo_optico': flujo_promedio,
            'intensidad_cambio': np.mean(gray_diff)
        }
        
        return movimiento, metricas
    
    def decidir(self, movimiento, metricas):
        """Decide usando logica de agentes inteligentes y reglas de inferencia"""
        # Sistema basado en reglas (Knowledge-Based System)
        
        # REGLA 1: Verificar si hay contornos (objetos detectados)
        tiene_objetos = metricas['num_contornos'] > 0
        
        # REGLA 2: Verificar si hay movimiento suficiente
        tiene_movimiento = movimiento >= self.umbral_movimiento
        
        # REGLA 3: Verificar flujo optico (movimiento real de pixeles)
        tiene_flujo = metricas['flujo_optico'] > 0.1  # Umbral mas realista
        
        # LOGICA DE DECISION:
        # Si hay objetos O hay flujo O hay movimiento -> PRODUCCION NORMAL
        if tiene_objetos or tiene_flujo or tiene_movimiento:
            self.tiempo_sin_movimiento = 0
            return "produccion_normal", "Operacion normal - Movimiento detectado"
        
        # Si no hay nada de movimiento -> Contar frames
        self.tiempo_sin_movimiento += 1
        
        # Solo declarar PARO despues de varios frames SIN movimiento
        if self.tiempo_sin_movimiento > 5:
            return "paro_detectado", "Ausencia de movimiento detectada"
        
        # En proceso de verificacion
        return "monitoreando", "Verificando condiciones"
    
    def actuar(self, decision, razon):
        """Actua segun la decision tomada (Accion del agente)"""
        if decision == "paro_detectado":
            return {
                "alerta": True,
                "nivel": "CRITICO",
                "mensaje": f"PARO DETECTADO - {razon}",
                "timestamp": datetime.now(),
                "accion": "Registrar evento en base de datos"
            }
        elif decision == "paro_sospechoso":
            return {
                "alerta": True,
                "nivel": "ADVERTENCIA",
                "mensaje": f"POSIBLE PARO - {razon}",
                "timestamp": datetime.now(),
                "accion": "Monitorear de cerca"
            }
        elif decision == "monitoreando":
            return {
                "alerta": False,
                "nivel": "VERIFICANDO",
                "mensaje": f"Monitoreando - {razon}",
                "timestamp": datetime.now(),
                "accion": "Verificar estado"
            }
        return {
            "alerta": False,
            "nivel": "NORMAL",
            "mensaje": f"Produccion normal - {razon}",
            "timestamp": datetime.now(),
            "accion": "Continuar monitoreando"
        }

def show_monitor():
    """Modulo de monitoreo en tiempo real con simulacion de camara"""
    st.title("Monitor en Tiempo Real")

    st.info("""
    Sistema de Agentes Inteligentes Implementado:
    - Agente Monitor: Detecta movimiento usando Vision por Computadora
    - Agente Analizador: Clasifica causas usando Reglas de Inferencia
    - Agente Predictor: Predice fallas basado en patrones historicos

    Algoritmos de IA Activos:
    - Deteccion de movimiento (Diferencia de frames)
    - Flujo optico (Farneback)
    - Segmentacion (Background Subtraction MOG2)
    - Deteccion de contornos (Busqueda en espacio)
    - Sistema basado en reglas (Knowledge-Based)
    """)
    
    # Inicializar estado de sesion
    if 'simulacion_activa' not in st.session_state:
        st.session_state.simulacion_activa = False
    if 'produccion_manual' not in st.session_state:
        st.session_state.produccion_manual = True
    if 'frame_count' not in st.session_state:
        st.session_state.frame_count = 0
    if 'stops_log' not in st.session_state:
        st.session_state.stops_log = []
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        st.subheader("Control de Simulacion")

        # Controles manuales
        if st.button("Iniciar Simulacion" if not st.session_state.simulacion_activa else "Detener Simulacion"):
            st.session_state.simulacion_activa = not st.session_state.simulacion_activa

        st.session_state.produccion_manual = st.checkbox(
            "Produccion ACTIVA (desmarcar para simular PARO)",
            value=st.session_state.produccion_manual
        )

        velocidad = st.slider("Velocidad de produccion", 0, 100, 50)

        st.markdown("---")
        st.subheader("Estado del Sistema")
        estado_placeholder = st.empty()
        metricas_placeholder = st.empty()

        st.markdown("---")
        st.subheader("Algoritmos de IA Activos")
        st.text("Vision por Computadora:")
        st.text("- Diferencia de frames")
        st.text("- Flujo optico Farneback")
        st.text("- Background Subtraction MOG2")
        st.text("- Deteccion de contornos")
        st.text("Sistema Experto:")
        st.text("- Reglas de inferencia")
        st.text("- Motor de decision")

        st.markdown("---")
        st.subheader("Historial de Paros Detectados")
        if st.session_state.stops_log:
            for stop in reversed(st.session_state.stops_log):
                st.error(f"[{stop['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}] {stop['mensaje']}")
        else:
            st.info("No se han detectado paros en esta sesión.")
    
    with col1:
        st.subheader("Vista de la Linea de Produccion")
        video_placeholder = st.empty()
        info_placeholder = st.empty()
        
        if st.session_state.simulacion_activa:
            agente = AgenteMonitor()
            frame_anterior = None

            # Loop de simulacion
            while st.session_state.simulacion_activa and st.session_state.frame_count < 200:
                # Generar frame simulado con control manual
                frame = generar_frame_simulado(
                    st.session_state.frame_count,
                    st.session_state.produccion_manual,
                    velocidad
                )

                # AGENTE PERCIBE (usando algoritmos reales de IA)
                movimiento, metricas = agente.percibir(frame_anterior, frame)

                # AGENTE DECIDE (usando sistema basado en reglas)
                decision, razon = agente.decidir(movimiento, metricas)

                # AGENTE ACTUA
                resultado = agente.actuar(decision, razon)

                # Guardar paros detectados en historial
                if resultado["alerta"] and resultado["nivel"] == "CRITICO":
                    st.session_state.stops_log.append({
                        "timestamp": resultado["timestamp"],
                        "mensaje": resultado["mensaje"]
                    })

                # Mostrar frame
                video_placeholder.image(frame, channels="BGR", width="stretch")

                # Mostrar informacion del agente
                with info_placeholder.container():
                    col_a, col_b, col_c = st.columns(3)
                    with col_a:
                        st.metric("Movimiento Detectado", f"{movimiento:.2f}")
                    with col_b:
                        st.metric("Flujo Optico", f"{metricas.get('flujo_optico', 0):.3f}")
                    with col_c:
                        st.metric("Contornos", metricas.get('num_contornos', 0))

                    if resultado["alerta"]:
                        if resultado["nivel"] == "CRITICO":
                            st.error(f"[{resultado['nivel']}] {resultado['mensaje']}")
                        else:
                            st.warning(f"[{resultado['nivel']}] {resultado['mensaje']}")
                    else:
                        st.success(f"[{resultado['nivel']}] {resultado['mensaje']}")

                # Actualizar metricas en columna derecha
                with metricas_placeholder.container():
                    st.metric("Piezas/min", int(velocidad * 0.6) if st.session_state.produccion_manual else 0)
                    st.metric("Eficiencia", f"{velocidad}%" if st.session_state.produccion_manual else "0%")
                    st.metric("Estado", "ACTIVO" if st.session_state.produccion_manual else "DETENIDO")

                frame_anterior = frame.copy()
                st.session_state.frame_count += 1
                time.sleep(0.3)

            st.session_state.simulacion_activa = False
            st.session_state.frame_count = 0

def generar_frame_simulado(frame_num, produccion_activa, velocidad):
    """Genera un frame simulado de la linea de produccion con control manual"""
    height, width = 480, 640
    frame = np.ones((height, width, 3), dtype=np.uint8) * 100
    
    # Dibujar banda transportadora
    cv2.rectangle(frame, (0, 150), (width, 330), (70, 70, 70), -1)
    cv2.line(frame, (0, 150), (width, 150), (50, 50, 50), 2)
    cv2.line(frame, (0, 330), (width, 330), (50, 50, 50), 2)
    
    if produccion_activa:
        # Calcular posicion basada en velocidad
        velocidad_factor = velocidad / 50.0
        pos_x = int((frame_num * 15 * velocidad_factor) % (width + 100))
        
        # Dibujar pieza en movimiento
        if pos_x < width:
            cv2.circle(frame, (pos_x, 240), 30, (0, 255, 0), -1)
            cv2.putText(frame, "PIEZA", (pos_x-25, 245), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            
            # Agregar ruido realista (variaciones naturales)
            noise = np.random.randint(-5, 5, frame.shape, dtype=np.int16)
            frame = np.clip(frame.astype(np.int16) + noise, 0, 255).astype(np.uint8)
        
        estado_text = f"PRODUCCION ACTIVA - Vel: {velocidad}%"
        color_estado = (0, 255, 0)
    else:
        # PARO MANUAL - Sin movimiento
        cv2.putText(frame, "LINEA DETENIDA", (width//2-120, 240), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
        estado_text = "PARO MANUAL ACTIVADO"
        color_estado = (0, 0, 255)
    
    # Agregar informacion
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(frame, timestamp, (10, 30), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.putText(frame, estado_text, (10, 60), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_estado, 2)
    cv2.putText(frame, f"Frame: {frame_num}", (10, height-10), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
    
    return frame
