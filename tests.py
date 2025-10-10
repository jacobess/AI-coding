#!/usr/bin/env python3
"""
Conjunto de pruebas para la aplicación de Tiro Parabólico
Verifica que la implementación sea correcta mediante casos de prueba específicos
"""

import math
import unittest
from tiro_parabolico import TiroParabolico

class TestTiroParabolico(unittest.TestCase):
    """Clase de pruebas para TiroParabolico"""
    
    def setUp(self):
        """Configuración inicial para cada prueba"""
        self.simulador = TiroParabolico()
    
    def test_inicializacion(self):
        """Prueba la inicialización correcta del simulador"""
        self.assertEqual(self.simulador.g, 9.81)
        self.assertEqual(self.simulador.altura_inicial, 0.0)
    
    def test_angulo_45_grados_velocidad_10(self):
        """Prueba caso clásico: 45° con velocidad 10 m/s"""
        resultados = self.simulador.calcular_trayectoria(45, 10)
        
        # Verificaciones básicas
        self.assertEqual(resultados['angulo'], 45)
        self.assertEqual(resultados['velocidad_inicial'], 10)
        
        # Para 45°, vx0 = vy0 = v0/sqrt(2) = 10/sqrt(2) ≈ 7.07
        vx0_esperado = 10 * math.cos(math.radians(45))
        vy0_esperado = 10 * math.sin(math.radians(45))
        
        self.assertAlmostEqual(vx0_esperado, 7.071, places=2)
        self.assertAlmostEqual(vy0_esperado, 7.071, places=2)
        
        # Tiempo de vuelo = 2*vy0/g = 2*7.071/9.81 ≈ 1.44s
        tiempo_esperado = 2 * vy0_esperado / 9.81
        self.assertAlmostEqual(resultados['tiempo_vuelo'], tiempo_esperado, places=2)
        
        # Distancia horizontal = vx0 * tiempo_vuelo
        distancia_esperada = vx0_esperado * tiempo_esperado
        self.assertAlmostEqual(resultados['distancia_horizontal'], distancia_esperada, places=2)
        
        # Altura máxima = vy0²/(2*g) = (7.071)²/(2*9.81) ≈ 2.55m
        altura_esperada = (vy0_esperado**2) / (2 * 9.81)
        self.assertAlmostEqual(resultados['altura_maxima'], altura_esperada, places=2)
        
        # Velocidad final debe ser igual a la inicial (conservación de energía)
        self.assertAlmostEqual(resultados['velocidad_final'], 10, places=2)
    
    def test_angulo_0_grados(self):
        """Prueba tiro horizontal (0°)"""
        resultados = self.simulador.calcular_trayectoria(0, 10)
        
        # Con ángulo 0°, no hay componente vertical
        self.assertEqual(resultados['altura_maxima'], 0)
        self.assertEqual(resultados['tiempo_vuelo'], 0)
        self.assertEqual(resultados['distancia_horizontal'], 0)
        self.assertEqual(resultados['velocidad_final'], 10)
    
    def test_angulo_90_grados(self):
        """Prueba tiro vertical (90°)"""
        resultados = self.simulador.calcular_trayectoria(90, 10)
        
        # Con ángulo 90°, no hay componente horizontal
        self.assertEqual(resultados['distancia_horizontal'], 0)
        
        # Tiempo de vuelo = 2*vy0/g = 2*10/9.81 ≈ 2.04s
        tiempo_esperado = 2 * 10 / 9.81
        self.assertAlmostEqual(resultados['tiempo_vuelo'], tiempo_esperado, places=2)
        
        # Altura máxima = vy0²/(2*g) = 100/(2*9.81) ≈ 5.10m
        altura_esperada = (10**2) / (2 * 9.81)
        self.assertAlmostEqual(resultados['altura_maxima'], altura_esperada, places=2)
    
    def test_angulo_30_grados_velocidad_20(self):
        """Prueba caso específico: 30° con velocidad 20 m/s"""
        resultados = self.simulador.calcular_trayectoria(30, 20)
        
        # Componentes de velocidad
        vx0 = 20 * math.cos(math.radians(30))  # ≈ 17.32
        vy0 = 20 * math.sin(math.radians(30))  # = 10
        
        # Verificaciones manuales
        tiempo_esperado = 2 * vy0 / 9.81
        distancia_esperada = vx0 * tiempo_esperado
        altura_esperada = (vy0**2) / (2 * 9.81)
        
        self.assertAlmostEqual(resultados['tiempo_vuelo'], tiempo_esperado, places=2)
        self.assertAlmostEqual(resultados['distancia_horizontal'], distancia_esperada, places=2)
        self.assertAlmostEqual(resultados['altura_maxima'], altura_esperada, places=2)
        self.assertAlmostEqual(resultados['velocidad_final'], 20, places=2)
    
    def test_conservacion_energia(self):
        """Prueba que se conserve la energía (velocidad final = velocidad inicial)"""
        casos = [(30, 15), (60, 25), (45, 30)]
        
        for angulo, velocidad in casos:
            with self.subTest(angulo=angulo, velocidad=velocidad):
                resultados = self.simulador.calcular_trayectoria(angulo, velocidad)
                self.assertAlmostEqual(resultados['velocidad_final'], velocidad, places=2)
    
    def test_simetria_angulos_complementarios(self):
        """Prueba que ángulos complementarios den la misma distancia horizontal"""
        velocidad = 20
        angulo1 = 30
        angulo2 = 60  # Complementario
        
        resultados1 = self.simulador.calcular_trayectoria(angulo1, velocidad)
        resultados2 = self.simulador.calcular_trayectoria(angulo2, velocidad)
        
        # Los ángulos complementarios deben dar la misma distancia horizontal
        self.assertAlmostEqual(resultados1['distancia_horizontal'], 
                              resultados2['distancia_horizontal'], places=2)
    
    def test_angulo_optimo_45_grados(self):
        """Prueba que 45° da la máxima distancia horizontal"""
        velocidad = 15
        angulos = [30, 45, 60]
        distancias = []
        
        for angulo in angulos:
            resultados = self.simulador.calcular_trayectoria(angulo, velocidad)
            distancias.append(resultados['distancia_horizontal'])
        
        # 45° debe dar la mayor distancia
        self.assertEqual(distancias.index(max(distancias)), 1)  # 45° está en índice 1
    
    def test_generar_puntos_trayectoria(self):
        """Prueba la generación de puntos para la trayectoria"""
        x_pos, y_pos = self.simulador.generar_puntos_trayectoria(45, 10, 10)
        
        # Verificaciones básicas
        self.assertEqual(len(x_pos), 10)
        self.assertEqual(len(y_pos), 10)
        
        # El primer punto debe ser (0, 0)
        self.assertEqual(x_pos[0], 0)
        self.assertEqual(y_pos[0], 0)
        
        # El último punto debe tener y = 0 (impacto)
        self.assertAlmostEqual(y_pos[-1], 0, places=2)
        
        # La trayectoria debe ser parabólica (y debe tener un máximo)
        max_y = max(y_pos)
        self.assertGreater(max_y, 0)
    
    def test_casos_limite(self):
        """Prueba casos límite y valores extremos"""
        # Velocidad muy pequeña
        resultados = self.simulador.calcular_trayectoria(45, 0.1)
        self.assertGreater(resultados['tiempo_vuelo'], 0)
        self.assertGreater(resultados['distancia_horizontal'], 0)
        
        # Velocidad grande
        resultados = self.simulador.calcular_trayectoria(45, 100)
        self.assertGreater(resultados['tiempo_vuelo'], 0)
        self.assertGreater(resultados['distancia_horizontal'], 0)
        self.assertGreater(resultados['altura_maxima'], 0)
    
    def test_formulas_fisicas(self):
        """Prueba que las fórmulas físicas sean correctas"""
        angulo = 45
        velocidad = 20
        resultados = self.simulador.calcular_trayectoria(angulo, velocidad)
        
        # Verificar fórmula del tiempo de vuelo: t = 2*vy0/g
        vy0 = velocidad * math.sin(math.radians(angulo))
        tiempo_teorico = 2 * vy0 / 9.81
        self.assertAlmostEqual(resultados['tiempo_vuelo'], tiempo_teorico, places=2)
        
        # Verificar fórmula de altura máxima: h = vy0²/(2*g)
        altura_teorica = (vy0**2) / (2 * 9.81)
        self.assertAlmostEqual(resultados['altura_maxima'], altura_teorica, places=2)
        
        # Verificar fórmula de distancia horizontal: d = vx0 * t
        vx0 = velocidad * math.cos(math.radians(angulo))
        distancia_teorica = vx0 * tiempo_teorico
        self.assertAlmostEqual(resultados['distancia_horizontal'], distancia_teorica, places=2)

