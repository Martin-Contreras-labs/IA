from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from rxthorax.domain.enums import PathologyLabel, StudySplit


@dataclass(frozen=True)
class ChestStudyRecord:
    study_id: str
    image_path: Path
    label: PathologyLabel
    split: StudySplit


@dataclass(frozen=True)
class FeatureVector:
    study_id: str
    values: tuple[float, ...]
