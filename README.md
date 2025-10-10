# Tiro Parabólico - Simulador de Proyectil

Esta aplicación simula el movimiento de un proyectil en un plano cartesiano, calculando todos los parámetros importantes del tiro parabólico.

## Características

- **Altura inicial**: 0 metros
- **Aceleración de la gravedad**: 9.81 m/s²
- **Simulación completa** hasta el impacto con el suelo

## Entradas (Inputs)

- **Ángulo de tiro**: En grados (0-90°)
- **Velocidad inicial**: En m/s

## Salidas (Outputs)

- **Distancia horizontal**: Alcance máximo del proyectil
- **Altura máxima**: Punto más alto alcanzado
- **Tiempo de vuelo**: Duración total del vuelo
- **Velocidad final**: Velocidad al momento del impacto
- **Gráfica de la trayectoria**: Visualización del movimiento

## Instalación

1. Asegúrate de tener Python 3.7+ instalado
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

Ejecuta el script principal:

```bash
python tiro_parabolico.py
```

El programa te pedirá:
1. El ángulo de tiro (0-90 grados)
2. La velocidad inicial (en m/s)

Después mostrará todos los resultados calculados y te preguntará si deseas ver la gráfica de la trayectoria.

## Ejemplo de uso

```
TIRO PARABÓLICO - Simulador de Proyectil
========================================
Esta aplicación simula el movimiento de un proyectil
con altura inicial = 0 y gravedad = 9.81 m/s²
========================================

Ingrese el ángulo de tiro (en grados, 0-90): 45
Ingrese la velocidad inicial (en m/s): 20

==================================================
RESULTADOS DEL TIRO PARABÓLICO
==================================================
Ángulo de tiro: 45.00°
Velocidad inicial: 20.00 m/s
Distancia horizontal: 40.77 m
Altura máxima: 10.19 m
Tiempo de vuelo: 2.88 s
Velocidad final: 20.00 m/s
Componentes finales: vx = 14.14 m/s, vy = -14.14 m/s
==================================================

¿Desea ver la gráfica de la trayectoria? (s/n): s
```

## Archivos generados

- `trayectoria_tiro_parabolico.png`: Gráfica de la trayectoria (si se selecciona la opción)

## Física implementada

El programa utiliza las ecuaciones del movimiento parabólico:

- **Componentes de velocidad inicial**:
  - vx₀ = v₀ × cos(θ)
  - vy₀ = v₀ × sin(θ)

- **Tiempo de vuelo**: t = 2 × vy₀ / g

- **Distancia horizontal**: x = vx₀ × t

- **Altura máxima**: y_max = vy₀² / (2 × g)

- **Velocidad final**: v_final = √(vx₀² + vy_final²)
