from __future__ import annotations

from dataclasses import dataclass

from rxthorax.domain.enums import PathologyLabel


@dataclass(frozen=True)
class PredictionResult:
    study_id: str
    predicted_label: PathologyLabel
    confidence: float


@dataclass(frozen=True)
class ClassificationMetrics:
    accuracy: float
    sensitivity: float
    specificity: float
    f1_score: float


@dataclass(frozen=True)
class ExperimentReport:
    project_name: str
    delivery: str
    dataset_name: str
    summary: str
