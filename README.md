# RxThorax - Hito H1

> Documento principal del hito: [Primera entrega (H1)](docs/first_delivery.md)

## Definición (H1)

H1 define un baseline mínimo y reproducible para clasificación binaria en radiografías de tórax: **Normal vs Patológico**.

## Objetivos (H1)

1. Establecer una ejecución reproducible mediante configuración (`configs/first_delivery.json`).
2. Estandarizar preprocesamiento básico (normalización y resize).
3. Generar características estadísticas para representar cada estudio.
4. Entrenar y evaluar un clasificador base binario.

## Datos (H1)

- El alcance H1 trabaja sobre la abstracción de estudios radiológicos (`ChestStudyRecord`) y particiones (`train`, `validation`, `test`).
- El pipeline está preparado para consumir registros ya definidos por la capa de datos.
- El objetivo de etiqueta en H1 es únicamente binario: `Normal` o `Patológico`.

## Ejemplo de baseline: Regresión Logística (LogReg)

Flujo resumido del baseline H1:

1. Cargar configuración del experimento.
2. Aplicar preprocesamiento de imagen (normalización + resize).
3. Extraer vector de características estadísticas.
4. Entrenar un clasificador LogReg `Normal vs Patológico`.
5. Reportar métricas de clasificación del hito.

## Fuera de alcance H1

- Modelos CNN y variantes profundas.
- Explicabilidad visual (p. ej., heatmaps).
- Retrieval por embeddings.
- Desarrollo de hitos posteriores H2/H3/H4.
