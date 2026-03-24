# Arquitectura técnica H1

## Propósito

Describir únicamente el flujo del hito H1 para construir y evaluar un baseline binario `Normal vs Patológico`.

## Componentes H1

### Configuración
- `configs/first_delivery.json`
- Parámetros del experimento: split, etiqueta binaria, tamaño objetivo y baseline.

### Dominio
- `PathologyLabel`
- `StudySplit`
- `ChestStudyRecord`
- `FeatureVector`
- `PredictionResult`
- `ExperimentReport`

### Datos
- `DatasetSpec` para declarar el dataset activo.
- Registros de estudios para alimentar el pipeline H1.

### Preprocesamiento
- `RadiographNormalizer`
- `RadiographResizer`

### Features
- `StatisticalFeatureExtractor` para transformar imágenes en vectores numéricos.

### Modelo
- `BaselineClassifier` como clasificador binario del hito.

### Evaluación
- `ClassificationMetrics` para resumen de desempeño del baseline.

### Orquestación
- `FirstDeliveryPipeline` integra configuración, datos, preprocesamiento, features, modelo y métricas.

## Flujo H1 (end-to-end)

1. `FirstDeliveryPipeline` carga configuración.
2. Se declara el dataset y se obtienen registros de estudio.
3. Se aplica split (`train`, `validation`, `test`).
4. Se ejecuta normalización y resize por imagen.
5. Se extraen características estadísticas.
6. Se entrena/infiere con clasificador binario baseline.
7. Se calculan métricas y se emite `ExperimentReport`.

## Estructura relevante del repositorio

```text
configs/
  first_delivery.json

docs/
  architecture.md
  first_delivery.md

src/rxthorax/
  config/
  data/
  domain/
  preprocessing/
  features/
  models/
  evaluation/
  pipelines/
```
