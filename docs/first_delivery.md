# Primera entrega (H1)

## Objetivo

Construir el baseline inicial `Normal vs Patológico` usando un pipeline reproducible en Python con regresión logística.

## Alcance funcional

- Configuración del experimento en archivo JSON.
- Representación explícita de estudios radiológicos y particiones.
- Placeholders estructurales para normalización y resize.
- Extracción de características estadísticas.
- Entrenamiento y evaluación del clasificador baseline `LogReg` binario (normal vs pneumonia).
- Cálculo y reporte de métricas del primer hito.

## Entregables de código

- `src/rxthorax/pipelines/first_delivery.py`: orquesta la entrega y el flujo train/validation.
- `src/rxthorax/features/statistics.py`: calcula/declara features estadísticas.
- `src/rxthorax/models/logreg.py`: encapsula el clasificador de regresión logística.
- `src/rxthorax/evaluation/metrics.py`: define métricas del baseline.
- `configs/first_delivery.json`: centraliza parámetros de ejecución.
- `scripts/run_h1_logreg.py`: ejecuta el flujo end-to-end reproducible.

## Ejecución reproducible

Comando exacto:

```bash
PYTHONPATH=src python scripts/run_h1_logreg.py
```

Salida esperada (formato):

```text
RxThorax - Primera entrega (H1)
Proyecto: RxThorax
Dataset activo: ChestX-ray14
Resumen: Entrega H1 sobre ChestX-ray14: normal_vs_pathological, features=statistical, classifier=logreg, train=8, val=2, val_accuracy=<valor>, avg_val_confidence=<valor>, preprocessing=resize(512x512), metrics=ClassificationMetrics(...)
```

## Siguiente paso recomendado

Conectar esta arquitectura a un dataset real y reemplazar los placeholders por:
1. lectura de metadata,
2. ingestión de imágenes,
3. split reproducible desde metadatos,
4. evaluación sobre conjunto de test.
