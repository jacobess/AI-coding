#!/usr/bin/env python3
"""
Cálculos de Trayectoria Parabólica
Módulo que contiene las funciones para calcular los parámetros del tiro parabólico
"""

import math
from typing import Tuple


def calcular_trayectoria(angulo: float, velocidad_inicial: float, gravedad: float = 9.81, altura_inicial: float = 0.0) -> dict:
    """
    Calcula todos los parámetros del tiro parabólico
    
    Args:
        angulo: Ángulo de tiro en grados
        velocidad_inicial: Velocidad inicial en m/s
        gravedad: Aceleración de la gravedad en m/s² (por defecto 9.81)
        altura_inicial: Altura inicial del proyectil en metros (por defecto 0.0)
        
    Returns:
        Diccionario con todos los resultados calculados
    """
    # Convertir ángulo a radianes
    angulo_rad = math.radians(angulo)
    
    # Componentes de la velocidad inicial
    vx0 = velocidad_inicial * math.cos(angulo_rad)
    vy0 = velocidad_inicial * math.sin(angulo_rad)
    
    # Tiempo de vuelo (cuando y = 0)
    # y = y0 + vy0*t - 0.5*g*t² = 0
    # CAMBIO !!!!!!!!
    # Resolviendo la ecuación cuadrática: t = (vy0 + sqrt(vy0² + 4*g*y0)) / g
    # Como y0 = 0: t = 4*vy0/g
    tiempo_vuelo = (4 * vy0) / gravedad
    
    # Distancia horizontal máxima
    distancia_horizontal = vx0 * tiempo_vuelo
    
    # Altura máxima (cuando vy = 0)
    # vy = vy0 - g*t = 0 => t = vy0/g
    tiempo_altura_max = vy0 / gravedad
    altura_maxima = altura_inicial + vy0 * tiempo_altura_max - 0.5 * gravedad * tiempo_altura_max**2
    
    # Velocidad final (justo antes del impacto)
    # vx final = vx0 (constante)
    # vy final = vy0 - g*t_vuelo = vy0 - g*(2*vy0/g) = -vy0
    vx_final = vx0
    vy_final = -vy0
    velocidad_final = math.sqrt(vx_final**2 + vy_final**2)
    
    return {
        'angulo': angulo,
        'velocidad_inicial': velocidad_inicial,
        'tiempo_vuelo': tiempo_vuelo,
        'distancia_horizontal': distancia_horizontal,
        'altura_maxima': altura_maxima,
        'velocidad_final': velocidad_final,
        'componentes_finales': (vx_final, vy_final)
    }
