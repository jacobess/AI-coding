#!/usr/bin/env python3
"""
Aplicación de Tiro Parabólico
Simula el movimiento de un proyectil en un plano cartesiano
"""

import math
import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple, List

class TiroParabolico:
    """Clase para simular el tiro parabólico de un proyectil"""
    
    def __init__(self, gravedad: float = 9.81):
        """
        Inicializa la simulación de tiro parabólico
        
        Args:
            gravedad: Aceleración de la gravedad en m/s² (por defecto 9.81)
        """
        self.g = gravedad
        self.altura_inicial = 0.0
        
    def calcular_trayectoria(self, angulo: float, velocidad_inicial: float) -> dict:
        """
        Calcula todos los parámetros del tiro parabólico
        
        Args:
            angulo: Ángulo de tiro en grados
            velocidad_inicial: Velocidad inicial en m/s
            
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
        # Resolviendo la ecuación cuadrática: t = (vy0 + sqrt(vy0² + 2*g*y0)) / g
        # Como y0 = 0: t = 2*vy0/g
        tiempo_vuelo = (2 * vy0) / self.g
        
        # Distancia horizontal máxima
        distancia_horizontal = vx0 * tiempo_vuelo
        
        # Altura máxima (cuando vy = 0)
        # vy = vy0 - g*t = 0 => t = vy0/g
        tiempo_altura_max = vy0 / self.g
        altura_maxima = self.altura_inicial + vy0 * tiempo_altura_max - 0.5 * self.g * tiempo_altura_max**2
        
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
    
    def generar_puntos_trayectoria(self, angulo: float, velocidad_inicial: float, 
                                 num_puntos: int = 100) -> Tuple[List[float], List[float]]:
        """
        Genera puntos para graficar la trayectoria
        
        Args:
            angulo: Ángulo de tiro en grados
            velocidad_inicial: Velocidad inicial en m/s
            num_puntos: Número de puntos para la trayectoria
            
        Returns:
            Tupla con listas de coordenadas x e y
        """
        angulo_rad = math.radians(angulo)
        vx0 = velocidad_inicial * math.cos(angulo_rad)
        vy0 = velocidad_inicial * math.sin(angulo_rad)
        
        # Calcular tiempo de vuelo
        tiempo_vuelo = (2 * vy0) / self.g
        
        # Generar puntos de tiempo
        tiempos = np.linspace(0, tiempo_vuelo, num_puntos)
        
        # Calcular posiciones
        x_positions = [vx0 * t for t in tiempos]
        y_positions = [self.altura_inicial + vy0 * t - 0.5 * self.g * t**2 for t in tiempos]
        
        return x_positions, y_positions
    
    def graficar_trayectoria(self, angulo: float, velocidad_inicial: float, 
                           resultados: dict, guardar: bool = True):
        """
        Crea y muestra la gráfica de la trayectoria
        
        Args:
            angulo: Ángulo de tiro en grados
            velocidad_inicial: Velocidad inicial en m/s
            resultados: Diccionario con los resultados calculados
            guardar: Si guardar la gráfica como archivo
        """
        # Generar puntos de la trayectoria
        x_pos, y_pos = self.generar_puntos_trayectoria(angulo, velocidad_inicial)
        
        # Crear la gráfica
        plt.figure(figsize=(12, 8))
        plt.plot(x_pos, y_pos, 'b-', linewidth=2, label='Trayectoria del proyectil')
        
        # Marcar puntos importantes
        plt.plot(0, self.altura_inicial, 'go', markersize=10, label='Punto de lanzamiento')
        plt.plot(resultados['distancia_horizontal'], 0, 'ro', markersize=10, label='Punto de impacto')
        plt.plot(resultados['distancia_horizontal']/2, resultados['altura_maxima'], 
                'yo', markersize=10, label='Altura máxima')
        
        # Configurar la gráfica
        plt.xlabel('Distancia horizontal (m)', fontsize=12)
        plt.ylabel('Altura (m)', fontsize=12)
        plt.title(f'Trayectoria del Tiro Parabólico\n'
                 f'Ángulo: {angulo}°, Velocidad inicial: {velocidad_inicial} m/s', 
                 fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.axis('equal')
        
        # Añadir información en la gráfica
        info_text = (f'Distancia horizontal: {resultados["distancia_horizontal"]:.2f} m\n'
                    f'Altura máxima: {resultados["altura_maxima"]:.2f} m\n'
                    f'Tiempo de vuelo: {resultados["tiempo_vuelo"]:.2f} s\n'
                    f'Velocidad final: {resultados["velocidad_final"]:.2f} m/s')
        
        plt.text(0.02, 0.98, info_text, transform=plt.gca().transAxes, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        plt.tight_layout()
        
        if guardar:
            plt.savefig('trayectoria_tiro_parabolico.png', dpi=300, bbox_inches='tight')
            print("Gráfica guardada como 'trayectoria_tiro_parabolico.png'")
        
        plt.show()

def obtener_entrada_usuario() -> Tuple[float, float]:
    """
    Obtiene la entrada del usuario de forma segura
    
    Returns:
        Tupla con (ángulo, velocidad_inicial)
    """
    while True:
        try:
            angulo = float(input("Ingrese el ángulo de tiro (en grados, 0-90): "))
            if 0 <= angulo <= 90:
                break
            else:
                print("El ángulo debe estar entre 0 y 90 grados.")
        except ValueError:
            print("Por favor, ingrese un número válido para el ángulo.")
    
    while True:
        try:
            velocidad = float(input("Ingrese la velocidad inicial (en m/s): "))
            if velocidad > 0:
                break
            else:
                print("La velocidad inicial debe ser mayor que 0.")
        except ValueError:
            print("Por favor, ingrese un número válido para la velocidad.")
    
    return angulo, velocidad

def mostrar_resultados(resultados: dict):
    """
    Muestra los resultados de forma formateada
    
    Args:
        resultados: Diccionario con los resultados calculados
    """
    print("\n" + "="*50)
    print("RESULTADOS DEL TIRO PARABÓLICO")
    print("="*50)
    print(f"Ángulo de tiro: {resultados['angulo']:.2f}°")
    print(f"Velocidad inicial: {resultados['velocidad_inicial']:.2f} m/s")
    print(f"Distancia horizontal: {resultados['distancia_horizontal']:.2f} m")
    print(f"Altura máxima: {resultados['altura_maxima']:.2f} m")
    print(f"Tiempo de vuelo: {resultados['tiempo_vuelo']:.2f} s")
    print(f"Velocidad final: {resultados['velocidad_final']:.2f} m/s")
    print(f"Componentes finales: vx = {resultados['componentes_finales'][0]:.2f} m/s, "
          f"vy = {resultados['componentes_finales'][1]:.2f} m/s")
    print("="*50)

def main():
    """Función principal de la aplicación"""
    print("TIRO PARABÓLICO - Simulador de Proyectil")
    print("="*40)
    print("Esta aplicación simula el movimiento de un proyectil")
    print("con altura inicial = 0 y gravedad = 9.81 m/s²")
    print("="*40)
    
    # Crear instancia del simulador
    simulador = TiroParabolico()
    
    # Obtener entrada del usuario
    angulo, velocidad_inicial = obtener_entrada_usuario()
    
    # Calcular resultados
    resultados = simulador.calcular_trayectoria(angulo, velocidad_inicial)
    
    # Mostrar resultados
    mostrar_resultados(resultados)
    
    # Preguntar si desea ver la gráfica
    while True:
        respuesta = input("\n¿Desea ver la gráfica de la trayectoria? (s/n): ").lower()
        if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
            try:
                simulador.graficar_trayectoria(angulo, velocidad_inicial, resultados)
            except ImportError:
                print("Error: matplotlib no está instalado. Instale con: pip install matplotlib")
            break
        elif respuesta in ['n', 'no']:
            print("Simulación completada.")
            break
        else:
            print("Por favor, responda 's' para sí o 'n' para no.")

if __name__ == "__main__":
    main()
