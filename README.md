# Diagnóstico asistido en radiografías de tórax

Este repositorio contiene la arquitectura técnica inicial del proyecto de IA para diagnóstico asistido en radiografías de tórax.

## Alcance actual

En esta fase se define únicamente la estructura de carpetas y clases para soportar los objetivos del proyecto:
- OE1: extracción de características estadísticas y clasificación base
- OE2: CNN para detección/localización de patologías
- OE3: heatmaps para interpretabilidad
- OE4: búsqueda de casos similares mediante embeddings visuales

## Estructura de alto nivel

- `src/main/java/org/ia/rxthorax/app`: puntos de entrada
- `src/main/java/org/ia/rxthorax/config`: configuración general
- `src/main/java/org/ia/rxthorax/domain`: entidades del dominio clínico/técnico
- `src/main/java/org/ia/rxthorax/data`: acceso y preparación de datos
- `src/main/java/org/ia/rxthorax/features`: extracción de características para modelos base
- `src/main/java/org/ia/rxthorax/baseline`: pipeline H1 / OE1
- `src/main/java/org/ia/rxthorax/cnn`: pipeline H2 / OE2
- `src/main/java/org/ia/rxthorax/xai`: interpretabilidad H3 / OE3
- `src/main/java/org/ia/rxthorax/retrieval`: recuperación de casos similares OE4
- `src/main/java/org/ia/rxthorax/evaluation`: validación y análisis de errores H4
- `src/main/java/org/ia/rxthorax/orchestration`: coordinación entre componentes
- `docs/architecture.md`: descripción técnica de módulos y responsabilidades
