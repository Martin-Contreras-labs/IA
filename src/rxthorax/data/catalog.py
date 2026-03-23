from dataclasses import dataclass


@dataclass(frozen=True)
class DatasetSpec:
    name: str
    label_schema: str
    task_type: str
