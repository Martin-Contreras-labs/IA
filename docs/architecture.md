# Arquitectura técnica propuesta

## 1. Objetivo general

Construir una plataforma modular para apoyo al diagnóstico médico en radiografías de tórax, separando claramente:
1. ingestión y normalización de datos,
2. modelos baseline y profundos,
3. interpretabilidad,
4. recuperación de casos similares,
5. evaluación clínica.

## 2. Capas del sistema

### `app`
Contiene los puntos de entrada del sistema y ejecuta el orquestador principal.

### `config`
Centraliza parámetros globales como rutas de datasets, tamaños de imagen, clases objetivo y banderas de ejecución.

### `domain`
Modela conceptos del problema: etiquetas patológicas, particiones del dataset, predicciones, embeddings y reportes.

### `data`
Gestiona datasets (`ChestX-ray14`, `CheXpert`), parsing de metadatos, normalización, particionado y preparación de ejemplos.

### `features`
Define el pipeline de características estadísticas para el baseline inicial.

### `baseline`
Implementa la clasificación preliminar `Normal vs Pathological` mediante características tabulares y un MLP/clasificador lineal.

### `cnn`
Agrupa modelos convolucionales para clasificación y localización de hallazgos radiológicos.

### `xai`
Provee interfaces y clases para generar heatmaps explicativos sobre predicciones.

### `retrieval`
Gestiona la creación de embeddings visuales y la búsqueda de estudios similares.

### `evaluation`
Calcula métricas, consolida reportes y habilita el análisis de falsos negativos/positivos.

### `orchestration`
Conecta todos los módulos en pipelines ejecutables por etapa.

## 3. Flujo propuesto

1. `DatasetLoader` carga imágenes y etiquetas.
2. `ImageNormalizer` y `DatasetSplitter` preparan los datos.
3. `StatisticalFeatureExtractor` alimenta el baseline (`baseline`).
4. `PneumoniaDetectionModel`/`OpacityLocalizationModel` soportan la etapa CNN.
5. `HeatmapGenerator` explica predicciones del modelo profundo.
6. `VisualEncoder` genera embeddings para `SimilarCaseRetriever`.
7. `MetricsEvaluator` y `ErrorAnalysisService` cierran la validación.

## 4. Principios de diseño

- **Modularidad:** cada objetivo del proyecto tiene su propio paquete.
- **Extensibilidad:** loaders, modelos y generadores de heatmaps están definidos mediante interfaces cuando conviene.
- **Trazabilidad:** evaluación y reportes separados del entrenamiento.
- **Escalabilidad:** la estructura permite migrar a integraciones con frameworks externos sin cambiar el dominio.
