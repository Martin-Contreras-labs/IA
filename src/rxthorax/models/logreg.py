from __future__ import annotations

from dataclasses import dataclass, field
import math

from rxthorax.domain.enums import PathologyLabel
from rxthorax.domain.records import FeatureVector
from rxthorax.domain.results import PredictionResult


@dataclass
class LogRegBaseline:
    """Regresión logística binaria mínima para H1 (normal vs pneumonia)."""

    learning_rate: float = 0.1
    epochs: int = 400
    l2: float = 0.0
    weights: list[float] = field(default_factory=list)
    bias: float = 0.0

    def fit(self, features: list[FeatureVector], labels: list[PathologyLabel]) -> None:
        if not features:
            raise ValueError("Expected at least one feature vector for training")

        n_features = len(features[0].values)
        self.weights = [0.0] * n_features
        self.bias = 0.0

        targets = [1.0 if label == PathologyLabel.PNEUMONIA else 0.0 for label in labels]
        samples = [list(vector.values) for vector in features]

        for _ in range(self.epochs):
            grad_w = [0.0] * n_features
            grad_b = 0.0

            for x_i, y_i in zip(samples, targets, strict=True):
                prob = self._sigmoid(self._linear(x_i))
                error = prob - y_i
                grad_b += error
                for j in range(n_features):
                    grad_w[j] += error * x_i[j]

            scale = 1.0 / len(samples)
            grad_b *= scale
            for j in range(n_features):
                grad_w[j] = grad_w[j] * scale + self.l2 * self.weights[j]
                self.weights[j] -= self.learning_rate * grad_w[j]

            self.bias -= self.learning_rate * grad_b

    def predict(self, feature_vector: FeatureVector) -> PredictionResult:
        confidence = self.predict_proba(feature_vector)
        label = PathologyLabel.PNEUMONIA if confidence >= 0.5 else PathologyLabel.NORMAL
        return PredictionResult(
            study_id=feature_vector.study_id,
            predicted_label=label,
            confidence=confidence,
        )

    def predict_proba(self, feature_vector: FeatureVector) -> float:
        if not self.weights:
            raise RuntimeError("Model must be fitted before calling predict_proba")
        return self._sigmoid(self._linear(list(feature_vector.values)))

    def _linear(self, sample: list[float]) -> float:
        return sum(weight * value for weight, value in zip(self.weights, sample, strict=True)) + self.bias

    @staticmethod
    def _sigmoid(value: float) -> float:
        if value >= 0:
            return 1.0 / (1.0 + math.exp(-value))
        exp_value = math.exp(value)
        return exp_value / (1.0 + exp_value)
