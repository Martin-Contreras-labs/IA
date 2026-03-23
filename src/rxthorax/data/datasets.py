from __future__ import annotations

from rxthorax.data.catalog import DatasetSpec


class DatasetRepository:
    """Registry de datasets soportados por la arquitectura."""

    def get(self, dataset_name: str) -> DatasetSpec:
        if dataset_name == "ChestX-ray14":
            return DatasetSpec(name="ChestX-ray14", label_schema="multi-label", task_type="classification")
        if dataset_name == "CheXpert":
            return DatasetSpec(name="CheXpert", label_schema="uncertain multi-label", task_type="classification")
        raise ValueError(f"Unsupported dataset: {dataset_name}")
