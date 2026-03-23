from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path


@dataclass(frozen=True)
class ImageSettings:
    target_width: int
    target_height: int
    normalize: bool


@dataclass(frozen=True)
class BaselineSettings:
    mode: str
    feature_family: str
    classifier: str


@dataclass(frozen=True)
class EvaluationSettings:
    metrics: tuple[str, ...]


@dataclass(frozen=True)
class ProjectSettings:
    name: str
    delivery: str
    active_dataset: str
    images: ImageSettings
    baseline: BaselineSettings
    evaluation: EvaluationSettings

    @classmethod
    def from_json(cls, config_path: Path) -> "ProjectSettings":
        with config_path.open("r", encoding="utf-8") as handler:
            data = json.load(handler)

        return cls(
            name=data["project"]["name"],
            delivery=data["project"]["delivery"],
            active_dataset=data["project"]["active_dataset"],
            images=ImageSettings(**data["images"]),
            baseline=BaselineSettings(**data["baseline"]),
            evaluation=EvaluationSettings(metrics=tuple(data["evaluation"]["metrics"])),
        )
