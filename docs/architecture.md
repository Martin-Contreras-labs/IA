# Arquitectura técnica propuesta - Opción B (Python + PyTorch)

## 1. Objetivo del replanteamiento

Se migra el diseño inicial a Python porque encaja mejor con:
- visión por computador,
- experimentación con datasets médicos,
- integración con PyTorch,
- generación de heatmaps,
- recuperación basada en embeddings.

La **primera entrega** queda acotada a **H1**:
- normalización de radiografías,
- extracción de características estadísticas,
- clasificación base `Normal vs Patológico`,
- evaluación inicial reproducible.

## 2. Capas del proyecto

### `config`
Carga settings del experimento inicial: dataset, tamaño objetivo, etiqueta binaria, split y parámetros del baseline.

### `domain`
Contiene entidades transversales del problema:
- `PathologyLabel`
- `StudySplit`
- `ChestStudyRecord`
- `FeatureVector`
- `PredictionResult`
- `ExperimentReport`

### `data`
Modela la fuente de datos y los registros de estudios radiológicos.
En la primera entrega esta capa declara contratos y estructuras; en la siguiente debe conectarse a `ChestX-ray14` o `CheXpert`.

### `preprocessing`
Define transformaciones canónicas para radiografías:
- normalización de intensidad,
- resize,
- validaciones previas.

### `features`
Implementa el extractor estadístico que alimentará el baseline tabular.

### `models`
Agrupa modelos del sistema. En esta primera entrega solo existe el baseline binario. Más adelante se extenderá a CNNs, atención y retrieval.

### `evaluation`
Consolida métricas, reportes y análisis de errores del primer hito.

### `pipelines`
Conecta módulos para ejecutar una entrega concreta. En esta fase el pipeline principal es `FirstDeliveryPipeline`.

## 3. Flujo de la primera entrega

1. `FirstDeliveryPipeline` carga la configuración.
2. `DatasetSpec` declara el dataset activo.
3. `ChestStudyRecord` representa los estudios disponibles.
4. `SplitStrategy` separa `train`, `validation` y `test`.
5. `RadiographNormalizer` y `RadiographResizer` preparan las imágenes.
6. `StatisticalFeatureExtractor` transforma la radiografía en un vector numérico.
7. `BaselineClassifier` produce predicciones binarias.
8. `ClassificationMetrics` resume accuracy, sensibilidad, especificidad y F1.
9. `ExperimentReport` documenta los resultados de la entrega.

## 4. Estructura objetivo del repositorio

```text
configs/
  first_delivery.json

docs/
  architecture.md
  first_delivery.md

src/rxthorax/
  cli.py
  config/
    settings.py
  domain/
    enums.py
    records.py
    results.py
  data/
    catalog.py
    datasets.py
    splits.py
  preprocessing/
    transforms.py
  features/
    statistics.py
  models/
    baseline.py
  evaluation/
    metrics.py
  pipelines/
    first_delivery.py
```

## 5. Qué NO incluye todavía

Esta primera entrega **no** implementa aún:
- lectura real del dataset desde disco,
- entrenamiento con PyTorch,
- CNNs para neumonía u opacidades,
- Grad-CAM,
- retrieval por embeddings.

Sí deja preparado el diseño para agregar esas piezas en siguientes iteraciones sin reorganizar el proyecto completo.