def ejecutar_pruebas_manuales():
    """Ejecuta algunas pruebas manuales adicionales"""
    print("\n" + "="*60)
    print("PRUEBAS MANUALES ADICIONALES")
    print("="*60)
    
    simulador = TiroParabolico()
    
    # Caso 1: Verificación con valores conocidos
    print("\n1. Caso de verificación: 45°, 20 m/s")
    resultados = simulador.calcular_trayectoria(45, 20)
    print(f"   Distancia horizontal: {resultados['distancia_horizontal']:.2f} m")
    print(f"   Altura máxima: {resultados['altura_maxima']:.2f} m")
    print(f"   Tiempo de vuelo: {resultados['tiempo_vuelo']:.2f} s")
    
    # Verificación manual: para 45° y v=20 m/s
    # vx0 = vy0 = 20/√2 ≈ 14.14 m/s
    # t = 2*14.14/9.81 ≈ 2.88 s
    # d = 14.14 * 2.88 ≈ 40.8 m
    # h = (14.14)²/(2*9.81) ≈ 10.2 m
    print("   Valores esperados: d≈40.8m, h≈10.2m, t≈2.88s")
    
    # Caso 2: Comparación de ángulos
    print("\n2. Comparación de ángulos con v=15 m/s:")
    for angulo in [30, 45, 60]:
        resultados = simulador.calcular_trayectoria(angulo, 15)
        print(f"   {angulo}°: d={resultados['distancia_horizontal']:.2f}m, "
              f"h={resultados['altura_maxima']:.2f}m")
    
    # Caso 3: Verificación de conservación de energía
    print("\n3. Verificación de conservación de energía:")
    casos = [(30, 10), (45, 15), (60, 20)]
    for angulo, velocidad in casos:
        resultados = simulador.calcular_trayectoria(angulo, velocidad)
        diferencia = abs(resultados['velocidad_final'] - velocidad)
        print(f"   {angulo}°, v={velocidad}: v_final={resultados['velocidad_final']:.2f} "
              f"(diferencia: {diferencia:.4f})")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    # Ejecutar pruebas unitarias
    print("Ejecutando pruebas unitarias...")
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    # Ejecutar pruebas manuales
    ejecutar_pruebas_manuales()