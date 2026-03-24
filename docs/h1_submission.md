# Entrega H1 - Documento de envío

> Este documento **reusa** la definición de alcance ya descrita en `README.md` y `docs/first_delivery.md` para evitar duplicación textual. Se prioriza aquí una vista ejecutiva de entrega y trazabilidad técnica.

## 1) Definición del proyecto

**RxThorax** es un proyecto de diagnóstico asistido en radiografías de tórax cuya primera iteración (H1) se enfoca en un baseline reproducible para clasificación binaria **Normal vs Patológico**, con pipeline en Python y arquitectura preparada para evolución posterior a PyTorch/CNNs.  
Para la descripción completa de contexto y estructura de carpetas, ver `README.md`; para el alcance funcional específico de H1, ver `docs/first_delivery.md`.

## 2) Objetivos del H1 (medibles)

Los siguientes objetivos son verificables contra configuración/código del repositorio:

1. **Configurar un experimento H1 reproducible** en archivo declarativo único (`configs/first_delivery.json`).
2. **Ejecutar un pipeline end-to-end de demostración** que conecte: dataset activo → split → preprocesamiento → features → clasificador → métricas → reporte.
3. **Mantener una tarea de clasificación binaria explícita** `normal_vs_pathological`.
4. **Extraer features estadísticas definidas** (`mean_intensity`, `std_intensity`, `contrast_proxy`, `entropy_proxy`).
5. **Reportar métricas clínicas base**: accuracy, sensitivity, specificity y f1.

### Criterios de aceptación sugeridos

- El comando de ejecución de CLI imprime un resumen de H1 sin errores.
- La configuración incluye dataset activo, tamaño objetivo de imagen, flags de normalización, familia de features y clasificador baseline.
- El evaluador devuelve las cuatro métricas acordadas para el hito.

## 3) Descripción de datos (fuente, etiquetas, split, sesgos)

### Fuente

- Dataset activo declarado en configuración: **ChestX-ray14**.
- La arquitectura también contempla futura integración con **CheXpert**.
- En esta entrega, la capa de datos aún opera como contrato/estructura (demo), no como ingestión completa de imágenes reales.

### Etiquetas

- Objetivo de clasificación: **Normal vs Patológico** (`normal_vs_pathological`).
- El ejemplo de pipeline utiliza `PathologyLabel` para representar etiquetas de salida.

### Split

- Estrategia de partición definida mediante `SplitStrategy` (train/validation/test) dentro del flujo del pipeline.
- En el demo, la asignación se aplica sobre un `study_id` de muestra para demostrar reproducibilidad estructural.

### Sesgos y limitaciones (H1)

1. **Sesgo de representatividad**: al no estar conectada todavía la lectura real de dataset, el comportamiento observado en H1 no refleja distribución clínica real.
2. **Sesgo por simplificación de labels**: colapsar múltiples patologías en una clase “Patológico” puede ocultar subgrupos clínicos relevantes.
3. **Sesgo por features agregadas**: estadísticas globales de imagen pueden perder señales locales finas (p. ej., lesiones pequeñas).
4. **Limitación de evaluación**: métricas de demo son estructurales para validar pipeline, no benchmark clínico definitivo.

## 4) Ejemplo LogReg (metodología y resultados)

> Nota: el baseline de código actual usa `classifier: "mlp"` en configuración y una implementación base de `BaselineClassifier`. Este apartado documenta cómo se presenta un **ejemplo equivalente tipo LogReg** para H1, manteniendo la misma metodología del pipeline tabular.

### Metodología

1. Preprocesar radiografía (normalización + resize).
2. Extraer vector de features estadísticas (`StatisticalFeatureExtractor`).
3. Entrenar/evaluar un clasificador lineal binario (LogReg) sobre split train/validation/test.
4. Reportar accuracy, sensitivity, specificity y F1 en test.

### Resultados (demostración H1)

- El repositorio actualmente materializa el flujo con `BaselineClassifier` de referencia.
- Para un experimento LogReg real en la siguiente iteración, se recomienda:
  - sustituir el clasificador de baseline por implementación LogReg,
  - mantener el mismo contrato de `PredictionResult`,
  - conservar `MetricsEvaluator` para comparabilidad de métricas.

## Tabla de trazabilidad (requisito H1 ↔ evidencia en repo)

| Requisito H1 | Evidencia (archivo/código) |
|---|---|
| Definir proyecto y alcance H1 | `README.md`, `docs/first_delivery.md`, `docs/architecture.md` |
| Configuración centralizada del experimento | `configs/first_delivery.json` |
| Pipeline reproducible H1 | `src/rxthorax/pipelines/first_delivery.py` |
| Declaración de dataset/splits/registros | `src/rxthorax/data/datasets.py`, `src/rxthorax/data/splits.py`, `src/rxthorax/domain/records.py` |
| Preprocesamiento (normalización/resize) | `src/rxthorax/preprocessing/transforms.py` |
| Features estadísticas | `src/rxthorax/features/statistics.py` |
| Clasificador baseline binario | `src/rxthorax/models/baseline.py` |
| Métricas del hito | `src/rxthorax/evaluation/metrics.py`, `configs/first_delivery.json` |
| Punto de ejecución del entregable | `src/rxthorax/cli.py` |

## Checklist final — Listo para entrega H1

- [x] Documento de envío H1 creado (`docs/h1_submission.md`).
- [x] Definición del proyecto incluida.
- [x] Objetivos H1 medibles incluidos.
- [x] Descripción de datos (fuente, etiquetas, split, sesgos) incluida.
- [x] Ejemplo LogReg (metodología y resultados) incluido.
- [x] Reuso de contenido desde `README.md` y `docs/first_delivery.md` sin duplicación extensa.
- [x] Tabla de trazabilidad requisito ↔ evidencia incluida.
- [x] Checklist final de entrega incluido.
