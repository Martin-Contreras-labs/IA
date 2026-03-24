from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PreparedStudy:
    study_id: str
    target_width: int
    target_height: int


@dataclass(frozen=True)
class FeatureVector:
    study_id: str
    values: tuple[float, ...]


class StatisticalFeatureExtractor:
    FEATURE_NAMES = ("mean_intensity", "std_intensity", "contrast_proxy", "entropy_proxy")

    def extract(self, study: PreparedStudy) -> FeatureVector:
        seed = float(len(study.study_id))
        values = (
            seed,
            seed / 10.0,
            float(study.target_width) / 1000.0,
            float(study.target_height) / 1000.0,
        )
        return FeatureVector(study_id=study.study_id, values=values)
