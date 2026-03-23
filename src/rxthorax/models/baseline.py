from __future__ import annotations

from dataclasses import dataclass

from rxthorax.domain.enums import PathologyLabel
from rxthorax.domain.records import FeatureVector
from rxthorax.domain.results import PredictionResult


@dataclass(frozen=True)
class BaselineModelSpec:
    mode: str
    classifier: str


class BaselineClassifier:
    def __init__(self, spec: BaselineModelSpec) -> None:
        self.spec = spec

    def predict(self, feature_vector: FeatureVector) -> PredictionResult:
        score = sum(feature_vector.values)
        label = PathologyLabel.PNEUMONIA if score > 5.0 else PathologyLabel.NORMAL
        confidence = min(0.99, max(0.50, score / 10.0))
        return PredictionResult(
            study_id=feature_vector.study_id,
            predicted_label=label,
            confidence=confidence,
        )
