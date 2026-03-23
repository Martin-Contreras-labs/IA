from __future__ import annotations

from rxthorax.domain.records import FeatureVector
from rxthorax.preprocessing.transforms import NormalizedRadiograph


class StatisticalFeatureExtractor:
    FEATURE_NAMES = ("mean_intensity", "std_intensity", "contrast_proxy", "entropy_proxy")

    def extract(self, radiograph: NormalizedRadiograph) -> FeatureVector:
        seed = float(len(radiograph.study_id))
        values = (
            seed,
            seed / 10.0,
            float(radiograph.target_width) / 1000.0,
            float(radiograph.target_height) / 1000.0,
        )
        return FeatureVector(study_id=radiograph.study_id, values=values)
