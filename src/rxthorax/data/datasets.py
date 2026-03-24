from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DatasetSpec:
    name: str
    label_schema: str
    task_type: str


class DatasetRepository:
    """Registro de datasets soportados por el flujo H1."""

    _SUPPORTED_DATASETS: dict[str, DatasetSpec] = {
        "ChestX-ray14": DatasetSpec(
            name="ChestX-ray14",
            label_schema="multi-label",
            task_type="classification",
        ),
        "CheXpert": DatasetSpec(
            name="CheXpert",
            label_schema="uncertain multi-label",
            task_type="classification",
        ),
    }

    def get(self, dataset_name: str) -> DatasetSpec:
        try:
            return self._SUPPORTED_DATASETS[dataset_name]
        except KeyError as exc:
            raise ValueError(f"Unsupported dataset: {dataset_name}") from exc
