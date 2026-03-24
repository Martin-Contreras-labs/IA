from __future__ import annotations

from dataclasses import dataclass

from rxthorax.features.statistics import FeatureVector


@dataclass(frozen=True)
class PredictionResult:
    study_id: str
    predicted_label: str
    confidence: float


class LogRegModel:
    """Modelo baseline estilo Logistic Regression para H1."""

    def __init__(self, decision_threshold: float = 5.0) -> None:
        self.decision_threshold = decision_threshold

    def predict(self, feature_vector: FeatureVector) -> PredictionResult:
        score = sum(feature_vector.values)
        label = "PNEUMONIA" if score > self.decision_threshold else "NORMAL"
        confidence = min(0.99, max(0.50, score / 10.0))
        return PredictionResult(
            study_id=feature_vector.study_id,
            predicted_label=label,
            confidence=confidence,
        )
