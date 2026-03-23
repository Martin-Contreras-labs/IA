# Primera entrega (H1)

## Objetivo

Construir el baseline inicial `Normal vs Patológico` usando un pipeline reproducible en Python.

## Alcance funcional

- Configuración del experimento en archivo JSON.
- Representación explícita de estudios radiológicos y particiones.
- Placeholders estructurales para normalización y resize.
- Extracción de características estadísticas.
- Clasificador baseline binario.
- Cálculo y reporte de métricas del primer hito.

## Entregables de código

- `src/rxthorax/pipelines/first_delivery.py`: orquesta la entrega.
- `src/rxthorax/features/statistics.py`: calcula/declara features estadísticas.
- `src/rxthorax/models/baseline.py`: encapsula el clasificador base.
- `src/rxthorax/evaluation/metrics.py`: define métricas del baseline.
- `configs/first_delivery.json`: centraliza parámetros de ejecución.

## Siguiente paso recomendado

Conectar esta arquitectura a un dataset real y reemplazar los placeholders por:
1. lectura de metadata,
2. ingestión de imágenes,
3. split reproducible,
4. entrenamiento/evaluación reales.
