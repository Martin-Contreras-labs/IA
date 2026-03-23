# RxThorax - Diagnóstico asistido en radiografías de tórax

Arquitectura técnica inicial del proyecto replanteada para **Python + PyTorch**, priorizando una **primera entrega enfocada en H1**:
normalización de imágenes, extracción de características estadísticas y clasificación base **Normal vs Patológico**.

## Primera entrega propuesta

La primera entrega deja preparado el proyecto para construir un baseline reproducible con estas piezas:

1. **Configuración centralizada** en `configs/first_delivery.json`.
2. **Modelado del dominio** para estudios, etiquetas, particiones y resultados.
3. **Capa de datos** para declarar datasets, splits y registros de radiografías.
4. **Preprocesamiento** orientado a normalización y redimensionamiento.
5. **Extracción de características estadísticas** para un baseline tabular.
6. **Pipeline H1** para conectar configuración, datos, features, entrenamiento y evaluación.
7. **Documentación** para que la siguiente iteración implemente lectura real de `ChestX-ray14` o `CheXpert`.

## Estructura de carpetas

- `configs/`: configuración de la primera entrega.
- `docs/`: arquitectura técnica y alcance del hito inicial.
- `src/rxthorax/cli.py`: punto de entrada del proyecto.
- `src/rxthorax/config/`: carga de configuración y settings.
- `src/rxthorax/domain/`: entidades del problema clínico y experimental.
- `src/rxthorax/data/`: catálogos, registros, particiones y contratos de datasets.
- `src/rxthorax/preprocessing/`: normalización y resize de radiografías.
- `src/rxthorax/features/`: extracción de características para el baseline.
- `src/rxthorax/models/`: modelos base y espacio futuro para CNNs.
- `src/rxthorax/evaluation/`: métricas y reportes de validación.
- `src/rxthorax/pipelines/`: pipelines de entrenamiento/evaluación por entrega.

## Enfoque tecnológico

- **Lenguaje principal:** Python.
- **Framework objetivo:** PyTorch para etapas posteriores de CNN/XAI/retrieval.
- **En esta entrega:** solo se implementa el esqueleto del baseline H1 y su arquitectura, sin entrenamiento profundo todavía.
